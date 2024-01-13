from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost:3306/hishabproject"
engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()