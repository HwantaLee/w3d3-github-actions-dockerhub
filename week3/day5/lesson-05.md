# 5교시: Deployment manifest 구조와 배포

## 수업 목표
- apiVersion, kind, metadata, spec, selector, template를 Kubernetes 실행 증거로 확인한다.
- manifest와 실제 cluster 상태를 비교한다.
- 실패 상태를 describe/events/logs로 읽는다.

## 핵심 설명
manifest의 selector와 template label이 맞아야 Deployment가 Pod를 관리한다.

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



## Evidence Note
```markdown
# Evidence
- command:
- observed output:
- normal or failure:
- next action:
```
