# Week 1 Day 2 Sample App

정적 HTML 파일과 환경변수/로그 실습용 Python 앱이 함께 있는 샘플 앱이다.

## 6교시 실행

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

## 7교시 실행

```bash
cp .env.example .env
python3 app.py
```

다른 터미널에서 확인한다.

```bash
curl http://localhost:8000/
curl http://localhost:8000/config
curl http://localhost:8000/not-found
curl http://localhost:8000/error
```

로그를 확인한다.

```bash
tail -n 20 logs/app.log
```

포트를 바꾸려면 `.env`의 `PORT` 값을 수정한 뒤 서버를 재기동한다.
