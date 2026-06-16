from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator
from app.core.config import settings

# SQLAlchemy 엔진 생성
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# 세션 팩토리 설정
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모델 베이스 클래스
Base = declarative_base()

def get_db() -> Generator:
    """
    데이터베이스 세션을 생성하고 반환하는 의존성 주입용 함수
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()