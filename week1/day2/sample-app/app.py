from datetime import datetime, timezone
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


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


def get_int_env(name, default):
    value = os.getenv(name, str(default))
    try:
        return int(value)
    except ValueError:
        raise SystemExit(f"Invalid {name}: {value}. {name} must be a number.")


load_env_file(ENV_FILE)

APP_NAME = os.getenv("APP_NAME", "local-server-lab")
APP_MODE = os.getenv("APP_MODE", "local")
PORT = get_int_env("PORT", 8000)
LOG_FILE = ROOT / os.getenv("LOG_FILE", "logs/app.log")
SECRET_TOKEN = os.getenv("SECRET_TOKEN", "")

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


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


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, body):
        payload = json.dumps(body, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        if self.path == "/":
            body = {
                "status": "ok",
                "app": APP_NAME,
                "mode": APP_MODE,
                "port": PORT,
                "logFile": str(LOG_FILE.relative_to(ROOT)),
                "secretTokenConfigured": bool(SECRET_TOKEN),
            }
            write_log("INFO", "request handled", path=self.path, status=200)
            self.send_json(200, body)
            return

        if self.path == "/health":
            write_log("INFO", "health check", path=self.path, status=200)
            self.send_json(200, {"status": "healthy"})
            return

        if self.path == "/config":
            write_log("INFO", "config requested", path=self.path, status=200)
            self.send_json(
                200,
                {
                    "APP_NAME": APP_NAME,
                    "APP_MODE": APP_MODE,
                    "PORT": PORT,
                    "LOG_FILE": str(LOG_FILE.relative_to(ROOT)),
                    "SECRET_TOKEN": "[configured]" if SECRET_TOKEN else "[empty]",
                },
            )
            return

        if self.path == "/error":
            write_log("ERROR", "intentional error endpoint", path=self.path, status=500)
            self.send_json(500, {"error": "intentional error for log practice"})
            return

        write_log("WARN", "not found", path=self.path, status=404)
        self.send_json(404, {"error": "not found", "path": self.path})

    def log_message(self, fmt, *args):
        return


if __name__ == "__main__":
    write_log("INFO", "server starting", port=PORT, logFile=str(LOG_FILE))
    try:
        HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        write_log("INFO", "server stopped")
