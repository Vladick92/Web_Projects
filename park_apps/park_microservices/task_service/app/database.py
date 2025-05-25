from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from fastapi import Depends
import os

DB_URL=os.environ.get("DATABASE_URL",'db_address')
engine=create_engine(DB_URL)
LocalSession=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()

def get_DB():
    db=LocalSession()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_DB)]