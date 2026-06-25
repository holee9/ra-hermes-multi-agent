# GLM-5.2 설정 조사 및 적용 메모

기준일: 2026-06-18

## 현재 장비 상태

- 현재 호스트: T3610 (`abyz-lab-Precision-T3610`)
- 역할: Honcho 서버 + Hermes 에이전트 실행
- 메모리/디스크: RAM 60GiB, 루트 디스크 440G 중 335G 여유
- 로컬 Ollama: `localhost:11434` 응답 없음
- GX10 추론 엔드포인트: `http://192.168.100.1:11434/v1`
- GX10 현재 모델: `gpt-oss:120b`, `qwen3-embedding:latest`

판정: GLM-5.2 원본 로컬 서빙은 현재 운영 경로로 두지 않는다. Z.ai 공식 GLM-5.2는 744B-A40B급 모델이며, T3610에는 로컬 추론 서버가 없고 GX10에는 GLM 모델이 올라와 있지 않다. 1차 적용 경로는 Z.ai 또는 GLM을 제공하는 OpenAI-compatible API다.

## 공식 API 요약

- 일반 API base URL: `https://api.z.ai/api/paas/v4`
- GLM Coding Plan 전용 base URL: `https://api.z.ai/api/coding/paas/v4`
- 모델 ID: `glm-5.2`
- GLM-5.2 context: 1,000,000 tokens
- 최대 출력: 128K tokens
- 기능: streaming, thinking mode, function calling, structured output, context caching, MCP

일반 애플리케이션/서버 호출은 일반 API endpoint를 우선 사용한다. Coding Plan 전용 endpoint는 지원 도구용으로 분리되어 있으므로 Hermes가 해당 플랜에서 정상 동작하는지는 계정 권한으로 별도 smoke test가 필요하다.

## Hermes 프로파일 전환

현재 Hermes 프로파일은 모두 다음 형태다.

```yaml
memory:
  provider: honcho
model:
  default: gpt-oss:120b
  provider: custom
  base_url: http://192.168.100.1:11434/v1
```

GLM-5.2로 바꾸려면:

```bash
export ZAI_API_KEY="..."
bash scripts/configure-glm.sh
export OPENAI_API_KEY="${ZAI_API_KEY}"
```

키를 각 로컬 프로파일 config에 저장해도 되는 운영 환경이면:

```bash
export ZAI_API_KEY="..."
WRITE_API_KEY=1 bash scripts/configure-glm.sh
```

Coding Plan endpoint를 쓸 때:

```bash
export ZAI_API_KEY="..."
GLM_BASE_URL=https://api.z.ai/api/coding/paas/v4 bash scripts/configure-glm.sh
export OPENAI_API_KEY="${ZAI_API_KEY}"
```

특정 프로파일만 전환:

```bash
PROFILES="ra-us ra-eu ra-kr" bash scripts/configure-glm.sh
```

GX10으로 되돌릴 때:

```bash
MODEL_DEFAULT=gpt-oss:120b \
MODEL_BASE_URL=http://192.168.100.1:11434/v1 \
bash profiles/setup.sh
```

## Claude Code CLI 상태

현재 장비에는 Claude Code CLI `2.1.181`이 설치되어 있다.

```bash
claude --version
# 2.1.181 (Claude Code)
```

Z.ai 공식 Claude Code 연동은 OpenAI-compatible endpoint가 아니라 Anthropic-compatible endpoint를 사용한다.

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "your_zai_api_key",
    "ANTHROPIC_BASE_URL": "https://api.z.ai/api/anthropic",
    "API_TIMEOUT_MS": "3000000"
  }
}
```

현재 `~/.claude/settings.json`에는 위 GLM 라우팅 env가 들어 있지 않다. 따라서 `claude` 기본 명령은 GLM으로 강제 라우팅되지 않는다.

대신 로컬에 `/home/abyz-lab/.local/bin/glm` wrapper가 존재한다. 이 wrapper는 `~/.config/glm-claude-code/env`에서 `ZAI_API_KEY`를 읽고, 실행 시 다음 값을 설정한 뒤 Claude Code를 호출한다.

```bash
ANTHROPIC_AUTH_TOKEN=<ZAI_API_KEY>
ANTHROPIC_BASE_URL=https://api.z.ai/api/anthropic
API_TIMEOUT_MS=3000000
```

현재 `~/.config/glm-claude-code/env`에는 `ZAI_API_KEY`가 존재한다. 모델 override는 주석 처리되어 있어, 기본적으로 Z.ai 서버측 mapping을 따른다.

현재 `/home/abyz-lab/.local/bin/glm` wrapper는 명령 인자로 모델 선택을 지원한다.

2026-06-24 실제 Z.ai Anthropic-compatible endpoint smoke test 기준:

- `glm-5.1` 요청: HTTP 200, 응답 `model`은 `glm-5.2`로 서버측 매핑
- `glm-5.2`: HTTP 200
- `glm-5.2[1m]`: HTTP 400 `Unknown Model`

따라서 현재 장비 설정은 명시 모델명을 `glm-5.2`로 고정하고, Claude Code compact window는 `GLM_AUTO_COMPACT_WINDOW=1000000`으로 별도 지정한다.

```bash
glm                 # Z.ai server-side default mapping
glm 5.2             # glm-5.2
glm 4.7             # glm-4.7
glm 5-turbo         # glm-5-turbo
glm 5.1             # glm-5.1
glm 4.5-air         # glm-4.5-air
glm models          # wrapper alias 목록
```

나머지 인자는 Claude Code로 그대로 전달된다.

```bash
glm 5.2 -p "review this repo"
glm 4.7 --continue
```

GLM-5.2 1M context를 Claude Code에서 명시하려면 Z.ai 공식 모델명은 `glm-5.2`로 두고, compact window만 wrapper env에 별도 지정한다.

```json
{
  "env": {
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.5-air",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.2",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.2",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000"
  }
}
```

현재 운영상 더 안전한 사용법은 기본 `claude`는 그대로 두고, GLM이 필요할 때 `glm` 명령을 쓰는 것이다. 이 방식은 Anthropic 기본 세션과 Z.ai GLM 세션을 명령 단위로 분리한다.

## Honcho 설정

Honcho deriver/dialectic/summary/dream 모델도 OpenAI-compatible 설정 패턴을 그대로 따른다.

```env
GX10_MODEL=glm-5.2
GX10_BASE_URL=https://api.z.ai/api/paas/v4
DERIVER_MODEL_CONFIG__MODEL=${GX10_MODEL}
DERIVER_MODEL_CONFIG__OVERRIDES__BASE_URL=${GX10_BASE_URL}
DERIVER_MODEL_CONFIG__OVERRIDES__API_KEY=${ZAI_API_KEY}
```

임베딩은 GLM-5.2로 바꾸지 않는다. 기존 `qwen3-embedding:latest`와 pgvector 4096차원 계약을 유지한다.

## 직접 API smoke test

키가 있을 때:

```bash
curl -sS https://api.z.ai/api/paas/v4/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${ZAI_API_KEY}" \
  -d '{
    "model": "glm-5.2",
    "messages": [{"role": "user", "content": "Reply with GLM-5.2 OK only."}],
    "max_tokens": 32
  }'
```

Hermes smoke test:

```bash
export OPENAI_API_KEY="${ZAI_API_KEY}"
HERMES_HOME="${HOME}/.hermes/profiles/ra-us" \
  /home/abyz-lab/.hermes/hermes-agent/venv/bin/hermes -m glm-5.2 --provider custom -z "Reply GLM-5.2 OK only."
```

## 참고 자료

- Z.ai GLM-5.2 docs: https://docs.z.ai/guides/llm/glm-5.2
- Z.ai Quick Start: https://docs.z.ai/guides/overview/quick-start
- Z.ai OpenAI SDK guide: https://docs.z.ai/guides/develop/openai/python
- Z.ai tool integration: https://docs.z.ai/devpack/tool/others
- GLM-5 GitHub README: https://github.com/zai-org/GLM-5
