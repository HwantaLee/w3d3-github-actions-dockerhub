# Week 3 Day2: 장애 전파와 MSA 운영 증거

## Overview
Day 2는 Day 1의 실행 성공에서 끝나지 않고 부분 장애, readiness, timeout/retry, worker/queue, correlation id, 운영 리포트까지 압축한다.

## Learning Goals
- API 장애, DB 장애, worker 장애가 사용자 경험에 어떻게 다르게 보이는지 설명한다.
- `/health`와 readiness, `depends_on`의 한계, 재시도 필요성을 구분한다.
- timeout/retry가 장애를 줄이기도 하고 중복 처리 위험을 만들기도 함을 설명한다.
- 여러 서비스 로그를 request id/correlation id로 이어 본다.
- MSA 운영 리포트를 표 형태로 작성하고 Kubernetes 필요성으로 연결한다.

## Lesson Index
| 교시 | 주제 | 핵심 확인 |
|---|---|---|
| 1교시 | Day1 10분 요약 + 장애 전파와 부분 장애 | api/db/worker 장애가 사용자 경험에 미치는 영향 |
| 2교시 | health check와 readiness | `/health`, DB readiness, `depends_on`의 한계 |
| 3교시 | timeout과 retry | 무한 대기 방지, 재시도의 위험, 중복 처리 문제 |
| 4교시 | queue/worker 운영 시나리오 | 작업 적체, worker 중지, 재처리 로그, 비동기 장애 확인 |
| 5교시 | 로그 분산과 correlation id | 여러 서비스 로그를 이어서 보는 방법 |
| 6교시 | 배포 설정 변경 | image tag, env, replica, port 변경이 장애로 이어지는 사례 |
| 7교시 | MSA 운영 리포트 작성 | 증상, 영향 범위, 원인 후보, 복구, 예방, 전달사항 |
| 8교시 | 구름 EXP 배움일기 | 장애 전파, health, timeout/retry, Kubernetes 필요성 |

## Practice Files
| 자료 | 용도 |
|---|---|
| `hands-on-lab.md` | 당일 실습 명령과 확인 순서 |
| `academic-foundations.md` | 공식/현업 기준 mapping |
| `assets/` | 보조 시각 자료 |
| `labs/` | 실행 가능한 실습 파일 |

## Evidence Policy
| Evidence | 제출 기준 |
|---|---|
| command evidence | 명령과 핵심 출력 요약 |
| failure note | 증상, 첫 확인 명령, 원인 후보, 복구 기준 |
| handoff note | 다음 운영자 또는 다음 주제로 넘길 정보 |
| goorm EXP note | 8교시 배움일기 항목 |

## Official References
| Topic | Reference |
|---|---|
| Google SRE Cascading Failures | https://sre.google/sre-book/addressing-cascading-failures/ |
| Docker Compose healthcheck | https://docs.docker.com/reference/compose-file/services/#healthcheck |
| OpenTelemetry Concepts | https://opentelemetry.io/docs/concepts/ |

## End-Of-Day Checklist
- [ ] 오늘의 핵심 흐름을 한 문장으로 설명했다.
- [ ] 명령 실행 결과를 evidence로 남겼다.
- [ ] 실패 로그 또는 이벤트를 하나 이상 읽었다.
- [ ] 다음 교시 또는 Week 4로 넘길 질문을 적었다.
