# Week 3 Day 4: Academic And Official Foundations

이 문서는 Day 4 수업 내용을 공식 문서와 현업 기준에 연결한다. 수업 중에는 링크 자체보다 어떤 판단 기준을 가져오는지가 중요하다.

## Official References
| Topic | Reference | 확인할 키워드 |
|---|---|---|
| Kubernetes Concepts | https://kubernetes.io/docs/concepts/ | cluster, node, control plane, workload |
| Kubernetes Components | https://kubernetes.io/docs/concepts/overview/components/ | kube-apiserver, kubelet, container runtime |
| kubectl Cheat Sheet | https://kubernetes.io/docs/reference/kubectl/quick-reference/ | get, describe, logs, exec |
| kind Quick Start | https://kind.sigs.k8s.io/docs/user/quick-start/ | Docker, create cluster, node |
| k3s Docs | https://docs.k3s.io/ | lightweight Kubernetes, edge, server |


## 수업 적용 기준
| 기준 | 수업에서의 사용 |
|---|---|
| Evidence first | 명령을 실행한 뒤 상태, 로그, 이벤트, PR check 결과를 근거로 판단한다. |
| Small reversible change | cluster, namespace, manifest를 작고 되돌릴 수 있는 단위로 다룬다. |
| Shared contract | Kubernetes manifest와 kubectl evidence는 팀이 공유하는 운영 계약이다. |
| Failure readable | 실패는 숨길 대상이 아니라 다음 행동을 결정하는 신호다. |
