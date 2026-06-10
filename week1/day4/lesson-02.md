# 2교시: 샘플앱 로컬 서버 실행

## 수업 목표
- 공통 샘플앱을 로컬 정적 서버로 실행한다.
- 브라우저, `curl -I`, 서버 로그가 각각 무엇을 확인하는지 구분한다.
- 서버 터미널과 확인 터미널을 분리해 사용한다.

## 오늘 반드시 가져갈 것
| 필수 개념 | 왜 필수인가 | 놓치면 생기는 문제 | 확인 기록 |
|---|---|---|---|
| 서버 실행 위치 | `http.server`는 현재 디렉터리 파일을 제공한다. | 엉뚱한 폴더를 서버로 열어 404가 난다. | `pwd`, `ls` |
| 서버 터미널 | 서버 프로세스가 요청을 받는 창이다. | 같은 터미널에서 확인 명령을 치려다 서버를 끈다. | server log |
| 브라우저 확인 | 사용자가 보는 화면 결과를 확인한다. | HTTP 상태는 모르고 화면만 본다. | URL, 화면 메시지 |
| `curl -I` 확인 | 상태 코드와 header를 확인한다. | 화면은 보이지만 상태 기준을 남기지 못한다. | 200 status |

### 챌린저 복구 기준
- 서버를 켠 터미널은 그대로 둔다. 확인 명령은 새 터미널에서 실행한다.
- `connection refused`는 서버가 꺼졌거나 포트가 다를 때 먼저 의심한다.
- 브라우저 주소는 `http://localhost:8000`부터 시작한다.

## 50분 운영
| 시간 | 활동 | 학습 초점 | 학생 산출 |
|---|---|---|---|
| 0-5분 | 실행 전 위치 확인 | 현재 경로를 고정한다. | `pwd` 기록 |
| 5-15분 | 서버 실행 | 서버 터미널을 유지한다. | start command |
| 15-30분 | 브라우저 확인 | 화면 성공 기준을 본다. | URL/screen note |
| 30-40분 | `curl` 확인 | 상태 코드를 남긴다. | HTTP status |
| 40-50분 | 서버 로그 확인 | 요청 기록을 읽는다. | log excerpt |

## 0-5분 실행 전 위치 확인
```bash
cd week1/day4/sample-app
pwd
ls -la
```

현재 폴더에 `index.html`, `app.js`, `data.json`, `README.md`가 있어야 한다.

## 5-15분 서버 실행
```bash
python3 -m http.server 8000
```

예상 출력:
```text
Serving HTTP on 0.0.0.0 port 8000 ...
```

이 터미널은 서버가 실행되는 동안 그대로 둔다.

## 15-30분 브라우저 확인
브라우저에서 접속한다.

```text
http://localhost:8000
```

확인할 문장:
```text
정상: data.json을 읽어서 화면에 표시했습니다.
```

## 30-40분 `curl` 확인
새 터미널에서 실행한다.

```bash
curl -I http://localhost:8000
curl -I http://localhost:8000/data.json
```

기대 결과는 `200` 상태 코드다.

## 40-50분 서버 로그 확인
서버 터미널에서 다음과 비슷한 로그를 찾는다.

```text
GET / HTTP/1.1
GET /data.json HTTP/1.1
```

## 실행 확인 기록
| 확인 항목 | 값 |
|---|---|
| working directory | |
| start command | |
| browser URL | |
| `curl -I /` status | |
| `curl -I /data.json` status | |
| server log excerpt | |

## 다음 연결
다음 교시는 지금 확인한 정상 상태를 기준으로 data rendering, console, Network를 조금 더 관찰한다.
