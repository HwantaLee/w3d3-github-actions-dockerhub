# Week 3 Day4: Kubernetes 컨셉과 kind 설치

## Overview
Day 4는 바로 YAML부터 치지 않는다. Kubernetes가 왜 등장했고, 현업에서 왜 많이 쓰이며, kind를 왜 실습 도구로 선택하는지 설명한 뒤 WSL/macOS 설치와 cluster 생성을 진행한다.

## Learning Goals
- Kubernetes가 등장한 배경과 Compose만으로 부족해지는 지점을 설명한다.
- cluster/node/control plane/worker node/kubelet/container runtime을 구분한다.
- 장점과 단점을 함께 설명한다.
- WSL/macOS에서 Docker, kubectl, kind 설치 상태를 확인한다.
- kind cluster를 만들고 context/node/cluster-info를 확인한다.

## Lesson Index
| 교시 | 주제 | 핵심 확인 |
|---|---|---|
| 1교시 | Day3 10분 요약 + Kubernetes가 등장한 배경 | 컨테이너 수 증가, 배포 반복, 장애 복구, 스케줄링 문제 |
| 2교시 | Kubernetes 핵심 컨셉 | cluster, node, control plane, worker node, kubelet, container runtime |
| 3교시 | Kubernetes가 많이 쓰이는 이유 | 선언적 운영, self-healing, service discovery, rollout/rollback, 확장성 |
| 4교시 | 장점과 단점 | 표준화/자동화/이식성 vs 러닝커브/YAML/관찰/비용/운영 부담 |
| 5교시 | 많이 쓰이는 분야와 참고 사례 | MSA, SaaS, platform engineering, CI/CD, managed Kubernetes, edge/k3s |
| 6교시 | 실습 도구 선택 | kind는 학습/테스트용, k3s는 경량 운영 배포판 |
| 7교시 | WSL/macOS kind 설치 | Docker, kubectl, kind 설치와 버전 확인 |
| 8교시 | kind cluster 생성과 확인 | `kind create cluster`, context, node, cluster-info 확인 |

## Practice Files
| 자료 | 용도 |
|---|---|
| `hands-on-lab.md` | 당일 실습 명령과 확인 순서 |
| `academic-foundations.md` | 공식/현업 기준 mapping |
| `assets/` | 보조 시각 자료 |
| `labs/` | 실행 가능한 실습 파일 |

## Evidence Policy
| Evidence | 제출 기준 |
|---|---|
| command evidence | 명령과 핵심 출력 요약 |
| failure note | 증상, 첫 확인 명령, 원인 후보, 복구 기준 |
| handoff note | 다음 운영자 또는 다음 주제로 넘길 정보 |
| goorm EXP note | 8교시 배움일기 항목 |

## Official References
| Topic | Reference |
|---|---|
| Kubernetes Concepts | https://kubernetes.io/docs/concepts/ |
| kind Quick Start | https://kind.sigs.k8s.io/docs/user/quick-start/ |
| k3s Docs | https://docs.k3s.io/ |

## End-Of-Day Checklist
- [ ] 오늘의 핵심 흐름을 한 문장으로 설명했다.
- [ ] 명령 실행 결과를 evidence로 남겼다.
- [ ] 실패 로그 또는 이벤트를 하나 이상 읽었다.
- [ ] 다음 교시 또는 Week 4로 넘길 질문을 적었다.
