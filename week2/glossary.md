# Week 2 Glossary: Docker 실행 환경 표준화

| Term | 뜻 | 운영 관점 질문 |
|---|---|---|
| Docker | 애플리케이션 실행 환경을 image와 container로 표준화하는 도구와 생태계 | 같은 실행 조건을 다른 사람이 재현할 수 있는가 |
| Docker Desktop | 로컬 장비에서 Docker를 쉽게 실행하고 관리하게 해주는 데스크톱 앱 | macOS에서는 chip/권한/실행 상태가 맞는가, Windows 사용자는 WSL 2/가상화 조건이 맞는가 |
| Docker Engine | image build, container run, network, volume을 실제로 처리하는 Docker 실행 엔진 | CLI 명령이 어느 daemon에 전달되는가 |
| Image | container를 만들기 위한 읽기 중심 실행 패키지 | runtime, app code, config default가 무엇을 포함하는가 |
| Container | image에서 시작된 실행 중인 process와 격리된 실행 환경 | 현재 running/stopped/exited 상태인가 |
| Registry | image를 저장하고 내려받는 저장소 | image 출처를 신뢰할 수 있는가 |
| Docker Hub | Docker의 대표 public registry | public image 사용 시 tag와 출처를 확인했는가 |
| Dockerfile | image를 만들기 위한 instruction 파일 | 빌드 절차가 문서화되어 재현 가능한가 |
| Build context | `docker build`가 image로 보낼 수 있는 파일 범위 | 불필요한 파일이나 secret이 포함되지 않았는가 |
| Layer | image를 구성하는 filesystem 변경 단위 | cache가 어디서 재사용되고 어디서 깨지는가 |
| Tag | image 이름에 붙이는 사람이 읽기 쉬운 version label | `latest`만 쓰지 않고 의미 있는 tag를 남겼는가 |
| Digest | image 내용을 기준으로 한 고유 식별값 | 같은 tag가 다른 내용을 가리킬 위험을 어떻게 줄이는가 |
| Port binding | host port를 container port에 연결하는 설정 | 사용자가 어떤 port로 접속하고 충돌은 없는가 |
| Volume | container lifecycle 밖에 데이터를 보존하는 저장 영역 | container 삭제 후 데이터가 남아야 하는가 |
| Bind mount | host directory/file을 container에 연결하는 방식 | 개발 중 파일 변경을 바로 반영해야 하는가 |
| Named volume | Docker가 이름으로 관리하는 volume | DB 데이터처럼 장기 보존할 데이터인가 |
| Environment variable | 실행 시점에 주입하는 설정 값 | 설정을 image에 굳히지 않고 바꿀 수 있는가 |
| Secret | password, token, key처럼 노출되면 안 되는 값 | 값이 repository, image layer, screenshot에 남지 않았는가 |
| Bridge network | Docker container들이 기본적으로 연결되는 가상 network 방식 | container끼리 어떻게 이름과 port로 통신하는가 |
| Compose | 여러 container를 하나의 YAML 파일로 정의하고 실행하는 Docker 도구 | 명령어 묶음을 파일로 재현 가능하게 관리하는가 |
| Service | Compose에서 하나의 container 실행 단위를 정의하는 항목 | app, db, cache 같은 역할이 명확한가 |
| `compose.yaml` | Compose application model을 담는 YAML 파일 | services, ports, environment, volumes, networks가 설명 가능한가 |
| `docker logs` | container의 stdout/stderr를 확인하는 명령 | 장애 증거가 log에 남아 있는가 |
| `docker exec` | 실행 중인 container 안에서 명령을 실행하는 방법 | 내부 상태를 확인해야 하는 이유가 있는가 |
| Cleanup | 사용하지 않는 container, image, volume을 정리하는 작업 | disk 낭비와 잘못된 재실행을 줄였는가 |
