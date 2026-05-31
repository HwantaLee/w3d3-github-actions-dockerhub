# Week 1 Day 2 Observability App

8교시 원인 분석 실습용 체크아웃 API 샘플 앱이다. 7교시 `sample-app`과 분리해서, 여기서는 요청 단계, 지연, 실패 지점, 메트릭, 로그 분석을 연습한다.

## 실행

```bash
cp .env.example .env
python3 app2.py
```

다른 터미널에서 확인한다.

```bash
curl http://localhost:8010/config
curl "http://localhost:8010/api/checkout?item=book&qty=1"
curl http://localhost:8010/metrics
tail -n 20 logs/app.log
```

## 장애 재현

```bash
curl "http://localhost:8010/api/checkout?item=book&qty=abc"
curl "http://localhost:8010/api/checkout?item=book&qty=99"
```

`.env`를 수정하고 재기동한다.

```text
SLOW_MS=800
FAIL_STEP=payment
```

```bash
python3 app2.py
```
