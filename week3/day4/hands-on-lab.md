# Week 3 Day 4 Hands-on Lab: Kubernetes 컨셉과 kind 설치

## 목표
Day 4의 목표는 샘플앱 배포가 아니라 Kubernetes를 이해할 준비를 끝내는 것이다. WSL 또는 macOS에서 Docker, kubectl, kind를 준비하고, 로컬 kind cluster가 정상 생성되는지 확인한다. Pod와 샘플앱 실행은 Day 5에서 이어간다.

## 도구 선택 기준
| 도구 | 수업에서의 위치 | 선택 이유 |
|---|---|---|
| kind | Week3/Week4 기본 실습 도구 | Docker 위에 Kubernetes node를 컨테이너로 띄우므로 설치/삭제/재생성이 빠르다. |
| k3s | 비교 설명 및 후반 참고 | 경량 Kubernetes 배포판으로 edge, 온프레미스, 소형 서버 운영 사례를 설명할 때 좋다. |

이번 수업은 `kind`를 사용한다. `k3s`는 Kubernetes 운영 배포판의 예시로 소개만 하고, 설치 실습은 하지 않는다.

## WSL 설치 경로
WSL에서는 Docker Desktop의 WSL integration 또는 Linux Docker Engine이 먼저 정상 동작해야 한다.

```bash
docker version
docker compose version
```

`docker-credential-desktop.exe` 오류가 나면 Docker config가 Windows credential helper를 가리키고 있는데 WSL PATH에서 helper를 찾지 못하는 상태다. 수업 중 임시 우회는 아래처럼 한다.

```bash
mkdir -p /tmp/week3-docker-config
printf '{"auths":{}}\n' > /tmp/week3-docker-config/config.json
export DOCKER_CONFIG=/tmp/week3-docker-config
docker pull nginx:1.27
```

kubectl과 kind는 아래처럼 설치한다. 이미 설치되어 있으면 version 확인만 한다.

```bash
curl -Lo kubectl "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/kubectl

KIND_VERSION=v0.32.0
curl -Lo kind "https://kind.sigs.k8s.io/dl/${KIND_VERSION}/kind-linux-amd64"
chmod +x kind
sudo mv kind /usr/local/bin/kind
```

## macOS 설치 경로
macOS에서는 Docker Desktop을 먼저 실행한 뒤 Homebrew로 kubectl과 kind를 설치하는 경로가 가장 단순하다.

```bash
docker version
brew install kubectl kind
kubectl version --client
kind version
```

Apple Silicon과 Intel Mac 모두 Homebrew 경로가 다를 수 있으므로 `which kubectl`, `which kind`로 실제 실행 파일 위치를 확인한다.

## 공통 버전 확인
WSL/macOS 모두 설치 후 아래 결과를 evidence로 남긴다.

```bash
docker version
kubectl version --client
kind version
kubectl config current-context
```

`kubectl config current-context`가 아직 없다고 나와도 cluster를 만들기 전이면 정상이다.

## kind cluster 생성
```bash
kind create cluster --name week3-k8s
kubectl cluster-info --context kind-week3-k8s
kubectl get nodes -o wide
```

## context와 node 확인
```bash
kubectl config current-context
kubectl config get-contexts
kubectl get nodes
kubectl describe node week3-k8s-control-plane
```

`kubectl describe node` 출력에서는 `Roles`, `Conditions`, `Addresses`, `Capacity`, `Allocatable`을 훑어본다. 숫자를 외우는 것이 아니라 node가 어떤 상태 정보를 제공하는지 보는 것이 목적이다.

## 흔한 설치/실행 문제
| 증상 | 주로 발생하는 환경 | 확인할 것 | 복구 방향 |
|---|---|---|---|
| `Cannot connect to the Docker daemon` | WSL/macOS | Docker Desktop 실행 여부, WSL integration | Docker Desktop 실행 후 WSL 재시작 |
| `docker-credential-desktop.exe not found` | WSL | `~/.docker/config.json` credential helper | 임시 `DOCKER_CONFIG` 또는 config 수정 |
| `kind: command not found` | WSL/macOS | 설치 위치, PATH | `/usr/local/bin` 또는 Homebrew PATH 확인 |
| `kubectl config current-context` 실패 | 공통 | cluster 생성 전인지 확인 | `kind create cluster` 후 재확인 |
| node image pull 실패 | 공통 | Docker network, proxy, credential | Docker pull 가능 여부 먼저 확인 |

## namespace와 첫 Pod
아래는 Day 5에서 본격적으로 진행한다. Day 4 시간이 남으면 설치 확인용으로만 실행한다.

```bash
kubectl apply -f week3/day4/labs/k8s-first-pod/namespace.yaml
kubectl get serviceaccount default -n week3
kubectl apply -f week3/day4/labs/k8s-first-pod/hello-pod.yaml
kubectl get pod -n week3 -o wide
kubectl describe pod hello-pod -n week3
kubectl logs hello-pod -n week3
```

namespace를 만든 직후 `serviceaccount "default" not found`가 나오면 namespace 내부 기본 리소스가 아직 준비되기 전이다. 몇 초 뒤 `kubectl get serviceaccount default -n week3`가 보이면 다시 apply한다.

## 실패 상태 관찰
```bash
kubectl apply -f week3/day4/labs/k8s-first-pod/bad-image-pod.yaml
kubectl get pod -n week3
kubectl describe pod bad-image -n week3
kubectl delete pod bad-image -n week3
```

## Cleanup
```bash
kubectl delete namespace week3
kind delete cluster --name week3-k8s
```

## 제출 Evidence
```markdown
# Day 4 Kubernetes Evidence

## Cluster
- Tool: kind
- OS: WSL/macOS
- Docker:
- kubectl:
- kind:
- Context:
- Nodes:

## Pod
- Command:
- Pod status:
- Logs/describe evidence:

## Failure
- Failure type:
- Event message:
- Recovery:
```
