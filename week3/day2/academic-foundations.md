# Week 3 Day2 Academic Foundations

## 수업 기준
Day 2는 Day 1의 실행 성공에서 끝나지 않고 부분 장애, readiness, timeout/retry, worker/queue, correlation id, 운영 리포트까지 압축한다.

## 공식/현업 참고 자료
| 자료 | URL | 연결 포인트 |
|---|---|---|
| Google SRE Cascading Failures | https://sre.google/sre-book/addressing-cascading-failures/ | 수업에서 확인할 키워드 |
| Docker Compose healthcheck | https://docs.docker.com/reference/compose-file/services/#healthcheck | 수업에서 확인할 키워드 |
| OpenTelemetry Concepts | https://opentelemetry.io/docs/concepts/ | 수업에서 확인할 키워드 |

## 수업 적용 원칙
- 공식 문서를 명령 암기 자료로 쓰지 않고, 어떤 상태를 확인하는 기준인지 읽는다.
- 정상/비정상 판단은 화면 인상보다 command output, log, event, health response로 남긴다.
- 보안 값과 token은 evidence에 그대로 남기지 않는다.
- 8교시 배움일기에는 그날 확인한 증거와 다음 수업 질문을 남긴다.
