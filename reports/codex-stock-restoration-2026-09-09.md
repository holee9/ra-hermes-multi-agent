# Codex 순정 설정 복구 보고서

## 결과와 적용 범위

Codex CLI 0.153.4의 로컬 사용자 설정을 설치된 버전의 내장 기본값으로 복구했다. 사용자 설정 파일과 명령 규칙 파일은 그대로 유지하고, 원본을 별도 보관한 상태에서 사용자 재정의가 없는 내용으로 정상화했다. 설정 로더에서 확인되는 사용자 설정 항목은 13개에서 0개, 저장된 명령 허용 규칙은 258개에서 0개가 됐다.

검사 기준일은 2026년 9월 9일이며, 대상 프로젝트는 `/home/abyz-lab/work/workspace-github/holee9/ra-hermes-multi-agent`다. 실제 변경 파일은 사용자 공용 경로인 `~/.codex/config.toml`과 `~/.codex/rules/default.rules`다. 따라서 이 사용자 계정으로 시작하는 다른 Codex 프로젝트에도 기본값 복구가 적용된다.

로그인 정보, 대화 기록, 상태 데이터베이스, 기본 제공 스킬, 계정에 연결된 원격 플러그인, Claude/MoAI 설정, RA/Hermes 애플리케이션 코드는 보존했다. 이번 결과는 **로컬 Codex 사용자 설정의 순정 복구**이며, 로그인 전의 새 계정 상태나 플러그인이 하나도 없는 계정으로 초기화한 것은 아니다.

## 순정의 판단 기준

OpenAI 공식 문서는 실행 옵션, 프로젝트 설정, 선택한 프로필, 사용자 설정, 시스템 설정, 내장 기본값의 순서로 설정을 해석한다고 설명한다. 따라서 특정 모델명이나 예제의 모든 값을 새로 고정하기보다, 사용자 재정의가 없는 상태에서 설치된 Codex가 기본값을 결정하게 하는 것이 버전별 기본 동작을 보존한다.[^1]

공식 예제 설정도 필요한 항목만 선택해 사용하도록 안내하며, 예제 전체가 그대로 설치 초기 상태를 뜻하지는 않는다. 기본 지침 파일의 강제 교체, 개발자 지침 추가, 압축 프롬프트 교체 등은 선택 설정이다. 이 항목을 새로 만들거나 타 도구의 지침 파일로 연결하지 않았다.[^2]

순정 복구는 모든 승인과 제한을 해제하는 설정과도 다르다. 공식 기본 승인 정책은 `on-request`이며, 기본 샌드박스는 `read-only`다. 복구 검증에서 실제 CLI의 승인 정책과 새 입력의 샌드박스가 이 상태임을 확인했다.[^2]

## 조사 결과

| 조사 대상 | 확인 결과 | 처리 |
| --- | --- | --- |
| Codex 버전 | `codex-cli 0.153.4`, npm 설치 | 동일 버전을 기준으로 검사 |
| 사용자 `config.toml` | 사용자 원점으로 식별된 설정 13개 | 내장 기본값 사용 상태로 복구 |
| 사용자 `rules/default.rules` | 258개 모두 `allow`, `prompt`와 `forbidden`은 0개 | 저장된 예외가 없는 기본 상태로 복구 |
| 프로젝트 `AGENTS.md`, `AGENTS.override.md` | 프로젝트 트리에서 발견되지 않음 | 새로 만들지 않음 |
| 사용자 전역 AGENTS 파일 | 발견되지 않음 | 변경 없음 |
| 프로젝트 `.codex`, `.agents` | 발견되지 않음 | 변경 없음 |
| 상위 경로 추가 설정 | 조사한 상위 경로에서 추가 Codex 설정·스킬 경로 없음 | 변경 없음 |
| 시스템 `/etc/codex` | 디렉터리 없음, 로더의 시스템 계층은 빈 객체 | 변경 없음 |
| 관리자 요구사항 | `configRequirements/read`의 `requirements: null` | 변경 없음 |
| 별도 사용자 프로필 | 추가 프로필 TOML 없음 | 변경 없음 |
| 지침 교체 설정 | `developer_instructions`, `model_instructions_file`, `compact_prompt` 등 미설정 | 기본 지침 유지 |
| 대체 지침 파일명 | `project_doc_fallback_filenames: []` | 기본 발견 규칙 유지 |
| Codex MCP 서버 | 로컬 설정 0개 | 변경 없음 |
| Codex 훅 | 로더에서 `hooks: null` | 변경 없음 |
| 기본 로컬 스킬 | 시스템 범위 6개, 로딩 오류 없음 | 유지 |
| 메모리 | 메모리 파일 디렉터리는 비어 있고 기능 플래그는 기본 비활성 | 데이터베이스 유지 |
| 셸 시작 설정 | 조사한 셸 설정에 Codex 커스텀 실행 설정 검색 결과 없음 | 변경 없음 |
| Git 훅 | `core.hooksPath` 설정 없음, `.git/hooks`는 sample 파일 | 변경 없음 |
| Claude/MoAI | 별도의 프로젝트 지침·권한·훅·스킬이 존재 | Codex 설정으로 취급하지 않고 보존 |

Codex의 지침 발견은 전역 및 프로젝트의 `AGENTS.override.md`, `AGENTS.md`, 명시적으로 설정한 대체 파일명을 따른다. 이 환경에서는 `CLAUDE.md`를 대체 지침으로 지정하지 않았으며, 새 Codex 입력에서도 Claude/MoAI 지침이 발견되지 않았다. 따라서 해당 파일을 바꾸는 것은 확인된 Codex 복구 대상에 해당하지 않는다.[^3]

## 실제 복구 내용

### 사용자 설정

`/home/abyz-lab/.codex/config.toml`의 원본은 `config.toml.original`로 보관했다. 현재 파일은 다음 주석만 포함하며, 유효 TOML 설정 항목은 없다.

```toml
# No user overrides. Use the installed Codex built-in defaults.
```

| 항목 | 복구 전 | 복구 후 | 실제 의미 |
| --- | --- | --- | --- |
| 기본 모델 | `gpt-6-astra` 고정 | 미설정, 진단 출력 `<default>` | 설치 버전과 모델 카탈로그가 기본 모델을 선택 |
| 추론 강도 | `low` 고정 | 미설정 | 선택 모델의 기본값 사용 |
| 승인 검토 주체 | `user` 명시 | 미설정 | 기본값도 `user`이므로 이 항목 자체의 실질 동작은 동일 |
| 프로젝트 신뢰 3건 | 모두 `trusted` | 저장된 신뢰 항목 없음 | 다음 실행에서 초기 신뢰 확인이 다시 필요할 수 있음 |
| 모델 안내 UI 기록 2건 | 기존 안내 상태 저장 | 기본 상태 | 안내 표시 상태 초기화, 모델 사용 권한에는 영향 없음 |
| 로컬 플러그인 지정 2건 | Figma/GitHub `enabled = true` | 로컬 지정 없음 | 로컬 강제 지정 초기화, 원격 계정 설치 상태는 유지 |
| GitHub 도구 승인 3건 | 도구별 `approval_mode = "approve"` | 도구별 재정의 없음 | 기본 앱·호스트 승인 동작 사용 |

신뢰 기록 3건은 `/home/abyz-lab/work`, `ra-med-bot`, `ra-hermes-multi-agent`다. 로컬 플러그인 키는 `figma@openai-curated`와 `github@openai-curated`였다. GitHub 승인 재정의가 있던 도구는 `github_add_comment_to_issue`, `github_create_issue`, `github_update_issue`다.

모델 기본값을 특정 모델명으로 단정하지 않는다. 복구 후 `config/read`는 모델과 추론 강도를 `null`로 반환하고, `doctor`는 모델을 `<default>`로 표시한다. 이는 사용자 고정값이 없어졌다는 증거이며, 실제 대화의 모델은 새 실행 시 계정 가용 모델과 실행 옵션에 따라 결정된다.

### 명령 규칙

`/home/abyz-lab/.codex/rules/default.rules`의 원본은 `default.rules.original`로 보관했다. 현재 파일은 다음 주석만 포함한다.

```text
# No saved user command rules. Use the built-in approval policy.
```

기존 258개 규칙은 모두 추가 자동 허용 예외였다. 실행을 금지하는 규칙이 있었다는 증거는 없었다. 복구는 이 예외 목록을 기본 상태로 되돌린 것이며, Codex 자체의 승인 정책이나 기본 안전 동작을 없앤 것이 아니다.

OpenAI 문서에 따르면 이 파일에는 사용자가 승인 과정에서 저장한 명령 접두사 예외가 누적되며, 활성 설정 계층의 `rules/`가 시작 시 읽힌다. 기본 예외가 없는 상태를 확인하기 위해 파일 내용과 `codex execpolicy check`를 함께 검사했다.[^4]

## 검증

진단에는 모델에게 실제 작업을 시키는 대신 설치된 CLI의 설정 해석, 스킬 목록, 규칙 검사, 입력 렌더링 기능을 사용했다. 별도 앱 서버 프로세스에서 `config/read`와 `configRequirements/read`를 호출해 디스크에 적용된 계층을 확인했고, 검사 프로세스는 종료했다. 공식 앱 서버 문서는 `config/read`를 계층 해석 후 설정 조회 기능으로 정의한다.[^5]

| 검증 | 결과 |
| --- | --- |
| 사용자 설정 원점 수 | 13 → 0 |
| 로더의 사용자 계층 | `{}` |
| 로더의 시스템 계층 | `{}` |
| 관리자 요구사항 | `null` |
| 저장된 명령 규칙 수 | 258 → 0 |
| 규칙 검사 | `git status`에 대한 `matchedRules: []` |
| 엄격한 설정 검사 | `--strict-config doctor` 및 앱 서버 설정 로딩 성공 |
| 전체 진단 | 20개 항목 모두 `ok` |
| 실제 승인 정책 | `OnRequest` |
| 새 입력의 샌드박스 | `read-only`, 네트워크 제한 |
| 새 입력의 MoAI/Claude 지침 | 검색 결과 없음 |
| 새 입력의 프로젝트 AGENTS 지침 블록 | 검색 결과 없음 |
| 기본 스킬 | 복구 전후 목록 동일, 오류 없음 |
| 원격 플러그인 | 복구 전후 목록 동일 |
| 로그인 정보 | `auth.json`의 복구 전후 SHA-256 동일 |

`config/read`의 `null`은 해당 선택 설정이 명시되지 않았다는 뜻이다. 이를 기능이 전부 꺼졌다는 뜻으로 해석하지 않고, 실제 기본 동작은 `doctor`와 새 입력 렌더링으로 별도 확인했다.

기본 로컬 스킬 6개는 `imagegen`, `openai-docs`, `plugin-creator`, `review-agent`, `skill-creator`, `skill-installer`다. 로더가 모두 `system` 범위로 보고했으며 기존 항목을 보존했다. 공식 문서도 로컬 사용자·프로젝트 스킬과 Codex 번들 시스템 스킬을 구분한다.[^6]

### 배포 원본 무결성

OpenAI가 npm에 배포한 `@openai/codex@0.153.4`와 `@openai/codex@0.153.4-linux-x64`를 다운로드했다. 먼저 각 압축 파일의 SHA-512가 npm 레지스트리 메타데이터의 `dist.integrity`와 일치하는지 검사한 다음, 압축 파일 안의 각 파일과 설치된 대응 파일의 SHA-256을 비교했다.[^8]

런처 패키지 3개 파일과 Linux 패키지 8개 파일, 총 11개 모두 동일했다. Codex 실행 파일, 코드 실행 호스트, 검색 도구, 샌드박스 보조 프로그램, 번들 셸도 포함된다. 따라서 검사한 설치 파일에서 변조나 손상 증거는 없으며, 프로그램 교체나 버전 변경 없이 설정만 복구했다. 이 검사는 패키지 파일의 바이트 일치를 확인한 것이며 계정 서버의 모델이나 실행 중인 호스트 전체를 검사한 것은 아니다.

| 검증 대상 | 결과 |
| --- | --- |
| 다운로드 패키지 2개의 SHA-512 | 모두 레지스트리 무결성 값과 동일 |
| 설치 파일 11개의 SHA-256 | 모두 배포 원본과 동일 |
| Codex 실행 파일 SHA-256 | `56ef98ab4032d317ab26e9b5e5a175650717351edb16ed9cde0cb6d1734d62da` |
| 최종 복구 검증 | `validation.json`: 17개 모두 통과 |

## 원격 구성과 세션 경계

`codex plugin list --json`은 다음 계정 플러그인을 복구 전후 동일하게 반환했다. 이 결과는 단순히 로컬 캐시 디렉터리 존재 여부로 추정한 것이 아니다.

| 원격 플러그인 | 설치 정책 | 복구 후 |
| --- | --- | --- |
| `plugin-management` | `INSTALLED_BY_DEFAULT` | 유지 |
| `openai-templates` | `INSTALLED_BY_DEFAULT` | 유지 |
| `deep-research-work` | `INSTALLED_BY_DEFAULT` | 유지 |
| `gmail` | `AVAILABLE`, 계정에 설치됨 | 유지 |
| `github` | `AVAILABLE`, 계정에 설치됨 | 유지 |
| `figma` | `AVAILABLE`, 계정에 설치됨 | 유지 |

Gmail/GitHub/Figma를 기본 설치 플러그인으로 분류하지 않는다. 계정의 선택 설치 상태는 보존했으며, 로컬 설정 복구가 이 연결들을 해제했다는 주장도 하지 않는다. 공식 문서에서도 플러그인 설치, 워크스페이스 기본 플러그인, 외부 서비스 연결은 별도 범위로 설명한다.[^7]

현재 열려 있는 대화에는 이미 읽힌 지침과 호스트가 제공한 실행 설정이 남아 있다. 디스크 설정 변경만으로 실행 중인 대화의 과거 입력이나 호스트 설정이 소급 교체되지는 않는다. **복구된 로컬 기본값은 별도 옵션 없이 새로 시작하는 Codex 세션에서 사용해야 한다.** 기존 대화 재개나 앱이 전달하는 모델·권한 옵션은 기본값보다 우선할 수 있다.[^1][^3]

이는 승인 제한을 우회하는 설정을 새로 추가해야 한다는 뜻이 아니다. 이번 복구는 `never`, 전체 파일 접근, 커스텀 개발자 지침, 대체 시스템 프롬프트를 추가하지 않은 상태다.

## 백업과 증거

원본과 검증 자료는 저장소 밖의 다음 디렉터리에 보관되어 있다. 디렉터리 권한은 `0700`이며 로그인 토큰 원문은 백업 자료에 복사하지 않았다.

```text
/home/abyz-lab/.local/state/codex-restores/20260909T041535Z/
```

| 파일 | 내용 |
| --- | --- |
| `config.toml.original` | 복구 전 설정 원본 |
| `default.rules.original` | 복구 전 258개 규칙 원본 |
| `before-inventory.json`, `after-inventory.json` | 크기, 해시, 규칙 개수 |
| `before-config.json`, `after-config.json` | 설정 원점과 계층의 실제 조회 결과 |
| `before-requirements.json`, `after-requirements.json` | 관리자 요구사항 조회 결과 |
| `before-doctor.json`, `after-doctor.json` | CLI 진단 원문 |
| `before-skills.json`, `after-skills.json` | 로컬 스킬과 범위 |
| `before-plugins.json`, `after-plugins.json` | 계정 원격 플러그인 상태 |
| `after-prompt-input.json` | 새 CLI 입력 렌더링 결과 |
| `installation-verification.json` | 두 패키지의 무결성과 11개 설치 파일의 해시 비교 |
| `validation.json` | 최종 복구 검증 17개 항목의 통과 결과 |
| `audit.mjs`, `capture-prompt.mjs` | 동일 검사를 수행하는 스크립트 |
| `verify-install.mjs` | 배포 패키지와 설치 파일의 무결성 비교 |
| `validate-restoration.mjs` | 복구 상태와 보존 항목의 검증 |

원래 개인 설정으로 되돌릴 필요가 생기면 두 `.original` 파일을 대응하는 원래 경로로 복원하면 된다. 이는 이번 순정 복구를 취소하는 동작이다. 원본 백업과 복구 전 해시의 일치도 별도로 검사했다.

## 출처

공식 문서는 조사일에 열람한 현행 문서다. 문서와 설치 버전의 표현이 다를 수 있는 항목은 설치된 0.153.4의 실제 출력으로 보완했다. 로컬 측정값은 위 증거 디렉터리에서 재검토할 수 있다.

[^1]: OpenAI, [Config basics](https://learn.chatgpt.com/docs/config-file/config-basic), 설정 계층 및 우선순위, 2026-09-09 열람.
[^2]: OpenAI, [Sample Configuration](https://learn.chatgpt.com/docs/config-file/config-sample), 선택 설정, 기본 승인·샌드박스, 지침 재정의, 2026-09-09 열람.
[^3]: OpenAI, [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), 지침 발견 규칙 및 새 세션 반영, 2026-09-09 열람.
[^4]: OpenAI, [Rules](https://learn.chatgpt.com/docs/agent-configuration/rules), 규칙 저장·로딩·검사, 2026-09-09 열람.
[^5]: OpenAI, [Codex App Server](https://learn.chatgpt.com/docs/app-server), 초기화 및 `config/read`, 2026-09-09 열람.
[^6]: OpenAI, [Build skills](https://learn.chatgpt.com/docs/build-skills), 시스템·사용자·프로젝트 스킬 범위, 2026-09-09 열람.
[^7]: OpenAI, [Plugins](https://learn.chatgpt.com/docs/plugins), 설치·기본 플러그인·외부 연결의 구분, 2026-09-09 열람.
[^8]: OpenAI npm 배포, [Codex 0.153.4 메타데이터](https://registry.npmjs.org/@openai/codex/0.153.4), [Linux x64 0.153.4 메타데이터](https://registry.npmjs.org/@openai/codex/0.153.4-linux-x64), `dist.integrity`와 해당 `dist.tarball`의 실제 파일, 2026-09-09 조회·검증.
