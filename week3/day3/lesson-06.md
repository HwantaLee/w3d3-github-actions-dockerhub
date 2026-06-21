# 6교시: tag와 version 기준

## 수업 목표
- `tag와 version 기준`를 운영 시나리오와 연결해 설명한다.
- 명령 결과나 문서 증거를 기준으로 정상/비정상을 구분한다.
- 실패했을 때 다음에 볼 증거와 복구 기준을 말한다.

## 50분 흐름
| 시간 | 활동 | 학습 초점 | 학생 산출 |
|---|---|---|---|
| 0-5분 | 전 교시 연결 | 지금 보는 기능이 전체 운영 흐름에서 어디에 있는지 확인한다. | 오늘의 질문 |
| 5-15분 | 핵심 개념 | 용어를 명령/현상/운영 판단과 연결한다. | 용어 note |
| 15-30분 | 데모 또는 실습 | 실제 명령이나 GitHub 화면에서 evidence를 확인한다. | command/screen evidence |
| 30-42분 | 실패 케이스 | 흔한 실패 로그, 이벤트, 충돌, 상태를 읽는다. | failure note |
| 42-50분 | 정리 | 다음 교시 또는 Week 4로 넘길 기준을 작성한다. | handoff 문장 |

## 핵심 설명
app version, Git tag, Docker image tag, latest 사용 기준 evidence를 남기는 것이 이 교시의 핵심이다. 명령을 외우는 것보다 어떤 상태를 확인하려고 그 명령을 실행하는지 말할 수 있어야 한다.

## 실습 또는 데모 기준
자세한 명령은 [hands-on-lab.md](./hands-on-lab.md)를 따른다. 이 교시에서는 아래 세 가지를 반드시 구분한다.

| 구분 | 확인할 것 |
|---|---|
| 정상 상태 | 기대한 status, log, check, response가 무엇인지 |
| 실패 상태 | 어떤 메시지가 다음 행동의 힌트인지 |
| 복구 기준 | 수정 후 무엇을 다시 실행해야 하는지 |

## Evidence Note
```markdown
# Week 3 Day 3 Lesson 6 Evidence

## Topic
- Lesson: tag와 version 기준
- Goal:

## Observation
- Command or screen:
- Expected:
- Actual:

## Failure or risk
- Symptom:
- Evidence:
- Fix or next request:
```

## 평가 기준
| 기준 | 통과 조건 |
|---|---|
| 개념 이해 | 오늘 주제를 운영 판단과 연결했다. |
| 실행 증거 | 명령 결과나 화면 evidence를 남겼다. |
| 실패 분석 | 실패 메시지와 다음 행동을 연결했다. |
| 다음 연결 | 다음 교시 또는 Week 4 Kubernetes 확장 지점을 적었다. |
