# Week 3 Day 4: Kubernetes 컨셉과 kind 설치

## Overview
Day 4는 Kubernetes를 바로 명령어부터 치지 않고, 왜 Kubernetes가 등장했고 왜 현업에서 널리 쓰이는지부터 정리한다. MSA에서 늘어난 컨테이너 운영 문제를 cluster, node, control plane, worker node, kubelet, container runtime이라는 언어로 다시 표현한 뒤, WSL/macOS에서 kind 기반 로컬 클러스터를 설치하고 확인한다.

## Learning Goals
- Kubernetes가 등장한 배경과 Docker Compose만으로 부족해지는 지점을 설명한다.
- Kubernetes가 많이 쓰이는 이유, 장점, 단점, 자주 쓰이는 분야를 구분한다.
- kind와 k3s의 차이를 학습/테스트용 클러스터와 경량 운영 배포판 관점으로 비교한다.
- cluster, node, control plane, worker node, kubelet, container runtime의 역할을 구분한다.
- WSL과 macOS에서 Docker, kubectl, kind 설치 상태를 확인한다.
- kind cluster를 만들고 context, node, cluster-info를 확인한다.

## Lesson Index
| 교시 | 주제 | 핵심 산출물 |
|---|---|---|
| 1교시 | Kubernetes가 등장한 배경 | 컨테이너 수 증가, 배포 반복, 장애 복구, 스케줄링 문제 evidence |
| 2교시 | Kubernetes 핵심 컨셉 | cluster, node, control plane, worker node, kubelet, container runtime evidence |
| 3교시 | Kubernetes가 많이 쓰이는 이유 | 선언적 운영, self-healing, service discovery, rollout/rollback evidence |
| 4교시 | 장점과 단점 | 표준화/자동화/이식성 vs 러닝커브/YAML/비용/운영 부담 evidence |
| 5교시 | 많이 쓰이는 분야와 참고 사례 | MSA, SaaS, platform engineering, CI/CD, managed Kubernetes, edge evidence |
| 6교시 | 실습 도구 선택 | kind와 k3s 비교, kind 선택 이유 evidence |
| 7교시 | WSL/macOS kind 설치 | Docker, kubectl, kind 설치와 버전 확인 evidence |
| 8교시 | kind cluster 생성과 확인 | create cluster, context, node, cluster-info evidence |

## Practice Files And Assets
| 자료 | 용도 |
|---|---|
| `hands-on-lab.md` | 오늘 실습 흐름 실행 가이드 |
| `academic-foundations.md` | 공식/현업 기준 mapping |
| `assets/` | 이전 버전 보조 이미지 보관 위치. 새 수업에서는 필요할 때 선별 사용 |

## Session Visual Index
| 교시 | 주제 | 시각 자료 기준 |
|---|---|---|
| 1교시 | Kubernetes가 등장한 배경 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 2교시 | Kubernetes 핵심 컨셉 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 3교시 | Kubernetes가 많이 쓰이는 이유 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 4교시 | 장점과 단점 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 5교시 | 많이 쓰이는 분야와 참고 사례 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 6교시 | 실습 도구 선택 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 7교시 | WSL/macOS kind 설치 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 8교시 | kind cluster 생성과 확인 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |

## Today Evidence
| Evidence | 제출 기준 |
|---|---|
| command evidence | 실행/확인/로그/정리 명령 |
| failure note | 장애 재현, 관찰, 복구, 예방 |
| handoff note | 다음 운영자 또는 Week 4로 넘길 정보 |

## Official References
| Topic | Reference | 확인할 키워드 |
|---|---|---|
| Kubernetes Concepts | https://kubernetes.io/docs/concepts/ | cluster, pod, deployment, service |
| kubectl Cheat Sheet | https://kubernetes.io/docs/reference/kubectl/quick-reference/ | get, describe, logs, exec |
| kind Quick Start | https://kind.sigs.k8s.io/docs/user/quick-start/ | Docker, create cluster, node |
| k3s Docs | https://docs.k3s.io/ | lightweight Kubernetes, edge, server |


## End-Of-Day Checklist
- [ ] Kubernetes가 많이 쓰이는 이유와 단점을 함께 설명했다.
- [ ] kind와 k3s의 차이를 한 문장으로 설명했다.
- [ ] WSL 또는 macOS 설치 확인 결과를 남겼다.
- [ ] kind cluster 생성, context, node 확인 결과를 남겼다.
