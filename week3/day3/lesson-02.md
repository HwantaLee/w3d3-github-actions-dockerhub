# 2교시: branch 전략 압축

## 수업 목표
- GitHub Flow 중심, trunk-based/Git Flow 선택 기준 비교를 배포 사고 예방 관점으로 설명한다.
- Git 명령을 이력 상태 확인과 연결한다.
- 실패했을 때 되돌리기 기준을 말한다.

## 핵심 설명
GitHub Flow를 기본으로 두고 trunk-based/Git Flow는 선택 기준만 비교한다.

## 실습 기준
```bash
cd /mnt/d/paperclip
git status
git branch --show-current
# 자세한 흐름은 week3/day3/hands-on-lab.md 참고
```

## 반드시 구분할 것
| 구분 | 기준 |
|---|---|
| merge | 협업 이력을 보존하고 합친다. |
| rebase | 내 branch의 base를 최신으로 정리한다. 공유 후에는 주의한다. |
| revert | 공유된 commit을 새 commit으로 되돌린다. |
| tag | 특정 릴리스 지점을 이름으로 고정한다. |
| CI gate | merge 전에 자동 검증으로 위험을 줄인다. |



## Evidence Note
```markdown
# Evidence
- command:
- observed output:
- normal or failure:
- next action:
```
