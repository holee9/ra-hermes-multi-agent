FROM node:20-alpine

WORKDIR /app

# virtual-office.html과 어댑터 서버 복사
COPY virtual-office.html ./
COPY virtual-office-honcho-adapter.js ./server.js

ENV PORT=3000
# DATA_SOURCE: mock (기본) | honcho (실데이터)
ENV DATA_SOURCE=mock
ENV HONCHO_API_URL=http://honcho-api:8000
ENV HONCHO_APP_NAME=work
ENV POLL_INTERVAL_MS=30000

EXPOSE 3000

# 읽기 전용 관찰자 — 쓰기 권한 없는 비루트 사용자로 실행
RUN adduser -D -u 1001 observer
USER observer

CMD ["node", "server.js"]
