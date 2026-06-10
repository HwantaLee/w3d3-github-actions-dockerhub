# Week 1 Day 4: 공통 샘플앱 실행, 성공/실패/오류 관찰, runbook 작성

## Day Goal
Day4는 새 앱을 만드는 개발 수업이 아니다. 학생은 제공된 공통 샘플앱을 실행하고, 정상 상태와 실패 상태를 관찰하며, 브라우저와 `curl`, 서버 로그, console/Network를 사용해 확인 기록을 남긴다. 목표는 IT를 처음 접하는 챌린저도 "서버를 실행한다", "성공을 확인한다", "실패를 구분한다", "문서로 남긴다"를 체험하는 것이다.

## 운영 원칙
- 공통 샘플앱은 `week1/day4/sample-app/`에 제공한다.
- 학생은 앱을 새로 만들지 않는다. 아주 작은 값 수정과 의도적 오류 관찰만 한다.
- backend, database, paid API, authentication, cloud deploy는 다루지 않는다.
- HTML/CSS/JS 문법 설명은 필요한 만큼만 하고, 수업의 중심은 실행 조건과 관찰 기록이다.
- 7~8교시는 새 진도 없이 최초 1:1 개인 면담과 기본 멘토링으로 운영한다.

## 오늘 반드시 가져갈 것
| 필수 개념 | 왜 필수인가 | 놓치면 생기는 문제 | 확인 기록 |
|---|---|---|---|
| 샘플앱 실행 조건 | 같은 앱을 모두가 같은 조건으로 실행해야 관찰을 비교할 수 있다. | 사람마다 다른 앱을 만들어 오류 원인을 비교하지 못한다. | 실행 경로, start command, URL |
| 성공 상태 확인 | 정상 기준을 먼저 알아야 실패를 구분할 수 있다. | 200, 화면 표시, 로그를 연결하지 못한다. | 브라우저 화면, `curl -I`, 서버 로그 |
| 실패/오류 관찰 | 404, 경로 오류, JSON 오류는 운영에서 흔한 첫 장애다. | 모든 실패를 "안 됨"으로만 표현한다. | 실패 URL, 상태 코드, console/Network |
| README/runbook | 다음 사람이 실행하고 막혔을 때 확인할 순서를 제공한다. | 수업 후 혼자 다시 따라오지 못한다. | start/check/stop/troubleshoot |
| 최초 1:1 면담 | IT 첫 경험자와 경험자의 출발점, 불안, 관심사가 다르므로 개인별 상태 확인이 필요하다. | 막힘을 기술 문제로만 보고 학습 지원 방향을 놓친다. | interview note, mentoring action |

## Lesson Index
| 교시 | 주제 | 핵심 산출물 |
|---|---|---|
| 1교시 | 공통 샘플앱 구조 읽기 | file role map |
| 2교시 | 샘플앱 로컬 서버 실행 | start/check log |
| 3교시 | 성공 상태 관찰 | success 확인 기록 table |
| 4교시 | 실패 1: 잘못된 URL과 404 | 404 observation note |
| 5교시 | 실패 2: data.json 경로/JSON 오류 | console/network error note |
| 6교시 | README/runbook 작성 | start/check/stop/troubleshoot |
| 7교시 | 최초 1:1 개인 면담 1 | interview note |
| 8교시 | 최초 1:1 개인 면담 2 및 기본 멘토링 | mentoring note, Day5 carry-over |

## Required Deliverables
| Deliverable | Minimum 확인 기록 |
|---|---|
| sample app run | command, working directory, URL |
| success check | browser result, `curl -I`, server log |
| 404 observation | failing URL, status code, meaning |
| data/JS error observation | console or Network note |
| runbook | start/check/stop/troubleshoot |
| interview/mentoring note | background, concern, blocker type, next action |

## 챌린저 복구 기준
- 서버가 안 켜지면 `python3 --version`, 현재 경로, 포트 8000 충돌을 먼저 본다.
- 브라우저가 안 열리면 서버 터미널이 살아 있는지와 URL이 `http://localhost:8000`인지 확인한다.
- 화면은 열리지만 데이터가 안 보이면 console과 Network에서 `data.json` 요청을 확인한다.
- 오류를 고치기 전에 실패 URL, 상태 코드, 오류 메시지를 먼저 적는다.
- Day4 끝에는 새 기능보다 실행 확인 기록, README, 위험 표, 면담 이월 메모를 먼저 닫는다.

## 다음 주차 연결
Day4 샘플앱은 Week2 Docker 실습의 공통 입력이 된다. Day4에서 확인한 실행 경로, start command, 포트, HTTP 확인, 오류 관찰 기록은 Week2에서 container command, port mapping, container logs, Docker runbook으로 확장된다.

## Visual Support
![로컬 서비스 확인 기록 흐름](../assets/week1-service-evidence-flow.png)

Day4에서는 이 확인 기록 흐름을 샘플앱에 적용한다. 구현 자체보다 command, port, status, log, console, README가 함께 남는지 확인한다.
