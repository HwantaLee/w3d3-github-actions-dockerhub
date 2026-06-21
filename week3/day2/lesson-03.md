# 3교시: timeout과 retry

## 수업 목표
- 무한 대기 방지, 재시도의 위험, 중복 처리 문제를 실제 운영 판단과 연결한다.
- running, healthy, ready, user-visible success를 구분한다.
- 장애 리포트에 남길 증거를 고른다.

## 핵심 설명
timeout은 무한 대기를 막고 retry는 일시 장애를 완화하지만 중복 처리 위험을 만든다.

## 실습 기준
```bash
cd week3/day1/labs/msa-demo
docker compose logs --tail=80 worker
```

## 판단 표
| 상황 | 먼저 볼 증거 | 다음 행동 |
|---|---|---|
| frontend는 열리지만 데이터가 안 보임 | frontend logs, api status | API URL/proxy 확인 |
| api가 running인데 503 | `/health`, api logs | DB host/readiness 확인 |
| worker가 반복 실패 | worker logs, API health | dependency 복구 또는 retry 간격 확인 |
| 원인 전달 필요 | ops report | 재현 조건과 핵심 출력만 첨부 |

## 리포트 문장 예시
```text
증상: frontend /api/status 요청이 503으로 실패했다.
증거: api /health에서 database_reachable=false를 확인했다.
원인 후보: DB container 중지 또는 DB_HOST 설정 오류.
복구: db start 후 /health 200 재확인.
```



## Evidence Note
```markdown
# Evidence
- command:
- observed output:
- normal or failure:
- next action:
```
