# 6교시: README/runbook 작성 - start, check, stop, troubleshoot

## 수업 목표
- 샘플앱의 실행 절차를 README/runbook 형태로 정리한다.
- 성공 확인과 실패 대응을 분리해 적는다.
- 비용, 보안, 재현성, handoff 위험을 짧게 분류한다.

## 오늘 반드시 가져갈 것
| 필수 개념 | 왜 필수인가 | 놓치면 생기는 문제 | 확인 기록 |
|---|---|---|---|
| README | 다음 사람이 앱의 목적과 실행 방법을 읽는다. | 실행 조건이 사람 기억에만 남는다. | README section |
| Runbook | 문제가 생겼을 때 확인 순서를 제공한다. | 실패 때마다 처음부터 추측한다. | troubleshoot table |
| 위험 분류 | 비용, 보안, 재현성, handoff 위험을 분리한다. | 막연한 불안이 행동으로 바뀌지 않는다. | risk table |
| 비밀값 비노출 | 샘플앱은 token/password/key를 쓰지 않는다. | 불필요한 secret이 문서나 코드에 남는다. | secret 없음 note |

### 챌린저 복구 기준
- README에는 정상 실행 방법을, runbook에는 실패 시 확인 순서를 적는다.
- 오류 메시지를 모두 외우지 말고 증상별 첫 확인 위치를 적는다.
- Day4 문서는 길게 잘 쓰는 것보다 다시 따라 할 수 있게 쓰는 것이 우선이다.

## 50분 운영
| 시간 | 활동 | 학습 초점 | 학생 산출 |
|---|---|---|---|
| 0-10분 | README와 runbook 구분 | 목적과 절차를 나눈다. | doc map |
| 10-25분 | start/check/stop 작성 | 정상 실행 절차를 고정한다. | README draft |
| 25-35분 | troubleshoot 작성 | 실패 증상별 첫 확인을 적는다. | runbook table |
| 35-45분 | 위험 분류 | cost/security/reproducibility/handoff를 본다. | risk table |
| 45-50분 | 제출 전 점검 | 누락을 표시한다. | gap list |

## README 최소 구조
```md
# Sample App Runbook

## Start
python3 -m http.server 8000

## Check
curl -I http://localhost:8000
브라우저에서 http://localhost:8000 확인

## Stop
서버 터미널에서 Ctrl+C

## Troubleshoot
증상별 확인 순서 작성
```

## Troubleshoot 표
| 증상 | 먼저 볼 곳 | 첫 행동 |
|---|---|---|
| connection refused | 서버 터미널 | 서버가 켜져 있는지 확인 |
| 404 | URL 경로, 파일명 | 요청 경로와 실제 파일 비교 |
| 데이터가 안 보임 | Console, Network | `data.json` 요청 상태 확인 |
| JSON 오류 | Console, `data.json` | 쉼표, 따옴표, 중괄호 확인 |

## 위험 분류
| 위험 | Day4 샘플앱 기준 |
|---|---|
| Cost | 로컬 실행만 하므로 비용 없음 |
| Security | secret/token/password 없음 |
| Reproducibility | README대로 실행 가능한지 확인 필요 |
| Handoff | 다음 사람이 오류 대응 순서를 읽을 수 있어야 함 |

## 제출 전 점검
| 항목 | 상태 |
|---|---|
| Start command | |
| Browser check | |
| `curl -I` check | |
| 404 observation | |
| data/JSON error observation | |
| Troubleshoot table | |
| Risk table | |

## 다음 연결
다음 7~8교시는 개인별 막힘을 복구하고 Day4 운영 기록을 제출 가능한 상태로 닫는다.
