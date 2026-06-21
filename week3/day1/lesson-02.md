# 2교시: Monolith vs MSA

## 수업 목표
- 배포 단위, 장애 영향 범위, 네트워크 의존성, 운영 복잡도 비교를 운영 증거로 확인한다.
- MSA를 기능 목록이 아니라 서비스 경계와 의존성으로 읽는다.
- 실패했을 때 다음에 볼 명령과 복구 기준을 말한다.

## 핵심 설명
Monolith는 배포/장애/데이터 책임이 한 덩어리이고, MSA는 책임을 나누는 대신 네트워크 의존성을 만든다.

## 실습 기준
```bash
cd week3/day1/labs/msa-demo
service boundary 표 작성
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
MSA는 무조건 좋은 구조가 아니라 운영 비용을 지불하는 구조다.



## Evidence Note
```markdown
# Evidence
- command:
- observed output:
- normal or failure:
- next action:
```
