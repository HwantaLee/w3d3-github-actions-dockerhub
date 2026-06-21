# Week 3 Day 2 Hands-on Lab: 장애 전파와 운영 리포트

## Phase 0. Day1 앱 재실행
```bash
cd week3/day1/labs/msa-demo
docker compose up --build -d
docker compose ps
```

## Phase 1. Baseline 수집
```bash
curl -s http://localhost:18083/api/status
curl -s http://localhost:18084/health
docker compose logs --tail=30 api
docker compose logs --tail=30 worker
```

Baseline이 없으면 장애 상태를 비교할 수 없다.

## Phase 2. Health와 readiness 비교
```bash
docker compose stop db
curl -i http://localhost:18084/health
docker compose ps
docker compose logs --tail=50 api
```

기록할 질문:

| 질문 | 답 |
|---|---|
| api container는 running인가 | |
| `/health`는 몇 번 status인가 | |
| DB가 내려간 증거는 어디에 있는가 | |

복구:

```bash
docker compose start db
```

## Phase 3. Worker 장애 전파
```bash
docker compose stop api
sleep 10
docker compose logs --tail=80 worker
docker compose start api
```

worker는 사용자 traffic을 직접 받지 않지만 api 장애의 영향을 받는다.

## Phase 4. Correlation id 확인
```bash
curl -s -H 'x-request-id: classroom-msa-001' http://localhost:18084/api/status
docker compose logs --tail=80 api | grep classroom-msa-001 || true
```

`|| true`는 grep 결과가 없어도 실습 스크립트를 멈추지 않기 위한 것이다. 실제 원인 확인 명령에는 남용하지 않는다.

## Phase 5. 운영 리포트 작성
`ops-report-template.md`를 열고 다음 항목을 채운다.

| 항목 | 기준 |
|---|---|
| symptom | 사용자가 본 증상 |
| impact | frontend/api/worker/db 중 영향받은 service |
| evidence | curl/logs/ps/health 핵심 출력 |
| likely cause | 설정, dependency, readiness, timeout 중 후보 |
| recovery | 실행한 복구 명령 |
| prevention | healthcheck, retry, env 검증, runbook 보강 |

## Cleanup
```bash
docker compose down
```
