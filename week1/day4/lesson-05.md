# 5교시: 실패 2 - data.json 경로와 JSON 오류 관찰

## 수업 목표
- 데이터 파일 경로 오류와 JSON 문법 오류를 안전하게 체험한다.
- 브라우저 console과 Network에서 오류 흔적을 찾는다.
- 오류를 복구하고 같은 기준으로 다시 확인한다.

## 오늘 반드시 가져갈 것
| 필수 개념 | 왜 필수인가 | 놓치면 생기는 문제 | 확인 기록 |
|---|---|---|---|
| 데이터 요청 | `app.js`가 `data.json`을 HTTP로 요청한다. | 파일은 있는데 화면에 데이터가 안 보이는 이유를 찾지 못한다. | Network `data.json` |
| Console 오류 | JavaScript나 JSON 처리 실패가 console에 남는다. | 화면만 보고 원인을 추측한다. | console message |
| 안전한 실패 | 의도적으로 작은 오류를 만들고 바로 복구한다. | 실습 파일이 계속 깨진 상태로 남는다. | break/fix note |
| Recheck | 복구 후 정상 기준으로 다시 확인한다. | 고쳤는지 확인하지 않고 넘어간다. | success recheck |

### 챌린저 복구 기준
- 오류를 만들기 전에 정상 `data.json`을 복사해 두거나 변경 내용을 메모한다.
- JSON 오류는 쉼표, 따옴표, 중괄호부터 확인한다.
- 복구가 안 되면 `git diff` 또는 원본 샘플과 비교한다.

## 50분 운영
| 시간 | 활동 | 학습 초점 | 학생 산출 |
|---|---|---|---|
| 0-5분 | 정상 데이터 확인 | data.json 200을 본다. | baseline |
| 5-20분 | 경로 오류 체험 | 요청 실패를 만든다. | network error |
| 20-35분 | JSON 오류 체험 | parsing 실패를 본다. | console error |
| 35-45분 | 복구 | 원래 상태로 되돌린다. | fixed file |
| 45-50분 | recheck | 성공 기준을 다시 확인한다. | recheck note |

## 0-5분 정상 데이터 확인
```bash
curl -I http://localhost:8000/data.json
```

기대 결과는 `200`이다.

## 5-20분 경로 오류 체험
`app.js`에서 아래 줄을 찾는다.

```js
const response = await fetch("./data.json");
```

잠시만 다음처럼 바꾼다.

```js
const response = await fetch("./missing-data.json");
```

브라우저를 새로고침하고 확인한다.

| 볼 곳 | 기대 관찰 |
|---|---|
| 화면 | 데이터를 불러오지 못했다는 메시지 |
| Console | `Sample app data load failed` |
| Network | `missing-data.json` 404 |

## 20-35분 JSON 오류 체험
`app.js`를 원래대로 돌린 뒤, `data.json`에서 쉼표 하나를 일부러 잘못 넣거나 따옴표를 하나 지운다. 브라우저를 새로고침하고 console 오류를 확인한다.

주의: 오류를 본 뒤 바로 원래 JSON으로 복구한다.

## 35-45분 복구
정상 값으로 되돌린다.

```js
const response = await fetch("./data.json");
```

`data.json`도 원래 JSON 형식으로 되돌린다.

## 45-50분 recheck
```bash
curl -I http://localhost:8000/data.json
```

브라우저 화면에 정상 메시지가 다시 보이는지 확인한다.

## 오류 관찰 기록
| 오류 유형 | 관찰한 곳 | 메시지/상태 | 복구 방법 |
|---|---|---|---|
| wrong data path | Network/Console | | |
| broken JSON | Console | | |
| recheck | Browser/curl | | |

## 다음 연결
다음 교시는 오늘 관찰한 성공/실패/오류를 README와 runbook으로 정리한다.
