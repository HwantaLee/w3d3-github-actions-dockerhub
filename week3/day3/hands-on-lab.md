# Week 3 Day 3 Hands-on Lab: GitHub Flow와 PR CI Gate

## 공통 준비
```bash
git status
git switch -c feature/week3-ci-gate
```

## branch와 PR 흐름
```bash
git add week3/README.md
git commit -m "docs: update week3 operating flow"
git push -u origin feature/week3-ci-gate
```

GitHub에서 PR을 만들고 reviewer, status check, merge 방식이 어디에 표시되는지 확인한다.

## merge/rebase/revert 실습 기준
| 작업 | 확인할 것 |
|---|---|
| merge commit | 이력이 분기와 합류를 그대로 보여주는지 |
| squash merge | 여러 commit이 하나로 정리되는지 |
| rebase | 내 branch의 base가 최신 main으로 이동하는지 |
| revert | 공유된 commit을 새 commit으로 되돌리는지 |

## GitHub Actions CI gate 예시
샘플 workflow는 `week3/day3/labs/github-actions/ci.yml`에 있다. 실제 repository에서 테스트할 때는 아래처럼 복사한다.

```bash
mkdir -p .github/workflows
cp week3/day3/labs/github-actions/ci.yml .github/workflows/week3-ci.yml
git add .github/workflows/week3-ci.yml
git commit -m "ci: add week3 pull request gate"
git push
```

workflow 구조는 다음 형태를 기준으로 읽는다.

```yaml
name: ci
on:
  pull_request:
  push:
    branches: [ main ]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Show repository
        run: pwd && ls
      - name: Validate Week 3 markdown exists
        run: |
          test -f week3/README.md
          test -f week3/day3/hands-on-lab.md
```

## 실패 로그 만들기
CI gate의 의미는 실패했을 때 더 잘 보인다. `test -f week3/not-exists.md`처럼 존재하지 않는 파일을 잠깐 넣어 실패시키고, Actions log에서 어느 step이 실패했는지 확인한다. 확인 후 정상 조건으로 되돌린다.

## 제출 Evidence
```markdown
# Day 3 GitHub Evidence

## Branch strategy
- Selected strategy:
- Why:

## PR gate
- PR URL:
- Status check result:
- Failed log, if any:

## History operation
- merge/rebase/revert/tag command:
- Before:
- After:
- Risk note:
```
