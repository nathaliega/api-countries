from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "postgresql://nathalie:krystian@localhost/fastapi_db"

SQLALCHEMY_DATABASE_URL = "postgresql://nathalie:krystian@192.168.40.113/fastapi_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
