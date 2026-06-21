# Week 3 Day 5: Kubernetes 샘플앱 실행

## Overview
Day 5는 Day 4에서 만든 kind 클러스터 위에 기초 샘플앱을 실행한다. 먼저 kubectl 기본 명령과 첫 Pod를 확인한 뒤, Pod 직접 실행의 한계를 Deployment와 Service로 해결한다. 마지막에는 내부 통신과 rollout/undo를 맛보며 Week4의 본격 Kubernetes 운영 수업으로 연결한다.

## Learning Goals
- Pod 직접 실행과 Deployment 실행의 차이를 desired state와 self-healing 관점으로 설명한다.
- Deployment manifest의 selector, template, replicas가 어떤 의미인지 설명한다.
- Service가 Pod IP 변화 문제를 어떻게 가리는지 ClusterIP와 endpoint로 확인한다.
- rollout status, history, undo를 사용해 image tag 변경과 되돌리기 흐름을 맛본다.
- 실패 증상을 숨기지 않고 재현 조건, 관찰 결과, 수정 또는 요청사항으로 기록한다.
- Week 4 Kubernetes 확장 수업으로 넘길 질문을 남긴다.

## Lesson Index
| 교시 | 주제 | 핵심 산출물 |
|---|---|---|
| 1교시 | kubectl 기본 | context, namespace, get, describe, logs, exec, apply, delete evidence |
| 2교시 | 첫 Pod 실행 | image, command, port, logs, exec, delete evidence |
| 3교시 | Pod 장애 확인 | ImagePullBackOff, CrashLoopBackOff, Pending 상태 evidence |
| 4교시 | Deployment가 필요한 이유 | Pod 직접 실행의 한계, desired state, replica, self-healing evidence |
| 5교시 | Deployment manifest 구조와 배포 | apiVersion, kind, metadata, spec, selector, template evidence |
| 6교시 | Service가 필요한 이유 | Pod IP 변화, 안정적인 접근 주소, ClusterIP, endpoint evidence |
| 7교시 | 샘플앱 내부 통신과 rollout 맛보기 | service DNS, curlbox, image tag 변경, rollout status/undo evidence |
| 8교시 | 구름 EXP 배움일기 | kind 설치, Pod/Deployment/Service 역할, Week4 Kubernetes 질문 |

## Practice Files And Assets
| 자료 | 용도 |
|---|---|
| `hands-on-lab.md` | 오늘 실습 흐름 실행 가이드 |
| `academic-foundations.md` | 공식/현업 기준 mapping |
| `assets/` | 이전 버전 보조 이미지 보관 위치. 새 수업에서는 필요할 때 선별 사용 |

## Session Visual Index
| 교시 | 주제 | 시각 자료 기준 |
|---|---|---|
| 1교시 | kubectl 기본 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 2교시 | 첫 Pod 실행 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 3교시 | Pod 장애 확인 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 4교시 | Deployment가 필요한 이유 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 5교시 | Deployment manifest 구조와 배포 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 6교시 | Service가 필요한 이유 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 7교시 | 샘플앱 내부 통신과 rollout 맛보기 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |
| 8교시 | 구름 EXP 배움일기 | 교시 전용 보드/명령 결과 캡처 또는 수업 중 Mermaid 다이어그램 |

## Today Evidence
| Evidence | 제출 기준 |
|---|---|
| command evidence | 실행/확인/로그/정리 명령 |
| failure note | 장애 재현, 관찰, 복구, 예방 |
| handoff note | 다음 운영자 또는 Week 4로 넘길 정보 |

## Official References
| Topic | Reference | 확인할 키워드 |
|---|---|---|
| Pods | https://kubernetes.io/docs/concepts/workloads/pods/ | pod, container, lifecycle |
| Deployments | https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ | desired state, replica, rollout |
| Services | https://kubernetes.io/docs/concepts/services-networking/service/ | ClusterIP, selector, endpoint |
| kubectl Cheat Sheet | https://kubernetes.io/docs/reference/kubectl/quick-reference/ | get, describe, logs, exec |
| kind Quick Start | https://kind.sigs.k8s.io/docs/user/quick-start/ | Docker, create cluster, delete cluster |


## End-Of-Day Checklist
- [ ] 오늘의 핵심 흐름을 한 문장으로 설명했다.
- [ ] 명령 실행 결과를 evidence로 남겼다.
- [ ] 실패 로그 또는 이벤트를 하나 이상 읽었다.
- [ ] Week 4에서 더 깊게 다룰 질문을 적었다.
