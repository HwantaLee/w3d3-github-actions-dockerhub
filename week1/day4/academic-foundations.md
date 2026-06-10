# Week 1 Day 4 학술 근거와 교육 설계 기준

## 교육 설계 의도
Day4는 작은 정적 앱을 새로 만드는 개발 수업이 아니다. 공통 샘플앱을 실행하고, 성공 상태와 실패 상태를 관찰하며, 확인 기록과 runbook을 남기는 운영 입문 수업이다. 7~8교시는 최초 1:1 개인 면담과 기본 멘토링으로 운영해 학생별 출발점, 환경 상태, 불안 요소, 다음 행동을 확인한다.

## Crosswalk
| Standard / Theory | Observable Action | 확인 기록 |
|---|---|---|
| ABET-style problem analysis | 제공된 샘플앱의 성공/실패 조건을 관찰한다. | success/failure note |
| ABET-style professional responsibility | 비용/보안/재현성 위험을 분류한다. | risk table |
| CS2023 software practice | UI, script, data file 책임을 읽고 실행 조건을 정리한다. | file role map |
| CS2023 systems perspective | file, process, port, HTTP 확인 기록을 연결한다. | execution record |
| NIST NICE-style task | secret/API/resource 위험을 피한다. | exclusion note |
| Bloom analyze/evaluate | 실행 결과와 오류를 관찰하고 운영 기준으로 평가한다. | README/runbook |
| Cognitive load theory | 새 앱 제작 변수를 제외해 챌린저 부담을 낮춘다. | scope rule |
| Mastery learning | 7~8교시에서 개인 출발점과 다음 행동을 확인한다. | interview/mentoring note |

## 평가 설계
| 평가 영역 | 관찰 가능한 증거 |
|---|---|
| 범위 통제 | include/exclude table, excluded feature reasons |
| 실행 | sample app, JSON rendering, one user flow |
| 실행 검증 | command, path, port, URL, browser/curl result |
| 운영 사고 | risk classification, troubleshoot runbook |
| 면담과 멘토링 | 학습 배경, 환경 상태, blocker type, next action |

## 필수 면담 블록
4일차 7~8교시는 새 진도 없이 최초 1:1 개인 면담과 기본 멘토링으로 운영한다. 면담은 환경, 학습 배경, 관심사, 불안 요소, 자신감 blocker를 확인하고 다음 행동을 정하는 형식이어야 한다. 샘플앱 진행 상태는 학생을 평가하는 자료가 아니라 멘토링 방향을 잡기 위한 입력이다.

## 현업 DevOps 연결
Day4에서 다루는 현업 관점은 독립 프레임워크 수업이 아니라 다음 습관으로 제한한다.
- 실행 조건을 문서화한다.
- 실패 상태를 숨기지 않는다.
- 위험을 비용, 보안, 재현성으로 분류한다.
- handoff 가능한 README/runbook을 만든다.

Week1에는 DORA와 Well-Architected를 독립 수업으로 배치하지 않는다.
