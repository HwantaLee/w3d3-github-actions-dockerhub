# Week 1 Day 2 Sample App

정적 HTML 파일만 있는 로컬 웹 서버 실습용 샘플 앱이다.

## 실행

```bash
git clone https://github.com/niceguy61/kdt_devops_lecture_2026_rev2.git
cd kdt_devops_lecture_2026_rev2
cd week1/day2/sample-app
python3 -m http.server 8000
```

브라우저에서 확인한다.

```text
http://localhost:8000
```

터미널에서 확인한다.

```bash
curl http://localhost:8000
```

## 정리

서버를 실행한 터미널에서 `Ctrl+C`를 눌러 종료한다.
