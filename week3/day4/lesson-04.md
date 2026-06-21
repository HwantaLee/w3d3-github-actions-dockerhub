# 4교시: 장점과 단점

## 수업 목표
- 표준화/자동화/이식성 vs 러닝커브/YAML/관찰/비용/운영 부담를 Kubernetes 도입 배경과 연결한다.
- 명령 실행 전 어떤 상태를 확인하려는지 설명한다.
- WSL/macOS 차이와 설치 증거를 남긴다.

## 핵심 설명
Kubernetes는 강력하지만 YAML, 관찰, 비용, 운영 부담이 함께 온다.

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
