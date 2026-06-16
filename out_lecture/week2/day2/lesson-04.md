# 4교시: bind mount와 host path 주의

## 수업 목표
- bind mount와 named volume을 비교한다.
- host 파일 변경이 container 응답에 반영되는지 확인한다.
- read-only mount를 사용해 안전한 실습 기준을 만든다.

## 강의 전개
bind mount는 host filesystem을 container path에 직접 연결한다. 개발 중 HTML, config, script를 빠르게 바꿔 확인할 때 유용하지만, host path가 강하게 드러난다. macOS와 Linux의 path 차이, 권한 차이, read/write mode를 이해해야 한다.

이 교시는 설명만 듣고 지나가지 않는다. 명령은 반드시 code block으로 실행하고, 바로 이어서 검증 명령을 실행한다. 정상 출력이 다를 수 있는 부분은 전체 문자열을 외우지 않고 성공 패턴을 기록한다. 실패도 수업 산출물이다. 실패한 명령, 에러 요약, 가설, 다시 확인한 명령을 함께 남긴다.

## 실습 명령
```bash
mkdir -p week2/day2/tmp-bind/html
printf "<h1>bind mount v1</h1>" > week2/day2/tmp-bind/html/index.html
docker run -d --name paperclip-bind-web -p 18082:80 -v "$PWD/week2/day2/tmp-bind/html:/usr/share/nginx/html:ro" nginx:alpine
```

```bash
printf "<h1>bind mount v2</h1>" > week2/day2/tmp-bind/html/index.html
```

## 검증 명령
```bash
curl -s http://localhost:18082
docker inspect paperclip-bind-web --format "{{ json .Mounts }}"
```

## 실패 드릴과 오해 교정
| 상황 | 해석 |
|---|---|
| host path가 틀림 | container는 뜨지만 expected file이 보이지 않을 수 있다. |
| :ro를 빼먹음 | container 쪽에서 host file을 수정할 위험이 생긴다. |
| Windows/mac path 문제 | Docker Desktop file sharing/path permission을 확인한다. |

## Cleanup
```bash
docker stop paperclip-bind-web || true
docker rm paperclip-bind-web || true
rm -rf week2/day2/tmp-bind
```

Cleanup은 비용과 데이터 안전을 동시에 다룬다. container를 지우는 명령과 volume/network/image를 지우는 명령은 의미가 다르다. 특히 volume 삭제는 database data 삭제일 수 있으므로 실습 volume인지 확인한 뒤 실행한다.

## Evidence
| 항목 | 제출 기준 |
|---|---|
| Bind source/destination | host path와 container path |
| HTTP 결과 | v1/v2 변경 확인 |
| mode | read-only 여부 |

## 강의자 설명 포인트
이 실습의 핵심은 명령어 자체가 아니라 경계다. container는 실행 단위이고, volume은 data lifecycle이며, network는 통신 경계다. 학생이 `docker run` 한 줄을 볼 때 `-v`, `--network`, `-p`를 옵션 목록으로 외우면 뒤에서 Compose와 Kubernetes로 넘어갈 때 같은 혼란이 반복된다. 그래서 각 옵션을 "무엇을 container 밖으로 분리하는가"라는 질문으로 읽게 한다.

강의 중에는 성공 출력보다 실패 출력의 의미를 더 오래 다룬다. port가 열리지 않은 것은 web server 문제가 아닐 수 있고, DB 접속 실패는 password 문제가 아니라 network boundary 문제일 수 있다. host terminal, container 내부, 같은 Docker network의 client container는 모두 서로 다른 관찰 위치다. 학생이 어디에서 명령을 실행하는지 말로 먼저 설명한 뒤 CLI를 실행하게 한다.

## 운영 해석
실무에서 database container를 다룰 때 가장 위험한 실수는 cleanup을 단순 정리로만 보는 것이다. container 삭제는 process와 container writable layer를 정리하는 것이고, volume 삭제는 data를 삭제하는 것이다. network 삭제는 통신 경로를 정리하는 것이다. 이 세 가지를 구분하지 않으면 실습은 성공해도 운영 사고를 배운 셈이 된다.

README에는 "실행됐다" 대신 "어떤 data를 남기고 무엇을 삭제했는지"를 써야 한다. Day 2 evidence는 Day 5 Compose에서 `volumes`와 `networks`를 읽는 기준이 된다. Compose의 YAML 항목은 갑자기 생긴 문법이 아니라 Day 2에서 손으로 실행한 storage/network 결정을 파일로 옮긴 것이다.

## README 기록 예시
```markdown
## Storage/Network Evidence
- Container:
- Volume name:
- Volume target path:
- Network name:
- Host port published? yes/no
- Container DNS check:
- Data survived container replacement? yes/no
- Cleanup decision:
```

## 다음 연결
다음 교시는 storage에서 network로 넘어간다. host port 공개와 container 간 통신은 다른 문제다.
