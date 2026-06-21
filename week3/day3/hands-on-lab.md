# Week 3 Day 3 Hands-on Lab: GitHub 협업과 CI Gate

## Phase 1. Branch 시작
```bash
git status
git switch -c practice/github-ci-gate
```

## Phase 2. 작은 변경 만들기
```bash
mkdir -p practice/week3-ci
printf 'console.log("ci gate ok")\n' > practice/week3-ci/app.js
printf '{"scripts":{"test":"node practice/week3-ci/app.js"}}\n' > package.practice.json
```

## Phase 3. Workflow 읽기
```bash
cat week3/day3/labs/github-actions/ci.yml
```

확인할 것: `on`, `jobs`, `runs-on`, `steps`, `checkout`, test/build command.

## Phase 4. Git evidence
```bash
git status
git add practice/week3-ci package.practice.json
git commit -m "practice ci gate"
git log --oneline -3
```

## Phase 5. Rebase/Revert 개념 확인
```bash
git branch --show-current
git log --oneline --graph --decorate -5
```

실제 공유 branch에서 `reset --hard`를 사용하지 않는다. 되돌리기는 `git revert`를 기준으로 설명한다.

## Phase 6. Tag 기준 정리
```bash
git tag --list
# 예시만 설명: git tag v0.1.0
```

App version, Git tag, Docker image tag가 언제 같은 값이어야 하는지 메모한다.
