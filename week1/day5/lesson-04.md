# 4교시: 샘플앱 운영 기록 보완

## 수업 목표
- Day4 샘플앱의 성공, 404, data/JSON 오류 관찰 기록을 보완한다.
- 새 기능 추가보다 실행 확인 기록과 runbook 완성을 우선한다.
- Week2 Docker preview의 입력이 될 실행 조건을 정리한다.

## 오늘 반드시 가져갈 것
| 필수 개념 | 왜 필수인가 | 놓치면 생기는 문제 | 확인 기록 |
|---|---|---|---|
| 운영 기록 보완 | 성공/실패/오류 관찰이 모두 있어야 Day4 실습이 완성된다. | 정상 실행만 있고 실패 대응이 없다. | success/404/error notes |
| Fresh run | 서버를 새로 시작해 현재 상태를 다시 확인한다. | 예전 성공 기록만 믿고 제출한다. | fresh run command/status |
| Runbook 일치 | README의 절차가 실제 실행과 맞아야 한다. | 문서대로 따라 하면 실패한다. | start/check/stop 검증 |
| Docker 입력 | Week2는 이 실행 조건을 container로 옮기는 데서 시작한다. | Docker 문제가 아니라 기존 실행 조건 누락으로 막힌다. | readiness note |

### 챌린저 복구 기준
- 기능을 더 만들지 않는다. 성공, 404, data/JSON 오류 기록 중 빈칸을 먼저 채운다.
- fresh run은 새 터미널에서 서버를 다시 시작하는 기준으로 확인한다.
- runbook을 고치면 같은 명령으로 다시 확인한다.

## 50분 운영
| 시간 | 활동 | 학습 초점 | 학생 산출 |
|---|---|---|---|
| 0-5분 | 보완 기준 확인 | 새 기능 금지와 확인 기록 우선 원칙을 확인한다. | 기준 확인 |
| 5-20분 | Day4 기록 gap 보완 | 성공/404/data error 중 빈칸을 채운다. | completed notes |
| 20-30분 | fresh run | 서버 재시작 후 URL과 status를 확인한다. | fresh run note |
| 30-40분 | README/runbook 보완 | 문서와 실제 실행을 맞춘다. | final runbook |
| 40-50분 | Docker readiness 연결 | Week2로 넘길 실행 조건을 적는다. | readiness note |

## 0-5분 보완 기준 확인
Day4의 목표는 샘플앱을 새로 만드는 것이 아니라 공통 샘플앱을 운영 관점으로 다뤄보는 것이다. Day5 4교시에는 새 기능을 추가하지 않고 관찰 기록과 runbook을 닫는다.

## 5-20분 Day4 기록 gap 보완
| 기록 항목 | complete/partial/missing | 보완 행동 |
|---|---|---|
| 성공 상태: browser, `curl -I`, server log | | |
| 404 상태: wrong URL, status, server log | | |
| data/JSON 오류: console 또는 Network | | |
| runbook: start/check/stop/troubleshoot | | |
| risk: cost/security/reproducibility/handoff | | |

## 20-30분 fresh run
```bash
cd week1/day4/sample-app
python3 -m http.server 8000
```

새 터미널:
```bash
curl -I http://localhost:8000
curl -I http://localhost:8000/data.json
```

브라우저에서 정상 메시지를 확인한다.

## 30-40분 README/runbook 보완
| README/runbook 항목 | 실제 값 |
|---|---|
| Start command | |
| Check command | |
| Browser URL | |
| Stop instruction | |
| 404 troubleshoot | |
| data/JSON troubleshoot | |

## 40-50분 Docker readiness 연결
| Week2로 넘길 항목 | Day4 샘플앱 값 |
|---|---|
| build context 후보 | `week1/day4/sample-app` |
| 실행 명령 | `python3 -m http.server 8000` |
| 포트 | 8000 |
| 확인 명령 | `curl -I http://localhost:8000` |
| 필요한 파일 | `index.html`, `style.css`, `app.js`, `data.json` |
| 남은 위험 | |

## 다음 연결
다음 교시는 평가 체크리스트와 2~5주차 기술 매핑을 정리한다. Day4 샘플앱 기록은 Week2 Docker readiness의 기준이 된다.
