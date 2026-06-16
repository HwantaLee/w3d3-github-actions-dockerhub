# 5교시: Docker network 기본

## 수업 목표
- default bridge와 custom bridge를 구분한다.
- network ls/inspect/connect/disconnect 명령을 사용한다.
- container가 어떤 network에 붙었는지 확인한다.

## 강의 전개
Docker network는 container들이 서로 통신하는 공간이다. host에서 접속하려면 port publish가 필요하지만, 같은 Docker network 안의 container끼리는 container name으로 통신할 수 있다. Compose를 배우기 전에 이 감각을 CLI로 먼저 잡아야 한다.

이 교시는 설명만 듣고 지나가지 않는다. 명령은 반드시 code block으로 실행하고, 바로 이어서 검증 명령을 실행한다. 정상 출력이 다를 수 있는 부분은 전체 문자열을 외우지 않고 성공 패턴을 기록한다. 실패도 수업 산출물이다. 실패한 명령, 에러 요약, 가설, 다시 확인한 명령을 함께 남긴다.

## 실습 명령
```bash
docker network ls
docker network create paperclip-day2-net
docker run -d --name paperclip-net-pg --network paperclip-day2-net -e POSTGRES_PASSWORD=postgres -v paperclip-pg16-data:/var/lib/postgresql/data postgres:16
```

## 검증 명령
```bash
docker network inspect paperclip-day2-net --format "{{ json .Containers }}"
docker ps --filter name=paperclip-net-pg
```

## 실패 드릴과 오해 교정
| 상황 | 해석 |
|---|---|
| network 이름 중복 | 이미 있으면 재사용하거나 삭제 후 생성한다. |
| container가 default bridge에 있음 | --network 옵션 누락을 확인한다. |
| host port가 안 보임 | 같은 network 통신 실습이므로 publish하지 않은 것이 정상일 수 있다. |

## Cleanup
```bash
docker stop paperclip-net-pg || true
docker rm paperclip-net-pg || true
# network는 다음 교시에서 재사용
```

Cleanup은 비용과 데이터 안전을 동시에 다룬다. container를 지우는 명령과 volume/network/image를 지우는 명령은 의미가 다르다. 특히 volume 삭제는 database data 삭제일 수 있으므로 실습 volume인지 확인한 뒤 실행한다.

## Evidence
| 항목 | 제출 기준 |
|---|---|
| Network 이름 | paperclip-day2-net |
| Inspect 결과 | container 연결 여부 |
| 해석 | host publish와 network attach 구분 |

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
다음 교시는 같은 network 안에서 client container가 PostgreSQL container 이름으로 접속하는지 확인한다.
