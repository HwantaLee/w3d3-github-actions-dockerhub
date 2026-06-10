# 4교시: 실패 1 - 잘못된 URL과 404 관찰

## 수업 목표
- 404가 "서버가 죽었다"가 아니라 "요청한 resource가 없다"는 뜻임을 이해한다.
- 잘못된 URL을 요청하고 브라우저, `curl`, 서버 로그에서 같은 실패를 확인한다.
- 실패를 고치기 전에 관찰 기록을 먼저 남긴다.

## 오늘 반드시 가져갈 것
| 필수 개념 | 왜 필수인가 | 놓치면 생기는 문제 | 확인 기록 |
|---|---|---|---|
| 404 | 서버는 응답했지만 요청한 파일이 없다는 신호다. | 서버 종료, 포트 오류, 파일 없음이 섞인다. | failing URL, 404 status |
| connection refused | 서버 프로세스가 없거나 포트가 다를 때 자주 보인다. | 404와 같은 문제로 오해한다. | server alive check |
| URL 경로 | 브라우저 주소의 경로가 파일 요청으로 연결된다. | 없는 파일을 요청하고 앱 오류로 착각한다. | requested path |
| 관찰 후 수정 | 실패 상태를 먼저 기록해야 비교가 가능하다. | 고친 뒤 무엇이 문제였는지 설명하지 못한다. | observe/fix/recheck |

### 챌린저 복구 기준
- 404가 나오면 먼저 "서버가 살아 있다"는 점을 확인한다.
- 없는 파일을 요청했는지 URL 끝부분을 읽는다.
- 실패를 만들었으면 바로 고치지 말고 브라우저, `curl`, 서버 로그를 각각 한 줄씩 기록한다.

## 50분 운영
| 시간 | 활동 | 학습 초점 | 학생 산출 |
|---|---|---|---|
| 0-5분 | 정상 기준 재확인 | 200 상태에서 시작한다. | baseline |
| 5-15분 | 없는 URL 요청 | 브라우저에서 404를 만든다. | failing URL |
| 15-25분 | `curl`로 404 확인 | 상태 코드를 기록한다. | `curl -I` result |
| 25-35분 | 서버 로그 확인 | 서버가 요청을 받았는지 본다. | log excerpt |
| 35-50분 | recheck | 정상 URL로 돌아와 비교한다. | recheck note |

## 0-5분 정상 기준 재확인
```bash
curl -I http://localhost:8000
```

기대 결과는 `200`이다.

## 5-15분 없는 URL 요청
브라우저에서 아래 주소를 연다.

```text
http://localhost:8000/no-such-file.html
```

이 상태는 의도적으로 만든 실패다.

## 15-25분 `curl`로 404 확인
```bash
curl -I http://localhost:8000/no-such-file.html
```

기대 결과:
```text
HTTP/1.0 404 File not found
```

## 25-35분 서버 로그 확인
서버 터미널에서 `/no-such-file.html` 요청이 남았는지 확인한다. 요청이 보이면 서버는 살아 있고, 요청한 파일이 없어서 404가 난 것이다.

## 35-50분 recheck
정상 URL로 돌아온다.

```bash
curl -I http://localhost:8000
curl -I http://localhost:8000/index.html
```

## 404 관찰 기록
| 항목 | 값 |
|---|---|
| failing URL | |
| browser result | |
| `curl -I` status | |
| server log excerpt | |
| 원인 후보 | wrong URL/resource missing |
| recheck URL/status | |

## 다음 연결
다음 교시는 앱 파일과 데이터 요청을 살짝 깨뜨려 console과 Network에서 오류를 관찰한다.
