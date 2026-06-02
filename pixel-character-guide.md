# 픽셀아트 캐릭터 제작 가이드 (가상 오피스용)

> 결정: **PixelLab(AI 생성) + Piskel(무료 브라우저 보정)** 조합.
> 이유: 사용자가 직접 그리지 않으므로 AI 생성이 현실적. PixelLab은 한 방향 캐릭터에서 나머지 방향을 자동 생성 → 오피스에서 캐릭터가 걸어가 쪽지 전달하는 측면 동작에 필요. Piskel은 설치 없이 색을 우리 팔레트에 맞춰 보정.
> (피그마는 벡터 UI 도구라 픽셀아트 부적합 — 제외.)

---

## 제작 규격 (8명 공통)

- 크기: **32×32 px** (오피스 캐릭터 라벨에 적정)
- 뷰: 정면 기준 (PixelLab 방향 자동 생성으로 측면 추가 가능)
- 배경: **투명 PNG**
- 팔레트: 아래 16색 레트로 톤(아티팩트와 동일)으로 통일
  - 배경 `#1a1c2c`, 피부 `#f4d29c`, 외곽선 `#1a1c2c`
  - 강조색은 캐릭터별 지정(아래 표)
- 프레임: 정지 1프레임이면 충분(우리 시스템은 "일 있을 때만 잠깐 움직임" — 복잡한 걷기 애니 불필요). 여유 있으면 2프레임(정지/말하기)만.

---

## 8명 생성 프롬프트 (PixelLab에 그대로 입력)

각 프롬프트 앞에 공통 접두사를 붙인다:
`32x32 pixel art character, front view, retro 16-color palette, dark outline #1a1c2c, transparent background, simple office worker, upper body, sitting-ready pose —`

| ID | 이름 | 강조색 | 프롬프트 본문 |
|---|---|---|---|
| ra_us | Mike | `#41a6f6` | confident professional in a **blue** shirt, neat short hair, calm sharp expression (US regulatory expert) |
| ra_eu | Theo | `#ffcd75` | meticulous professional in a **mustard/gold** shirt, glasses, composed serious look (EU regulatory expert) |
| ra_kr | Sam | `#ef7d57` | approachable professional in a **coral/orange** shirt, friendly attentive face (Korea regulatory expert) |
| op_manager | Margot | `#a7f070` | organized coordinator in a **green** blouse, tidy hair, focused look holding a clipboard (project manager) |
| n8n_manager | Olly | `#b8b5ff` | tinkerer engineer in a **lavender** hoodie, headphones, curious expression (automation engineer) |
| infra_t3610 | Finn | `#73eff7` | steady technician in a **cyan** jumpsuit, cap, reliable calm face (infrastructure ops) |
| infra_gx10 | Leo | `#94b0c2` | sturdy technician in a **steel-gray** jumpsuit, short beard, watchful face (infrastructure ops) |
| infra_rpi | Gus | `#f4d29c` | small wiry technician in a **tan** jumpsuit, goggles on forehead, alert face (infrastructure ops) |

> 톤 통일 포인트: 8명 모두 같은 화풍·같은 외곽선·같은 크기. 강조색만 다르게 해서 한눈에 구분되되 한 팀으로 보이게.
> 업무팀(Mike/Theo/Sam/Margot/Olly)과 인프라팀(Finn/Leo/Gus)을 복장으로 구분 — 업무팀은 셔츠/블라우스, 인프라팀은 점프수트.

---

## 제작 → 오피스 적용 절차

1. PixelLab에서 위 8개 프롬프트로 캐릭터 생성(무료 티어로 8명 커버). 필요시 방향(측면) 자동 생성.
2. Piskel(piskelapp.com, 브라우저)에서 색을 위 팔레트로 미세 보정, 32×32로 정리.
3. 투명 PNG로 export. 파일명을 ID와 맞춤: `mike.png, theo.png, sam.png, margot.png, olly.png, finn.png, leo.png, gus.png`.
4. 가상 오피스 아티팩트(virtual-office.html)의 `CHARS` 매핑에서 각 캐릭터에 `sprite:"경로/파일.png"` 추가.
   - 아티팩트는 이미 sprite 경로가 있으면 PNG를, 없으면 기존 도형을 그리도록 개조됨 → 8명 다 준비 안 돼도 일부만 PNG로 교체 가능.

---

## 대안 (참고)

- 완전 무료·무제한·통제 우선 → **Pixelorama**(브라우저도 됨, 레이어·애니 지원) 또는 **Piskel** 단독으로 직접 제작.
- Aseprite 워크플로우 무료 → **LibreSprite**.
- $20 일회 업계 표준 → **Aseprite**(소스 컴파일 시 무료).
- 위는 모두 직접 그리는 도구. 사용자가 그림에 익숙하지 않으면 PixelLab 생성 경로가 가장 빠름.

---

## 권장: 기성 CC0 에셋 (그림·툴 학습 불필요)

코드로 찍은 기본 캐릭터는 임시값. 고급스럽게 하려면 **Kenney CC0 캐릭터**를 받아 교체. CC0이라 출처 표기 의무도 없음(상업 사용 자유).

### 1) 다운로드 위치

- 사이트: **kenney.nl** → Assets → 캐릭터 팩
- 추천 팩(우리 탑다운 오피스에 적합):
  - **Mini Characters** — https://kenney.nl/assets/mini-characters (작은 탑다운 캐릭터, 오피스에 적합)
  - **Animated Characters 1** — https://kenney.nl/assets/animated-characters-1 (동작 프레임 포함)
- 받는 법: 페이지에서 **"Continue without donating"** 클릭 → zip 무료 다운로드(기부는 선택).
- zip 안에 PNG 캐릭터 스프라이트들이 들어있음. 8명에 가장 가까운 것 선택(업무팀=셔츠/정장, 인프라팀=작업복 느낌).

### 2) 파일 넣을 위치 (배포 구조 기준)

가상 오피스는 Docker 웹앱으로 배포 예정. 레포/컨테이너 구조:

```
virtual-office/
├─ index.html              # 가상 오피스 (현 virtual-office.html)
├─ assets/
│  └─ characters/          # ← 여기에 받은 PNG를 둔다
│     ├─ mike.png
│     ├─ theo.png
│     ├─ sam.png
│     ├─ margot.png
│     ├─ olly.png
│     ├─ finn.png
│     ├─ leo.png
│     └─ gus.png
├─ Dockerfile
└─ CREDITS.txt             # CC0이라 의무 아니지만 출처 기록 권장
```

- 파일명을 위처럼 **애칭과 맞춤**(또는 actor ID와 맞춤). 캐릭터당 정지 1프레임 PNG면 충분.

### 3) 코드에 연결 (한 줄씩)

`index.html`의 `CHARS`에서 각 캐릭터에 `sprite` 경로 추가:

```js
const CHARS = {
  ra_us:     {name:"Mike", role:"미국RA", room:"work", x:70, y:150, color:"#41a6f6",
              sprite:"assets/characters/mike.png"},   // ← 이 줄 추가
  ra_eu:     {name:"Theo", ... , sprite:"assets/characters/theo.png"},
  // ... 8명 동일하게
};
```

- 렌더링은 이미 **PNG 우선(1순위)** → 픽셀 canvas(2순위) → 도형(3순위)로 짜여 있음.
- `sprite` 경로를 넣은 캐릭터만 PNG로 교체됨 → **8명 한꺼번에 안 해도 됨**, 받은 것부터 하나씩 교체.
- actor ID·이벤트 로직·뼈대 연동 무영향. **그림만 갈아끼움.**

### 4) 순서 주의

- 지금 아티팩트 미리보기에서는 외부 PNG 경로 접근이 제한될 수 있음 → 진짜 PNG 연동은 **Docker 배포 단계**에서 적용하는 게 맞음.
- 그 전까지는 코드로 찍은 기본 캐릭터(현재 32×32)가 임시 기본값으로 동작.

