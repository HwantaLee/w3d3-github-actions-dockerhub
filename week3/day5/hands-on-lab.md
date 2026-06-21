# Week 3 Day 5 Hands-on Lab: Pod, Deployment, Service

## Phase 0. Cluster 확인
```bash
kubectl config current-context
kubectl get nodes
```

## Phase 1. Namespace와 첫 Pod
```bash
kubectl apply -f week3/day4/labs/k8s-first-pod/namespace.yaml
kubectl apply -f week3/day4/labs/k8s-first-pod/hello-pod.yaml
kubectl -n paperclip get pods -o wide
kubectl -n paperclip logs hello-pod
kubectl -n paperclip describe pod hello-pod
```

## Phase 2. Pod 장애 확인
```bash
kubectl apply -f week3/day4/labs/k8s-first-pod/bad-image-pod.yaml
kubectl -n paperclip get pods
kubectl -n paperclip describe pod bad-image-pod
```

확인할 event: `ErrImagePull`, `ImagePullBackOff`.

## Phase 3. Deployment와 Service
```bash
kubectl apply -f week3/day5/labs/k8s-deployment-service/namespace.yaml
kubectl apply -f week3/day5/labs/k8s-deployment-service/deployment.yaml
kubectl apply -f week3/day5/labs/k8s-deployment-service/service.yaml
kubectl -n paperclip get deploy,pod,svc,endpoints
```

## Phase 4. 내부 통신
```bash
kubectl -n paperclip run curlbox --rm -it --image=curlimages/curl --restart=Never -- \
  curl -s http://hello-service
```

## Phase 5. Rollout 맛보기
```bash
kubectl -n paperclip rollout status deployment/hello-web
kubectl -n paperclip rollout history deployment/hello-web
kubectl -n paperclip set image deployment/hello-web hello-web=nginx:1.27-alpine
kubectl -n paperclip rollout status deployment/hello-web
kubectl -n paperclip rollout undo deployment/hello-web
```

## Cleanup
```bash
kubectl delete namespace paperclip
```
