from datetime import datetime, timezone
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from time import monotonic, sleep
from urllib.parse import parse_qs, urlparse
from uuid import uuid4


ROOT = Path(__file__).resolve().parent
ENV_FILE = ROOT / ".env"


def load_env_file(path):
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ[key.strip()] = value.strip()


load_env_file(ENV_FILE)

APP_NAME = os.getenv("APP_NAME", "checkout-observability-lab")
APP_MODE = os.getenv("APP_MODE", "local")
LOG_FILE = ROOT / os.getenv("LOG_FILE", "logs/app.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


def now():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def write_log(level, message, **fields):
    event = {
        "time": now(),
        "level": level,
        "app": APP_NAME,
        "mode": APP_MODE,
        "message": message,
        **fields,
    }
    line = json.dumps(event, ensure_ascii=False)
    print(line, flush=True)
    with LOG_FILE.open("a", encoding="utf-8") as log:
        log.write(line + "\n")


def get_config_int(name, default, minimum=None):
    raw = os.getenv(name, str(default))
    try:
        value = int(raw)
    except ValueError:
        write_log("ERROR", "config validation failed", setting=name, value=raw, reason="must be a number")
        raise SystemExit(f"Invalid {name}: {raw}. {name} must be a number.")
    if minimum is not None and value < minimum:
        write_log("ERROR", "config validation failed", setting=name, value=raw, reason=f"must be >= {minimum}")
        raise SystemExit(f"Invalid {name}: {raw}. {name} must be >= {minimum}.")
    return value


def get_config_choice(name, default, choices):
    value = os.getenv(name, default)
    if value not in choices:
        reason = f"must be one of {', '.join(choices)}"
        write_log("ERROR", "config validation failed", setting=name, value=value, reason=reason)
        raise SystemExit(f"Invalid {name}: {value}. {name} {reason}.")
    return value


PORT = get_config_int("PORT", 8010, minimum=1)
SLOW_MS = get_config_int("SLOW_MS", 0, minimum=0)
SLOW_THRESHOLD_MS = get_config_int("SLOW_THRESHOLD_MS", 500, minimum=1)
INVENTORY_LIMIT = get_config_int("INVENTORY_LIMIT", 5, minimum=0)
FAIL_STEP = get_config_choice("FAIL_STEP", "none", ["none", "validate", "inventory", "payment", "persist"])

METRICS = {
    "totalRequests": 0,
    "slowRequests": 0,
    "status": {},
    "durationsMs": [],
    "lastError": None,
}


def record_metric(status, duration_ms, error=None):
    METRICS["totalRequests"] += 1
    METRICS["status"][str(status)] = METRICS["status"].get(str(status), 0) + 1
    METRICS["durationsMs"].append(duration_ms)
    if duration_ms >= SLOW_THRESHOLD_MS:
        METRICS["slowRequests"] += 1
    if error:
        METRICS["lastError"] = error


def parse_int(name, query, default):
    raw = query.get(name, [default])[0]
    try:
        return int(raw)
    except ValueError:
        raise ValueError(f"{name} must be a number")


def validate_order(query, request_id):
    if FAIL_STEP == "validate":
        raise RuntimeError("forced failure at validate step")
    item = query.get("item", ["book"])[0]
    qty = parse_int("qty", query, "1")
    if qty <= 0:
        raise ValueError("qty must be greater than 0")
    write_log("INFO", "checkout step completed", requestId=request_id, step="validate", item=item, qty=qty)
    return {"item": item, "qty": qty}


def check_inventory(order, request_id):
    if FAIL_STEP == "inventory":
        raise RuntimeError("forced failure at inventory step")
    if order["qty"] > INVENTORY_LIMIT:
        write_log(
            "WARN",
            "checkout rejected",
            requestId=request_id,
            step="inventory",
            errorPoint="inventory",
            qty=order["qty"],
            inventoryLimit=INVENTORY_LIMIT,
            status=409,
            hint="reduce qty or increase INVENTORY_LIMIT",
        )
        return False
    write_log("INFO", "checkout step completed", requestId=request_id, step="inventory", available=True)
    return True


def authorize_payment(order, request_id):
    if FAIL_STEP == "payment":
        raise RuntimeError("forced failure at payment step")
    if SLOW_MS:
        sleep(SLOW_MS / 1000)
    amount = order["qty"] * 12000
    write_log("INFO", "checkout step completed", requestId=request_id, step="payment", amount=amount)
    return amount


def persist_order(amount, request_id):
    if FAIL_STEP == "persist":
        raise RuntimeError("forced failure at persist step")
    order_id = f"ord-{request_id[:8]}"
    write_log("INFO", "checkout step completed", requestId=request_id, step="persist", orderId=order_id)
    return {"orderId": order_id, "amount": amount}


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, body):
        payload = json.dumps(body, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        started = monotonic()
        request_id = uuid4().hex
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/health":
            self.send_json(200, {"status": "healthy"})
            return

        if path == "/config":
            write_log("INFO", "config requested", requestId=request_id, path=path, status=200)
            self.send_json(
                200,
                {
                    "APP_NAME": APP_NAME,
                    "APP_MODE": APP_MODE,
                    "PORT": PORT,
                    "LOG_FILE": str(LOG_FILE.relative_to(ROOT)),
                    "SLOW_MS": SLOW_MS,
                    "SLOW_THRESHOLD_MS": SLOW_THRESHOLD_MS,
                    "INVENTORY_LIMIT": INVENTORY_LIMIT,
                    "FAIL_STEP": FAIL_STEP,
                },
            )
            return

        if path == "/metrics":
            durations = METRICS["durationsMs"]
            avg_duration = round(sum(durations) / len(durations), 2) if durations else 0
            self.send_json(200, {**METRICS, "avgDurationMs": avg_duration, "slowThresholdMs": SLOW_THRESHOLD_MS})
            return

        if path == "/api/checkout":
            self.handle_checkout(query, request_id, started)
            return

        duration_ms = round((monotonic() - started) * 1000, 2)
        write_log("WARN", "not found", requestId=request_id, path=path, status=404, durationMs=duration_ms)
        record_metric(404, duration_ms, error={"requestId": request_id, "errorPoint": "route"})
        self.send_json(404, {"error": "not found", "requestId": request_id, "path": path})

    def handle_checkout(self, query, request_id, started):
        try:
            order = validate_order(query, request_id)
            if not check_inventory(order, request_id):
                duration_ms = round((monotonic() - started) * 1000, 2)
                record_metric(409, duration_ms, {"requestId": request_id, "errorPoint": "inventory"})
                self.send_json(409, {"error": "not enough inventory", "requestId": request_id})
                return
            amount = authorize_payment(order, request_id)
            result = persist_order(amount, request_id)
            duration_ms = round((monotonic() - started) * 1000, 2)
            level = "WARN" if duration_ms >= SLOW_THRESHOLD_MS else "INFO"
            write_log(
                level,
                "checkout completed",
                requestId=request_id,
                path="/api/checkout",
                status=200,
                durationMs=duration_ms,
                slowThresholdMs=SLOW_THRESHOLD_MS,
            )
            record_metric(200, duration_ms)
            self.send_json(200, {"status": "paid", "requestId": request_id, **result})
        except ValueError as error:
            duration_ms = round((monotonic() - started) * 1000, 2)
            write_log(
                "WARN",
                "checkout validation failed",
                requestId=request_id,
                step="validate",
                errorPoint="validate",
                error=str(error),
                status=400,
                durationMs=duration_ms,
                hint="check query string such as qty=1",
            )
            record_metric(400, duration_ms, {"requestId": request_id, "errorPoint": "validate"})
            self.send_json(400, {"error": str(error), "requestId": request_id})
        except RuntimeError as error:
            duration_ms = round((monotonic() - started) * 1000, 2)
            error_point = FAIL_STEP if FAIL_STEP != "none" else "application"
            write_log(
                "ERROR",
                "checkout failed",
                requestId=request_id,
                step=error_point,
                errorPoint=error_point,
                error=str(error),
                status=500,
                durationMs=duration_ms,
                hint="check FAIL_STEP and recent .env changes",
            )
            record_metric(500, duration_ms, {"requestId": request_id, "errorPoint": error_point})
            self.send_json(500, {"error": "checkout failed", "requestId": request_id, "errorPoint": error_point})

    def log_message(self, fmt, *args):
        return


if __name__ == "__main__":
    write_log(
        "INFO",
        "server starting",
        port=PORT,
        logFile=str(LOG_FILE),
        slowMs=SLOW_MS,
        slowThresholdMs=SLOW_THRESHOLD_MS,
        inventoryLimit=INVENTORY_LIMIT,
        failStep=FAIL_STEP,
    )
    try:
        HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        write_log("INFO", "server stopped")
