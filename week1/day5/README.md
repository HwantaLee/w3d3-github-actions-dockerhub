# Week 1 Day 5: 산출물 통합, 샘플앱 운영 기록, Day3 챌린지 발표, Docker preview

## Day Goal
학생은 Week1 산출물을 하나의 handoff package로 통합하고, Day3 AI 웹사이트 챌린지 결과와 Day4 샘플앱 운영 기록을 발표 가능한 형태로 정리한다. 발표와 Q&A를 통해 문서의 모호함을 보완하고, Week2 Docker가 어떤 실행 문제를 해결하는지 preview한다.

## 운영 원칙
- Day5는 새 기능 확장보다 통합, 증거, handoff, 발표를 우선한다.
- Day4 샘플앱 실습의 성공/실패/오류 관찰 범위를 유지한다.
- backend, database, paid API, authentication은 여전히 제외한다.
- Docker는 preview로만 다루며 Week2 본수업을 대체하지 않는다.
- DORA와 Well-Architected는 Week1 독립 수업으로 다루지 않는다.

## Lesson Index
| 교시 | 주제 | 핵심 산출물 |
|---|---|---|
| 1교시 | 1주차 산출물 통합 | integration inventory, 확인 기록 gap list |
| 2교시 | 컴퓨팅 spine 최종 매핑 | final spine map |
| 3교시 | 현업 DevOps handoff | handoff package |
| 4교시 | 샘플앱 운영 기록 보완 | success/failure/error notes, final README |
| 5교시 | 통합 체크리스트, 평가 기준, 2~5주차 기술 매핑 | evaluation checklist, residual risk |
| 6교시 | Day3 AI 챌린지와 Day4 운영 기록 발표 | presentation card, peer feedback |
| 7교시 | 발표 피드백 및 live Q&A | Q&A notes, patched package |
| 8교시 | 2주차 Docker preview | Docker readiness note |

## Required Deliverables
| Deliverable | Minimum 확인 기록 |
|---|---|
| final repository and README | start/check/stop/troubleshoot |
| computing spine mapping note | file/process/port/data/확인 기록 map |
| handoff package | summary, run, verify, risks, gaps, next step |
| Day4 sample app operation note | success, 404, data/JSON error, runbook |
| Day3 AI website challenge | prompt, static site files, run 확인 기록, risk removal note |
| evaluation 확인 기록 | checklist with complete/partial/missing |
| presentation card | 3-minute 확인 기록-centered structure |
| Docker readiness note | build context, port, files, risks, Week2 question |

## 최종 평가 관점
- 다른 사람이 README만 보고 앱을 실행할 수 있는가?
- 정상 상태를 HTTP/browser 확인 기록으로 확인할 수 있는가?
- 데이터, 위험, 실패 기록, handoff가 문서화되어 있는가?
- spine mapping이 실제 path/command/URL과 연결되는가?
- Week2 Docker가 해결할 문제가 명확한가?

## 다음 주차 연결
Week2는 Day5 Docker readiness note에서 시작한다. 학생은 Day4 샘플앱 폴더를 Docker build context로 사용하고, container 실행, port mapping, curl 확인 기록, container runbook을 작성한다.

## Visual Support
![Week 1 to Docker preview mapping](../assets/week1-docker-preview-mapping.png)

이 이미지는 Week1에서 만든 로컬 실행 증거가 Week2 Docker의 image, container, port mapping, volume, environment variable, logs로 확장되는 흐름을 보여준다. Week1에서는 preview로만 사용하고 Docker hands-on 실행은 Week2에서 진행한다.
