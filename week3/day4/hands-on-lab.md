# Week 3 Day 4 Hands-on Lab: kind 설치와 cluster 확인

## Phase 1. 공통 확인
```bash
docker version
docker compose version
kubectl version --client=true
kind version
```

## WSL 설치 기준
```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

`kubectl`은 OS/패키지 매니저 상태에 따라 공식 문서를 기준으로 설치한다.

## macOS 설치 기준
```bash
brew install kubectl kind
kubectl version --client=true
kind version
```

## Phase 2. Cluster 생성
```bash
kind create cluster --name paperclip-week3
kubectl config current-context
kubectl cluster-info
kubectl get nodes -o wide
```

## Phase 3. 종료 기준
```bash
kind delete cluster --name paperclip-week3
```

Day 5 실습을 바로 이어갈 경우 cluster를 삭제하지 않는다.
