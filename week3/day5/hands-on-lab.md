# Week 3 Day 5 Hands-on Lab: Deployment, Service, Rollout 맛보기

## 공통 준비
Day 4에서 만든 kind cluster가 살아 있으면 그대로 사용한다. 없으면 다시 만든다.

```bash
kind get clusters
kind get clusters | grep -qx week3-k8s || kind create cluster --name week3-k8s
kubectl config current-context
kubectl apply -f week3/day5/labs/k8s-deployment-service/namespace.yaml
kubectl get serviceaccount default -n week3
```

이미 `week3-k8s`가 있으면 새로 만들지 않는다. context가 다르면 다음 명령으로 바꾼다.

```bash
kubectl config use-context kind-week3-k8s
kubectl get nodes -o wide
```

WSL에서 Docker credential helper 오류가 나면 Day 4의 임시 `DOCKER_CONFIG` 우회 후 다시 실행한다.

## 첫 Pod 실행과 상태 확인
Deployment로 넘어가기 전 Pod 하나를 직접 실행해 Pod가 어떤 최소 실행 단위인지 확인한다.

```bash
kubectl apply -f week3/day4/labs/k8s-first-pod/hello-pod.yaml
kubectl get pod hello-pod -n week3 -o wide
kubectl describe pod hello-pod -n week3
kubectl logs hello-pod -n week3
```

## Pod 실패 확인
이미지를 잘못 지정한 Pod를 만들어 `ImagePullBackOff` 계열의 실패를 읽는다.

```bash
kubectl apply -f week3/day4/labs/k8s-first-pod/bad-image-pod.yaml
kubectl get pod bad-image -n week3
kubectl describe pod bad-image -n week3
kubectl delete pod bad-image -n week3
```

## Deployment 생성
```bash
kubectl apply -f week3/day5/labs/k8s-deployment-service/deployment.yaml
kubectl get deploy,pod -n week3 -o wide
kubectl describe deployment api-demo -n week3
```

Pod를 직접 만들 때와 달리 Deployment는 원하는 replica 수를 계속 맞추려고 한다.

```bash
kubectl delete pod -n week3 -l app=api-demo
kubectl get pod -n week3 -w
```

새 Pod가 다시 생기는 것을 확인하면 `Ctrl+C`로 watch를 종료한다.

## Service 생성과 내부 통신
```bash
kubectl apply -f week3/day5/labs/k8s-deployment-service/service.yaml
kubectl get svc,endpoints -n week3
kubectl run curlbox --image=curlimages/curl:8.10.1 -n week3 --restart=Never -- sleep 3600
kubectl exec -n week3 curlbox -- curl -s http://api-demo
```

## Rollout 맛보기
```bash
kubectl set image deployment/api-demo nginx=nginx:1.26 -n week3
kubectl rollout status deployment/api-demo -n week3
kubectl rollout history deployment/api-demo -n week3
kubectl rollout undo deployment/api-demo -n week3
kubectl rollout status deployment/api-demo -n week3
```

## Cleanup
```bash
kubectl delete namespace week3
kind delete cluster --name week3-k8s
```

## 제출 Evidence
```markdown
# Day 5 Kubernetes Evidence

## Deployment
- Replicas:
- Pods:
- Self-healing observation:

## Service
- Service name:
- Endpoint:
- Internal curl result:

## Rollout
- Image before:
- Image after:
- Undo result:
- Week4 question:
```
