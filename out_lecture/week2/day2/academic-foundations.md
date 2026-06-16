# Week 2 Day 2 Academic And Professional Foundations

Day 2는 Docker container의 실행 상태가 어디에 남고, container들이 어떤 이름과 network boundary로 서로를 찾는지 다룬다. 핵심은 volume과 network를 옵션 암기가 아니라 운영 계약으로 읽는 것이다.

| 기준 | Day 2 연결 |
|---|---|
| Docker storage docs | container writable layer, named volume, bind mount의 lifecycle 구분 |
| Docker volumes docs | database data persistence와 volume 재사용 실습 |
| Docker bind mounts docs | host path 의존성과 개발 편의, 권한 위험 설명 |
| Docker networking docs | bridge network, user-defined network, container DNS 구분 |
| Docker run reference | `-v`, `--mount`, `--network`, `-p` 실행 옵션의 공식 기준 |
| PostgreSQL official image | data directory, initialization, password env 기준 |
| SRE/DevOps evidence culture | 데이터 생존 여부와 연결 경로를 query/log로 증명 |

## Conceptual Rationale

Container는 지우고 다시 만들 수 있어야 하지만, 모든 데이터가 같이 사라져야 하는 것은 아니다. Day 2의 첫 실험은 volume 없이 PostgreSQL container를 띄우고 데이터를 넣은 뒤 container를 삭제했을 때 데이터가 사라지는지 확인한다. 이 실패를 먼저 보여주면 volume이 "편의 기능"이 아니라 stateful workload의 필수 경계라는 점이 명확해진다.

Network도 같은 방식으로 다룬다. host에서 `localhost:15432`로 붙는 것과 같은 Docker network 안의 container가 `postgres16:5432`로 붙는 것은 다른 경로다. 학생은 port publishing과 service discovery를 분리해서 설명해야 한다.

## Official Links

- Docker storage: https://docs.docker.com/engine/storage/
- Docker volumes: https://docs.docker.com/engine/storage/volumes/
- Docker bind mounts: https://docs.docker.com/engine/storage/bind-mounts/
- Docker networking: https://docs.docker.com/engine/network/
- Docker bridge network driver: https://docs.docker.com/engine/network/drivers/bridge/
- Docker run reference: https://docs.docker.com/reference/cli/docker/container/run/
- Docker volume CLI: https://docs.docker.com/reference/cli/docker/volume/
- Docker network CLI: https://docs.docker.com/reference/cli/docker/network/
- PostgreSQL Docker Official Image: https://hub.docker.com/_/postgres

## Standards Crosswalk

| 기준 | 학생 행동 |
|---|---|
| Bloom apply/analyze | volume 없는 DB와 named volume DB의 데이터 생존 결과를 비교 |
| ABET-style problem solving | 접속 실패를 port, network, DNS, container 상태로 분류 |
| Professional responsibility | `docker volume rm`과 `down -v`류 삭제 위험을 설명 |
| SRE/DevOps evidence | query 결과, `docker volume ls`, `docker network inspect`를 evidence로 남김 |

## Completion Evidence

학생은 Day 2 종료 시점에 다음을 제출할 수 있어야 한다.

- volume 없는 PostgreSQL container에서 데이터가 사라진 증거
- named volume을 붙인 PostgreSQL container에서 데이터가 유지된 증거
- bind mount로 host file이 container에 보이는 증거
- user-defined network에서 container name DNS로 DB에 접속한 증거
- host port publish와 Docker internal network의 차이를 설명한 README
