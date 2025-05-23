from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
