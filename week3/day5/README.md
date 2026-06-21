# Week 3 Day5: Kubernetes 샘플앱 실행

## Overview
Day 5는 Day 4에서 만든 kind cluster 위에 샘플앱을 실행한다. Pod 직접 실행에서 Deployment와 Service로 넘어가며 Kubernetes가 원하는 상태를 유지하는 방식을 맛본다.

## Learning Goals
- Pod 직접 실행과 Deployment 실행의 차이를 desired state 관점으로 설명한다.
- Deployment manifest의 selector/template/replicas를 설명한다.
- Service가 Pod IP 변화를 어떻게 가리는지 endpoint로 확인한다.
- rollout status/history/undo를 사용해 image tag 변경과 복구 흐름을 맛본다.

## Lesson Index
| 교시 | 주제 | 핵심 확인 |
|---|---|---|
| 1교시 | Day4 10분 요약 + kubectl 기본 | context, namespace, get, describe, logs, exec, apply, delete |
| 2교시 | 첫 Pod 실행 | image, command, port, logs, exec, delete 흐름 |
| 3교시 | Pod 장애 확인 | ImagePullBackOff, CrashLoopBackOff, Pending 상태를 describe/events/logs로 확인 |
| 4교시 | Deployment가 필요한 이유 | Pod 직접 실행의 한계, desired state, replica, self-healing |
| 5교시 | Deployment manifest 구조와 배포 | apiVersion, kind, metadata, spec, selector, template |
| 6교시 | Service가 필요한 이유 | Pod IP 변화, 안정적인 접근 주소, ClusterIP, endpoint 확인 |
| 7교시 | 샘플앱 내부 통신과 rollout 맛보기 | service DNS, curlbox, image tag 변경, rollout status/undo |
| 8교시 | 구름 EXP 배움일기 | kind 설치, Pod/Deployment/Service 역할, Week4 Kubernetes 질문 |

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
| Pods | https://kubernetes.io/docs/concepts/workloads/pods/ |
| Deployments | https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ |
| Services | https://kubernetes.io/docs/concepts/services-networking/service/ |
| kubectl Cheat Sheet | https://kubernetes.io/docs/reference/kubectl/quick-reference/ |

## End-Of-Day Checklist
- [ ] 오늘의 핵심 흐름을 한 문장으로 설명했다.
- [ ] 명령 실행 결과를 evidence로 남겼다.
- [ ] 실패 로그 또는 이벤트를 하나 이상 읽었다.
- [ ] 다음 교시 또는 Week 4로 넘길 질문을 적었다.
