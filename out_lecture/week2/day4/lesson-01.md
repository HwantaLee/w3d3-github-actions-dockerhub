# 1교시: environment variable과 runtime config

![Day 4 Runtime Observability overview](https://raw.githubusercontent.com/niceguy61/kdt_devops_lecture_2026_rev2/main/week2/day4/assets/day4-runtime-observability-overview.png)

## 수업 목표
- runtime config와 관찰 명령을 구분한다.
- 정상/장애 evidence를 선별한다.
- cleanup과 secret 비노출을 적용한다.

## 강의 전개
config를 image 밖에서 주입하고 env evidence를 남긴다.

이 교시는 설명만 듣고 지나가지 않는다. 명령은 반드시 code block으로 실행하고, 바로 이어서 검증 명령을 실행한다. 정상 출력이 다를 수 있는 부분은 전체 문자열을 외우지 않고 성공 패턴을 기록한다. 실패도 수업 산출물이다. 실패한 명령, 에러 요약, 가설, 다시 확인한 명령을 함께 남긴다.

## 실습 명령
```bash
docker run --rm -e APP_ENV=practice -e FEATURE_FLAG=on alpine:3.20 env
```

## 검증 명령
```bash
docker run --rm -e APP_ENV=practice alpine:3.20 sh -c "echo $APP_ENV"
```

## 실패 드릴과 오해 교정
| 상황 | 해석 |
|---|---|
| secret 노출 | README/screenshot/history에 값이 남지 않도록 masking한다. |
| logs만 붙임 | inspect/exec/stats와 함께 원인을 좁힌다. |
| cleanup 과잉 | volume/image/network 삭제 범위를 구분한다. |

## Cleanup
```bash
docker stop paperclip-day4-nginx paperclip-day4-bad || true
docker rm paperclip-day4-nginx paperclip-day4-bad || true
# 생성한 env 파일에는 실제 비밀번호를 남기지 않는다.
```

Cleanup은 비용과 데이터 안전을 동시에 다룬다. container를 지우는 명령과 volume/network/image를 지우는 명령은 의미가 다르다. 특히 volume 삭제는 database data 삭제일 수 있으므로 실습 volume인지 확인한 뒤 실행한다.

## Evidence
| 항목 | 제출 기준 |
|---|---|
| Runtime evidence | env/logs/inspect/exec/stats 중 필요한 결과 |
| Failure drill | 증상, 원인 후보, fix, recheck |
| Cleanup | 삭제한 것과 남긴 것 |

## 강의자 설명 포인트
Day 4는 "container가 떠 있다"와 "서비스가 정상이다"를 분리하는 날이다. `docker ps`에서 Up이라고 보여도 application은 설정 누락으로 의미 없는 상태일 수 있다. 반대로 container가 exit된 경우에도 logs를 보면 원인이 명확히 남아 있을 수 있다. 그래서 logs, inspect, exec, stats를 서로 다른 관찰 도구로 가르친다.

환경변수는 편하지만 secret 관리와 연결된다. 수업용 password라도 README나 screenshot에 그대로 남기는 습관은 위험하다. 학생에게 공개해도 되는 것은 env var 이름과 주입 방식이지 실제 credential 값이 아니라는 점을 강조한다. `.env.example`은 형식을 공유하는 파일이고, 실제 `.env`는 로컬 전용이다.

## 운영 해석
장애 분석은 감으로 하는 것이 아니라 관찰 위치를 바꾸며 좁혀가는 일이다. logs는 application이 말한 내용, inspect는 Docker metadata, exec는 container 내부 관찰, stats는 resource 관찰이다. 어떤 문제에는 logs만으로 충분하고, 어떤 문제는 inspect의 network/mount/env를 봐야 한다. 학생이 명령을 많이 아는 것보다 언제 무엇을 볼지 말할 수 있어야 한다.

Cleanup도 Day 4에서 다시 다룬다. 장애 드릴을 하다 보면 실패 container, 잘못 붙은 network, 오래된 volume, 잘못 만든 image tag가 남는다. 남은 자원은 다음 실습의 원인이 되므로, cleanup audit을 수업 산출물로 인정한다.

## README 기록 예시
```markdown
## Runtime Observation Evidence
- Runtime command:
- Env/config source:
- Secret masked? yes/no
- Logs summary:
- Inspect summary:
- Exec command/result:
- Stats/restart note:
- Failure drill RCA:
- Cleanup audit:
```

## 다음 연결
Day 5는 Day 2~4의 옵션을 compose.yaml로 옮겨 유명 아키텍처를 실행한다.
