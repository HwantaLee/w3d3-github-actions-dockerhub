# 3교시: 성공 상태 관찰 - 화면, 데이터, console, Network

## 수업 목표
- 정상 상태의 기준을 브라우저 화면, 데이터 표시, console, Network로 확인한다.
- 성공 상태를 먼저 기록해 이후 실패 상태와 비교한다.
- `data.json`이 화면에 표시되는 흐름을 너무 깊지 않게 관찰한다.

## 오늘 반드시 가져갈 것
| 필수 개념 | 왜 필수인가 | 놓치면 생기는 문제 | 확인 기록 |
|---|---|---|---|
| 정상 기준 | 성공이 무엇인지 알아야 실패를 구분한다. | 오류가 생겨도 무엇이 달라졌는지 모른다. | success baseline |
| 데이터 렌더링 | `data.json` 값이 화면에 보여야 앱 흐름을 확인한 것이다. | 정적 HTML만 보고 성공으로 착각한다. | 화면 메시지 |
| Console | JavaScript 오류가 남는 대표 위치다. | 화면만 보고 JS 실패를 놓친다. | console error 없음 |
| Network | 브라우저가 어떤 파일을 요청했는지 보여준다. | `data.json` 요청 실패를 찾지 못한다. | `data.json` 200 |

### 챌린저 복구 기준
- 개발자 도구를 전부 배우려 하지 않는다. Console과 Network 두 곳만 본다.
- 성공 상태에서는 오류가 없어야 한다는 기준을 먼저 적는다.
- 화면 문장, 상태 코드, 서버 로그를 같은 요청의 다른 관점으로 본다.

## 50분 운영
| 시간 | 활동 | 학습 초점 | 학생 산출 |
|---|---|---|---|
| 0-5분 | 정상 서버 상태 확인 | 서버가 켜져 있는지 본다. | server alive |
| 5-15분 | 화면 기준 읽기 | 성공 문장을 찾는다. | screen note |
| 15-30분 | Console 확인 | 오류 없음 기준을 본다. | console note |
| 30-40분 | Network 확인 | `data.json` 요청을 찾는다. | network note |
| 40-50분 | 성공 baseline 작성 | 이후 실패와 비교할 기준을 만든다. | success baseline |

## 0-5분 정상 서버 상태 확인
서버 터미널이 살아 있는지 확인한다. 꺼져 있으면 다시 실행한다.

```bash
cd week1/day4/sample-app
python3 -m http.server 8000
```

## 5-15분 화면 기준 읽기
브라우저에서 `http://localhost:8000`을 열고 아래 항목을 찾는다.

| 화면 항목 | 보여야 하는 내용 |
|---|---|
| 제목 | 로컬 서버 실행과 오류 관찰 실습 |
| 상태 박스 | 정상: data.json을 읽어서 화면에 표시했습니다. |
| 목록 | HTML, CSS, JavaScript, Local server |

## 15-30분 Console 확인
브라우저 개발자 도구를 열고 Console을 확인한다.

정상 기준:
- 빨간 오류가 없다.
- `Sample app data load failed`가 보이지 않는다.

## 30-40분 Network 확인
Network 탭에서 새로고침 후 다음 요청을 찾는다.

| 요청 | 기대 상태 |
|---|---|
| `/` 또는 `index.html` | 200 |
| `style.css` | 200 |
| `app.js` | 200 |
| `data.json` | 200 |

## 40-50분 성공 baseline 작성
| 확인 항목 | 정상 기준 |
|---|---|
| browser URL | |
| screen message | |
| console | 오류 없음 |
| `data.json` network status | |
| server log | |

## 다음 연결
다음 교시는 일부러 없는 URL을 요청해 404를 만들고, 서버가 죽은 상태와 resource가 없는 상태를 구분한다.
