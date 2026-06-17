# GIS Insight Viewer 프로젝트 가이드

이 문서는 GIS Insight Viewer 프로젝트의 설정, 데이터베이스 구축 및 애플리케이션 실행 방법을 설명합니다.

---

## 1. 전제 조건

- **Python 3.10+**
- **Node.js 18+** (npm 포함)
- **PostgreSQL 14+** (PostGIS 확장 설치 필수)

---

## 2. 데이터베이스 설정

PostgreSQL에 접속하여 다음 절차를 수행합니다.

1. `postgres` 데이터베이스에 접속합니다. (또는 별도의 DB 생성 가능하나, 현재 설정은 `postgres`를 사용하도록 최적화되어 있습니다.)
2. `project/backend/init_db.sql` 파일을 실행하여 테이블과 인덱스를 생성합니다.

```sql
-- 테이블 생성 및 PostGIS 활성화
-- psql -U postgres -d postgres -f project/backend/init_db.sql
```

---

## 3. 백엔드 설정 및 실행 (FastAPI)

1. **의존성 설치**:
   ```bash
   cd project/backend
   pip install -r requirements.txt
   ```

2. **환경 설정**:
   `project/backend/app/core/config.py` 파일에서 `DATABASE_URL`을 본인의 환경에 맞게 수정합니다.
   *현재 설정: `postgresql://postgres:1234@127.0.0.1:5432/postgres?client_encoding=utf8`*

3. **서버 실행**:
   Windows 환경에서는 인코딩 문제를 방지하기 위해 다음 명령어를 사용합니다.
   ```powershell
   $env:PGCLIENTENCODING='UTF8'
   python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
   ```

---

## 4. 프론트엔드 설정 및 실행 (React + Vite)

1. **의존성 설치**:
   ```bash
   cd project/frontend
   npm install
   ```

2. **서버 실행**:
   ```bash
   npm run dev
   ```
   실행 후 터미널에 표시되는 주소(보통 `http://localhost:5173`)로 접속합니다.

---

## 5. 주요 기능 사용법

1. **GeoJSON 업로드**:
   - 화면 좌측 상단의 업로드 영역에 GeoJSON 파일을 드래그 앤 드롭하거나 클릭하여 선택합니다.
   - 프로젝트 루트에 포함된 `seoul_landmarks.geojson` 파일을 테스트용으로 사용할 수 있습니다.
2. **지도 시각화**:
   - 업로드된 데이터가 지도 위에 자동으로 렌더링됩니다.
3. **분석 결과 확인**:
   - 좌측 사이드바에서 각 객체별 면적(㎡ 및 평)을 확인할 수 있습니다.
   - 지도 위의 객체를 클릭하면 우측 하단 패널에 상세 속성 정보가 표시됩니다.

---

## 6. 주의 사항

- **CORS 및 Proxy**: 프론트엔드의 `vite.config.ts`에 백엔드(`:8000`)로의 프록시 설정이 포함되어 있습니다.
- **데이터베이스 인코딩**: Windows에서 PostgreSQL 연결 시 인코딩 에러가 발생하면 반드시 `PGCLIENTENCODING` 환경 변수를 `UTF8`로 설정하세요.
