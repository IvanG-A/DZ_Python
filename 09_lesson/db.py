from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Строка подключения
DATABASE_URL = "postgresql://postgres:12345@localhost:5432/QA"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Создаём таблицы (если их нет)
Base.metadata.create_all(bind=engine)
