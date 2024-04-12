from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = 'mariadb+pymysql://root:password@192.168.0.2:3306/inst'

base = declarative_base()
 
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False, pool_pre_ping=True, pool_recycle=3600)
session_maker = sessionmaker(bind=engine, autocommit=False, autoflush=False)
 
 
def get_db():
    with session_maker() as session:
        yield session