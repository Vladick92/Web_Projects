from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text

class Rangers(Base):
    __tablename__='rangers'
    ranger_uuid=Column(UUID(as_uuid=True),primary_key=True,unique=True,index=True,server_default=text('gen_random_uuid()'))
    ranger_name=Column(String,unique=False,nullable=False)