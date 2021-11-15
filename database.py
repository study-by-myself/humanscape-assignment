from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#데이터베이스 URL 생성 
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

#SQLALCHEMY engine 생성 코넥트알규는 sqlalchemy만 필요함 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
#실제 데이터베이스 session임 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()