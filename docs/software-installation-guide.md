# 필수 소프트웨어 설치 가이드: macOS / Linux

이 문서는 Week 1-2 실습을 시작하기 전에 반드시 필요한 소프트웨어를 macOS와 Linux 기준으로 준비하는 절차다. 목표는 "설치했다"가 아니라 터미널에서 명령이 실행되고, 버전과 상태를 evidence로 남길 수 있는 상태다.

## 0. 설치 전 원칙

설치 중 막히면 바로 다음 정보를 기록한다.

| 기록 항목 | 예시 |
|---|---|
| OS | macOS 14 Apple silicon, Ubuntu 24.04 등 |
| 설치 단계 | Git 설치 중, Docker daemon 시작 중 등 |
| 실행 명령 | `git --version`, `docker version` |
| 에러 메시지 | secret 없이 핵심 문장만 기록 |
| 확인한 공식 문서 | URL |

password, token, MFA code, verification code는 README, 스크린샷, 수업 채팅에 남기지 않는다.

## 1. 준비물 전체 목록

| 도구 | Week | 반드시 필요한 이유 | 확인 명령 |
|---|---:|---|---|
| Web browser | 1 | GitHub, 공식 문서, 로컬 앱 확인 | 브라우저 실행 |
| Terminal | 1 | CLI evidence 작성 | `pwd` |
| GitHub account | 1 | repository, README, push | GitHub 로그인 |
| Git | 1 | commit, branch, push | `git --version` |
| VS Code | 1 | 파일 편집, 내장 terminal | `code --version` 또는 VS Code terminal |
| Python 3 | 1 | 로컬 정적 서버 실행 | `python3 --version` |
| curl | 1 | HTTP status 확인 | `curl --version` |
| Docker | 2 | image/container 실습 | `docker version` |
| Docker Compose | 2 | multi-container 실행 | `docker compose version` |

## 2. macOS 설치

### 2.1 OS와 CPU 확인

터미널을 열고 다음을 실행한다.

```bash
sw_vers
uname -m
```

`uname -m` 결과가 `arm64`이면 Apple silicon, `x86_64`이면 Intel Mac이다. Docker Desktop 설치 파일을 고를 때 이 차이가 중요하다.

### 2.2 Homebrew 설치

Homebrew는 macOS에서 Git, Python, curl 같은 CLI 도구를 쉽게 설치하는 package manager다. 이미 설치되어 있으면 건너뛴다.

```bash
brew --version
```

없으면 Homebrew 공식 사이트의 설치 명령을 사용한다.

- 공식 문서: https://brew.sh/

설치 후 새 터미널을 열고 다시 확인한다.

```bash
brew --version
brew doctor
```

`brew doctor`가 warning을 출력할 수 있다. 수업 시작 전에는 `brew --version`이 동작하면 우선 진행 가능하다.

### 2.3 Git 설치

```bash
brew install git
git --version
```

Git 사용자 이름과 이메일을 설정한다. 공개 repository에 보일 수 있으므로 수업용으로 사용 가능한 값을 넣는다.

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git config --global init.defaultBranch main
git config --global --list
```

### 2.4 VS Code 설치

1. VS Code 공식 다운로드 페이지에서 macOS용 설치 파일을 받는다.
2. 압축을 풀고 `Visual Studio Code.app`을 `Applications` 폴더로 이동한다.
3. VS Code를 실행한다.
4. VS Code에서 `View > Terminal` 또는 `Terminal > New Terminal`을 연다.

- 공식 문서: https://code.visualstudio.com/docs/setup/mac

`code` 명령이 필요하면 VS Code에서 Command Palette를 열고 `Shell Command: Install 'code' command in PATH`를 실행한다.

```bash
code --version
```

`code --version`이 실패해도 VS Code 안의 terminal에서 `pwd`, `git --version`이 되면 Week 1 실습은 진행 가능하다.

### 2.5 Python 3 설치

macOS 기본 Python 상태는 장비마다 다를 수 있다. 수업에서는 `python3` 명령이 필요하다.

```bash
python3 --version
```

없거나 너무 오래된 버전이면 Homebrew로 설치한다.

```bash
brew install python
python3 --version
python3 -m http.server --help
```

### 2.6 curl 확인

macOS에는 보통 curl이 포함되어 있다.

```bash
curl --version
curl -I https://example.com
```

`HTTP/2 200` 또는 `HTTP/1.1 200 OK`처럼 status line이 보이면 충분하다.

### 2.7 Docker Desktop 설치

1. Docker Desktop 공식 Mac 설치 문서를 연다.
2. Apple silicon 또는 Intel Mac에 맞는 설치 파일을 선택한다.
3. `.dmg` 파일을 열고 Docker를 `Applications`로 이동한다.
4. Docker Desktop을 실행한다.
5. 필요한 권한 요청을 승인한다.
6. 상단 메뉴 또는 Docker Desktop 창에서 running 상태를 확인한다.

- 공식 문서: https://docs.docker.com/desktop/setup/install/mac-install/

터미널을 새로 열고 확인한다.

```bash
docker version
docker compose version
docker run --rm hello-world
docker ps
```

`docker version`에서 Client는 보이는데 Server가 보이지 않으면 Docker Desktop이 실행 중인지 먼저 확인한다.

## 3. Linux 설치

Linux는 배포판마다 package manager가 다르다. 수업 기준은 Ubuntu/Debian 계열을 우선으로 두고, Fedora/RHEL 계열은 공식 문서를 따라 같은 확인 명령을 실행한다.

### 3.1 OS 확인

```bash
cat /etc/os-release
uname -m
```

`ID=ubuntu`, `ID=debian`, `ID=fedora` 같은 값을 기록한다.

### 3.2 기본 업데이트

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
```

Fedora:

```bash
sudo dnf check-update
sudo dnf install -y curl git python3
```

### 3.3 Git 설치

Ubuntu/Debian:

```bash
sudo apt install -y git
git --version
```

Fedora:

```bash
sudo dnf install -y git
git --version
```

Git 기본 설정:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git config --global init.defaultBranch main
git config --global --list
```

### 3.4 VS Code 설치

VS Code는 배포판별 공식 설치 문서를 따른다.

- 공식 문서: https://code.visualstudio.com/docs/setup/linux

Ubuntu/Debian에서 `.deb` 파일을 받은 경우:

```bash
sudo apt install ./code_*.deb
code --version
```

Microsoft repository를 등록하는 방식도 공식 문서에 있다. 교육장 장비에서는 조직 정책상 repository 등록이 막힐 수 있으므로, 막히면 에러 메시지와 시도한 공식 문서 URL을 기록한다.

### 3.5 Python 3 설치

Ubuntu/Debian:

```bash
sudo apt install -y python3
python3 --version
python3 -m http.server --help
```

Fedora:

```bash
sudo dnf install -y python3
python3 --version
python3 -m http.server --help
```

### 3.6 curl 설치와 확인

Ubuntu/Debian:

```bash
sudo apt install -y curl
curl --version
curl -I https://example.com
```

Fedora:

```bash
sudo dnf install -y curl
curl --version
curl -I https://example.com
```

### 3.7 Docker 설치

Linux에서는 Docker Desktop 또는 Docker Engine 중 하나를 선택한다. 초보자는 Docker Desktop이 GUI와 Compose를 함께 제공해 편하지만, 서버형 Linux나 교육장 VM에서는 Docker Engine이 더 일반적이다.

Docker Desktop for Linux:

- 공식 문서: https://docs.docker.com/desktop/setup/install/linux/

Docker Engine for Ubuntu:

- 공식 문서: https://docs.docker.com/engine/install/ubuntu/

Docker Engine for Debian:

- 공식 문서: https://docs.docker.com/engine/install/debian/

Docker Engine for Fedora:

- 공식 문서: https://docs.docker.com/engine/install/fedora/

Ubuntu 기준 Docker Engine 설치 후 확인:

```bash
sudo systemctl status docker
docker version
sudo docker run --rm hello-world
```

일반 사용자로 `docker` 명령을 매번 `sudo` 없이 쓰려면 Docker 공식 post-install 절차를 따른다.

- 공식 문서: https://docs.docker.com/engine/install/linux-postinstall/

```bash
sudo usermod -aG docker "$USER"
newgrp docker
docker run --rm hello-world
docker compose version
```

주의: `docker` group은 Docker daemon 접근 권한을 준다. 개인 실습 장비에서는 편의를 위해 사용할 수 있지만, 공유 서버나 회사 장비에서는 보안 정책을 먼저 따른다.

## 4. GitHub 계정과 인증

### 4.1 계정 만들기

1. GitHub 공식 계정 생성 문서를 연다.
2. 수업용으로 사용할 이메일을 준비한다.
3. 이메일 인증을 완료한다.
4. 가능하면 MFA를 켠다.

- 공식 문서: https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github
- MFA 문서: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa

### 4.2 HTTPS push와 token

GitHub password를 Git push password로 사용하지 않는다. HTTPS 인증이 필요한 경우 personal access token 또는 Git Credential Manager/browser login 흐름을 사용한다.

- PAT 공식 문서: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

README에 남길 것은 token 값이 아니라 다음 항목뿐이다.

```markdown
| 항목 | 기록 |
|---|---|
| GitHub login | success/blocker |
| MFA | enabled/not yet |
| push method | HTTPS with credential manager / SSH / blocker |
| secret exposed | no |
```

## 5. 최종 확인 스크립트

아래 명령을 한 줄씩 실행하고 결과를 README evidence table에 요약한다.

```bash
pwd
git --version
python3 --version
curl --version
curl -I https://example.com
docker version
docker compose version
docker run --rm hello-world
docker ps
```

VS Code CLI가 준비된 경우:

```bash
code --version
```

## 6. 자주 막히는 지점

| 증상 | 먼저 확인할 것 | 기록할 evidence |
|---|---|---|
| `command not found: git` | 설치 여부, 새 terminal 여부, PATH | 명령과 에러 한 줄 |
| `code --version` 실패 | VS Code CLI PATH 등록 여부 | VS Code GUI terminal 대체 여부 |
| `python: command not found` | `python3` 명령 사용 여부 | `python3 --version` 결과 |
| `curl` HTTP 실패 | 인터넷 연결, 프록시, 인증 페이지 | status 또는 에러 요약 |
| `Cannot connect to the Docker daemon` | Docker Desktop/daemon running 상태 | Client/Server 출력 차이 |
| permission denied on Docker | Linux user group 또는 `sudo` 필요 여부 | `sudo docker run` 성공 여부 |
| port already allocated | 기존 container/process가 같은 port 사용 | `docker ps`, 사용한 port |

## 7. 공식 문서 모음

| 도구 | 공식 문서 |
|---|---|
| Git install | https://git-scm.com/book/en/v2/Getting-Started-Installing-Git |
| VS Code macOS | https://code.visualstudio.com/docs/setup/mac |
| VS Code Linux | https://code.visualstudio.com/docs/setup/linux |
| Python setup | https://docs.python.org/3/using/index.html |
| curl project | https://curl.se/ |
| Homebrew | https://brew.sh/ |
| GitHub account | https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github |
| GitHub PAT | https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens |
| Docker Desktop Mac | https://docs.docker.com/desktop/setup/install/mac-install/ |
| Docker Desktop Linux | https://docs.docker.com/desktop/setup/install/linux/ |
| Docker Engine Ubuntu | https://docs.docker.com/engine/install/ubuntu/ |
| Docker Engine Linux post-install | https://docs.docker.com/engine/install/linux-postinstall/ |
| Docker Compose | https://docs.docker.com/compose/ |
