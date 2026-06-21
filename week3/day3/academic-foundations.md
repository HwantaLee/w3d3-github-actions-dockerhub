# Week 3 Day 3: Academic And Official Foundations

이 문서는 Day 3 수업 내용을 공식 문서와 현업 기준에 연결한다. 수업 중에는 링크 자체보다 어떤 판단 기준을 가져오는지가 중요하다.

## Official References
| Topic | Reference | 확인할 키워드 |
|---|---|---|
| GitHub Flow | https://docs.github.com/en/get-started/using-github/github-flow | branch, commit, PR, deploy |
| GitHub Actions | https://docs.github.com/en/actions | workflow, event, job, runner |
| GitHub protected branches | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches | status check, review |
| Kubernetes Concepts | https://kubernetes.io/docs/concepts/ | cluster, pod, deployment, service |
| kubectl Cheat Sheet | https://kubernetes.io/docs/reference/kubectl/quick-reference/ | get, describe, logs, exec |


## 수업 적용 기준
| 기준 | 수업에서의 사용 |
|---|---|
| Evidence first | 명령을 실행한 뒤 상태, 로그, 이벤트, PR check 결과를 근거로 판단한다. |
| Small reversible change | branch, PR, rollout 모두 작고 되돌릴 수 있는 단위로 다룬다. |
| Shared contract | GitHub 규칙, CI gate, Kubernetes manifest는 팀이 공유하는 운영 계약이다. |
| Failure readable | 실패는 숨길 대상이 아니라 다음 행동을 결정하는 신호다. |
