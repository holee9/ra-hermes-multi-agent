-- pgvector 임베딩 차원 설정: GX10 4096차원
-- Honcho 기본값(1536)을 4096으로 오버라이드
-- docker-compose postgres 볼륨 마운트로 첫 초기화 시 실행됨
-- 마운트: ./init-vector-dim.sql:/docker-entrypoint-initdb.d/01-vector-dim.sql:ro

CREATE EXTENSION IF NOT EXISTS vector;

-- Honcho가 생성하는 embeddings 테이블의 vector 컬럼 차원을 4096으로 설정
-- Honcho가 자체 마이그레이션으로 테이블을 생성하므로,
-- 실제 컬럼 생성 전 아래 GUC 변수로 차원을 주입하거나
-- Honcho의 EMBEDDING_DIM 환경변수를 지원하는지 확인 필요.
--
-- ✅ Honcho v0.0.x 이상: 환경변수 EMBEDDING_DIM=4096 설정으로 처리 가능
-- ✅ 확인 방법: docker exec honcho-api-1 env | grep EMBEDDING
--
-- Honcho가 EMBEDDING_DIM을 지원하지 않을 경우:
-- Honcho 마이그레이션 실행 후 수동으로 컬럼 재생성:
--   ALTER TABLE messages ALTER COLUMN embedding TYPE vector(4096);
--   ALTER TABLE metamessages ALTER COLUMN embedding TYPE vector(4096);
