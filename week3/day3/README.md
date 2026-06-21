# Week 3 Day 3: GitHub 협업 압축과 CI Gate

## Overview
Day 3는 GitHub를 하루에 압축한다. 목표는 모든 기능을 얕게 나열하는 것이 아니라 branch, PR, merge, rebase, revert, tag, Actions CI gate가 배포 사고를 줄이는 흐름을 하나로 이해하는 것이다.

## Learning Goals
- GitHub Flow 중심의 branch, commit, push, pull request, review, merge 흐름을 설명한다.
- merge, rebase, revert, tag를 이력 관리가 아니라 배포 사고 예방 도구로 해석한다.
- GitHub Actions CI gate의 workflow, event, job, step, runner, secret 위치를 설명한다.
- PR check 실패 로그를 읽고 merge 차단 이유를 evidence로 남긴다.
- 실패 증상을 숨기지 않고 재현 조건, 관찰 결과, 수정 또는 요청사항으로 기록한다.
- Week 4 Kubernetes 확장 수업으로 넘길 질문을 남긴다.

## Lesson Index
| 교시 | 주제 | 핵심 산출물 |
|---|---|---|
| 1교시 | GitHub 협업 모델 | local branch, remote branch, origin, pull request 흐름 evidence |
| 2교시 | branch 전략 압축 | GitHub Flow 중심, trunk-based/Git Flow 선택 기준 evidence |
| 3교시 | PR 운영 기준 | 작은 PR, reviewer, status check, protected branch evidence |
| 4교시 | merge/rebase/conflict | merge commit, squash, rebase merge 차이와 conflict 재검증 evidence |
| 5교시 | revert와 rollback | git revert, PR revert, 배포 rollback 차이 evidence |
| 6교시 | tag와 version 기준 | app version, Git tag, Docker image tag, latest 사용 기준 evidence |
| 7교시 | GitHub Actions CI gate | pull_request event, checkout, lint/test/build, runner, secret evidence |
| 8교시 | 구름 EXP 배움일기 | branch 전략, PR gate, merge/rebase/revert/tag, CI 실패 증거 정리 |

## Practice Files And Assets
| 자료 | 용도 |
|---|---|
| `hands-on-lab.md` | 오늘 실습 흐름 실행 가이드 |
| `academic-foundations.md` | 공식/현업 기준 mapping |
| `assets/` | 이전 버전 보조 이미지 보관 위치. 새 수업에서는 필요할 때 선별 사용 |

## Session Visual Index
| 교시 | 주제 | 시각 자료 기준 |
|---|---|---|
| 1교시 | GitHub 협업 모델 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 2교시 | branch 전략 압축 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 3교시 | PR 운영 기준 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 4교시 | merge/rebase/conflict | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 5교시 | revert와 rollback | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 6교시 | tag와 version 기준 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 7교시 | GitHub Actions CI gate | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 8교시 | 구름 EXP 배움일기 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |

## Today Evidence
| Evidence | 제출 기준 |
|---|---|
| command evidence | 실행/확인/로그/정리 명령 |
| failure note | 장애 재현, 관찰, 복구, 예방 |
| handoff note | 다음 운영자 또는 Week 4로 넘길 정보 |

## Official References
| Topic | Reference | 확인할 키워드 |
|---|---|---|
| GitHub Flow | https://docs.github.com/en/get-started/using-github/github-flow | branch, commit, PR, deploy |
| GitHub Actions | https://docs.github.com/en/actions | workflow, event, job, runner |
| GitHub protected branches | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches | status check, review |
| Kubernetes Concepts | https://kubernetes.io/docs/concepts/ | cluster, pod, deployment, service |
| kubectl Cheat Sheet | https://kubernetes.io/docs/reference/kubectl/quick-reference/ | get, describe, logs, exec |


## End-Of-Day Checklist
- [ ] 오늘의 핵심 흐름을 한 문장으로 설명했다.
- [ ] 명령 실행 결과를 evidence로 남겼다.
- [ ] 실패 로그 또는 이벤트를 하나 이상 읽었다.
- [ ] Week 4에서 더 깊게 다룰 질문을 적었다.
