# 8교시: 구름 EXP 배움일기

## 수업 목표
- MSA 토폴로지, 서비스별 실행 조건, 연결 실패에서 먼저 볼 증거를 운영 증거로 확인한다.
- MSA를 기능 목록이 아니라 서비스 경계와 의존성으로 읽는다.
- 실패했을 때 다음에 볼 명령과 복구 기준을 말한다.

## 핵심 설명
오늘 배운 토폴로지와 실패 증거를 배움일기로 정리한다.

## 실습 기준
```bash
cd week3/day1/labs/msa-demo
goorm EXP note
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
다음 날 장애 전파 수업의 질문을 남긴다.


## 구름 EXP 배움일기
| 항목 | 작성 가이드 |
|---|---|
| 오늘 이해한 토폴로지 | frontend, api, worker, db 연결 방향 |
| 실행 증거 | `docker compose ps`, `curl`, `logs` 중 하나 |
| 막힌 지점 | port, service name, env, health 중 하나 |
| 다음 질문 | Day2 장애 전파에서 확인하고 싶은 것 |


## Evidence Note
```markdown
# Evidence
- command:
- observed output:
- normal or failure:
- next action:
```
