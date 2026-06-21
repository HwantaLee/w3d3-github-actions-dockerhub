# Week 3: MSA 운영, GitHub 협업, Kubernetes 입문

## Overview
3주차는 Week 2에서 만든 Docker/Compose 경험을 실제 운영 흐름으로 확장한다. 앞의 2일은 MSA를 인프라가 운영해야 하는 서비스 토폴로지로 다루고, 3일차는 GitHub 협업과 CI gate를 하루에 압축한다. 4~5일차는 학생 기대가 큰 Kubernetes로 진입해 cluster, kubectl, Pod, Deployment, Service를 직접 확인한다.

이번 주의 중심 질문은 다음과 같다.

```text
여러 서비스로 나뉜 애플리케이션을 어떻게 협업하고, 검증하고, Kubernetes로 옮길 준비를 할 것인가?
```

GitHub는 하루짜리 압축 수업이므로 모든 고급 배포 전략을 깊게 다루지 않는다. 대신 branch, PR, merge, rebase, revert, tag, Actions CI gate가 왜 운영 사고를 줄이는지 하나의 흐름으로 묶는다. Kubernetes는 Day 4부터 실제 명령과 manifest를 손으로 확인한다.

## Learning Goals
- Monolith와 MSA의 차이를 배포 단위, 장애 영향 범위, 데이터 책임, 운영 복잡도 관점으로 설명한다.
- 서비스 목록, 포트, 프로토콜, 환경변수, 의존 서비스, health endpoint, 로그 위치를 운영 문서로 정리한다.
- Docker Compose로 frontend, api, worker, database를 실행하고 서비스별 상태를 확인한다.
- frontend-api, api-database, worker-queue 연결 문제를 network와 configuration 관점에서 분석한다.
- GitHub Flow 중심의 branch/PR/merge/rebase/revert/tag 흐름을 설명한다.
- GitHub Actions로 PR CI gate를 만들고 실패 로그를 읽는다.
- Kubernetes cluster/node/control plane/worker node/kubectl의 기본 역할을 설명한다.
- Pod, Deployment, Service를 실행하고 logs/describe/events로 상태를 확인한다.

## Weekly Keywords
- MSA
- service boundary
- topology
- health check
- timeout
- retry
- correlation id
- GitHub Flow
- pull request
- merge
- rebase
- revert
- tag
- GitHub Actions
- runner
- secret
- CI gate
- Kubernetes
- cluster
- node
- Pod
- Deployment
- Service
- rollout

## Schedule Index
- Day 1: 2주차 복습, Monolith vs MSA, 서비스 토폴로지, 표준 MSA 실습 앱 실행
- Day 2: 서비스 간 HTTP 통신, frontend-api 연결, api-database 연결, health check, 연결 실패 분석
- Day 3: GitHub 협업 압축, branch/PR/merge/rebase/revert/tag, GitHub Actions CI gate
- Day 4: Kubernetes 배경, 핵심 컨셉, 장점/단점, 활용 분야, kind 선택 이유, WSL/macOS 설치
- Day 5: kubectl 기본, 첫 Pod, Pod 장애 확인, Deployment, Service, 내부 통신, rollout 맛보기

## Required Deliverables
- MSA 실습 애플리케이션 실행 가능한 `compose.yaml`
- frontend, api, worker, database 요청 흐름과 의존성 다이어그램
- 서비스별 실행 조건 표: image/build, port, environment variable, dependency, health check, log command
- 장애 주입 및 복구 기록 1개
- GitHub branch/PR/merge/rebase/revert/tag 압축 실습 로그
- GitHub Actions CI workflow 1개와 실패 로그 분석 메모
- 로컬 Kubernetes 클러스터 확인 결과
- kind 설치 및 로컬 클러스터 확인 evidence
- Pod, Deployment, Service 샘플앱 실행 evidence
- 4주차 Kubernetes 확장 질문 목록

## Practice Environment
| 항목 | 기준 |
|---|---|
| Docker | `docker version`, `docker compose version` 실행 가능 |
| Local ports | frontend host port `18083`, optional api debug port `18084` 사용 가능 |
| GitHub | repository push, PR, Actions 실행 가능 |
| Kubernetes | kind, kubectl context 확인 가능 |
| Cost | Week 3는 로컬 Docker/Kubernetes 중심이다. cloud resource를 만들지 않는다. |
| Security | `.env`, credential, token, DB password를 public screenshot/README에 그대로 남기지 않는다. |

## Week 3 To Week 4 Mapping
| Week 3 evidence | Week 4 확장 |
|---|---|
| Compose service | Deployment |
| service name DNS | Kubernetes Service DNS |
| environment variable | ConfigMap/Secret |
| health endpoint | liveness/readiness probe |
| image tag | rollout/rollback 기준 |
| PR CI gate | 배포 전 검증 조건 |

## Weekly Checklist
- [ ] 표준 MSA 실습 앱을 `docker compose up --build`로 실행했다.
- [ ] frontend, api, worker, database 역할을 설명했다.
- [ ] service name DNS와 localhost의 차이를 설명했다.
- [ ] branch, PR, merge, rebase, revert, tag의 운영 의미를 설명했다.
- [ ] GitHub Actions CI gate 실패 로그를 읽었다.
- [ ] 로컬 Kubernetes cluster와 kubectl context를 확인했다.
- [ ] Pod를 생성하고 logs/describe/events를 확인했다.
- [ ] Deployment와 Service로 api를 배포하고 내부 통신을 확인했다.

## Glossary
3주차 용어는 [glossary.md](./glossary.md)를 기준으로 정리한다.

## Next Week Connection
4주차 Kubernetes는 3주차 후반에 시작한 Pod, Deployment, Service 경험을 ConfigMap, Secret, Ingress, probe, rollout/rollback, resources, Helm, observability까지 확장한다.
