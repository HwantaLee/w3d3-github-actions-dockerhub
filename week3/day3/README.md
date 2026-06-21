# Week 3 Day3: GitHub 협업 압축과 CI Gate

## Overview
Day 3는 GitHub를 하루에 압축한다. branch, PR, merge, rebase, revert, tag, Actions CI gate가 배포 사고를 줄이는 흐름을 하나로 묶는다.

## Learning Goals
- GitHub Flow를 branch/commit/push/PR/review/merge 흐름으로 설명한다.
- merge/rebase/revert/tag를 배포 사고 예방 도구로 해석한다.
- Actions workflow, event, job, step, runner, secret 위치를 설명한다.
- PR check 실패 로그를 읽고 merge 차단 이유를 evidence로 남긴다.

## Lesson Index
| 교시 | 주제 | 핵심 확인 |
|---|---|---|
| 1교시 | Day2 10분 요약 + GitHub 협업 모델 | local branch, remote branch, origin, pull request 흐름 |
| 2교시 | branch 전략 압축 | GitHub Flow 중심, trunk-based/Git Flow 선택 기준 비교 |
| 3교시 | PR 운영 기준 | 작은 PR, reviewer, status check, protected branch, merge 조건 |
| 4교시 | merge/rebase/conflict | merge commit, squash, rebase merge 차이와 conflict 재검증 |
| 5교시 | revert와 rollback | `git revert`, PR revert, 배포 rollback 차이 |
| 6교시 | tag와 version 기준 | app version, Git tag, Docker image tag, latest 사용 주의 |
| 7교시 | GitHub Actions CI gate | `pull_request`, checkout, lint/test/build, runner, secret 맛보기 |
| 8교시 | 구름 EXP 배움일기 | branch 전략, PR gate, merge/rebase/revert/tag, CI 실패 증거 |

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
| GitHub Flow | https://docs.github.com/en/get-started/using-github/github-flow |
| GitHub Actions | https://docs.github.com/en/actions |
| Protected branches | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches |

## End-Of-Day Checklist
- [ ] 오늘의 핵심 흐름을 한 문장으로 설명했다.
- [ ] 명령 실행 결과를 evidence로 남겼다.
- [ ] 실패 로그 또는 이벤트를 하나 이상 읽었다.
- [ ] 다음 교시 또는 Week 4로 넘길 질문을 적었다.
