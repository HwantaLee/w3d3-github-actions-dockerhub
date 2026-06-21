# 6교시: 서비스 간 통신 확인

## 수업 목표
- frontend -> api, api -> db, worker -> api 흐름을 로그와 상태로 추적를 운영 증거로 확인한다.
- MSA를 기능 목록이 아니라 서비스 경계와 의존성으로 읽는다.
- 실패했을 때 다음에 볼 명령과 복구 기준을 말한다.

## 핵심 설명
frontend -> api, api -> db, worker -> api 연결을 각각 다른 증거로 확인한다.

## 실습 기준
```bash
cd week3/day1/labs/msa-demo
curl/logs/health
```

## 읽어야 할 증거
| 증거 | 의미 |
|---|---|
| `docker compose config` | service, env, port, healthcheck가 최종적으로 어떻게 해석되는지 |
| `docker compose ps` | container running과 health 상태 |
| `curl http://localhost:18083/api/status` | browser entrypoint에서 API까지 연결되는지 |
| `curl http://localhost:18084/health` | API가 DB까지 붙을 준비가 되었는지 |
| `docker compose logs api worker` | request id와 dependency 오류 |

## 주의할 점
한 서비스의 HTTP 200이 전체 정상은 아니다.



## Evidence Note
```markdown
# Evidence
- command:
- observed output:
- normal or failure:
- next action:
```
