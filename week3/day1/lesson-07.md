# 7교시: 장애 시나리오 1

## 수업 목표
- API URL 오류, DB host 오류, 환경변수 누락을 logs/inspect/exec로 분리를 운영 증거로 확인한다.
- MSA를 기능 목록이 아니라 서비스 경계와 의존성으로 읽는다.
- 실패했을 때 다음에 볼 명령과 복구 기준을 말한다.

## 핵심 설명
API 중지, DB 중지, env 오류는 증상이 다르다.

## 실습 기준
```bash
cd week3/day1/labs/msa-demo
stop api/db 후 curl/logs
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
첫 확인 명령을 정하고 복구 기준을 남긴다.



## Evidence Note
```markdown
# Evidence
- command:
- observed output:
- normal or failure:
- next action:
```
