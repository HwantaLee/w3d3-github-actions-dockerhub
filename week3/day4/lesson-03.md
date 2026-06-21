# 3교시: Kubernetes가 많이 쓰이는 이유

## 수업 목표
- 선언적 운영, self-healing, service discovery, rollout/rollback, 확장성를 Kubernetes 도입 배경과 연결한다.
- 명령 실행 전 어떤 상태를 확인하려는지 설명한다.
- WSL/macOS 차이와 설치 증거를 남긴다.

## 핵심 설명
선언적 운영, self-healing, service discovery, rollout/rollback이 Kubernetes 도입 이유다.

## 실습 기준
```bash
# 자세한 명령은 week3/day4/hands-on-lab.md 참고
docker version
kubectl version --client=true
kind version
```

## 판단 표
| 확인 대상 | 정상 증거 |
|---|---|
| Docker | Docker Desktop/engine이 실행 중 |
| kubectl | client version 출력 |
| kind | kind version 출력 |
| cluster | `kubectl get nodes`에서 node Ready |


## Evidence Note
```markdown
# Evidence
- command:
- observed output:
- normal or failure:
- next action:
```
