# 8교시: 구름 EXP 배움일기

## 수업 목표
- kind 설치, Pod/Deployment/Service 역할, Week4 Kubernetes 질문를 Kubernetes 실행 증거로 확인한다.
- manifest와 실제 cluster 상태를 비교한다.
- 실패 상태를 describe/events/logs로 읽는다.

## 핵심 설명
오늘의 Pod/Deployment/Service evidence와 Week4 질문을 정리한다.

## 실습 기준
```bash
# 자세한 명령은 week3/day5/hands-on-lab.md 참고
kubectl config current-context
kubectl get nodes
```

## 확인 명령
| 명령 | 보는 것 |
|---|---|
| `kubectl get` | 현재 resource 목록과 상태 |
| `kubectl describe` | event, selector, image, scheduling 이유 |
| `kubectl logs` | container stdout/stderr |
| `kubectl rollout` | Deployment 배포 상태와 되돌리기 |


## 구름 EXP 배움일기
- kind cluster 확인 결과
- Pod와 Deployment 차이
- Service가 필요한 이유
- Week4에서 더 보고 싶은 Kubernetes 장애


## Evidence Note
```markdown
# Evidence
- command:
- observed output:
- normal or failure:
- next action:
```
