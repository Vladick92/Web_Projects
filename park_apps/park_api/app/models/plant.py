from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text

class Plants(Base):
    __tablename__='plants'
    plant_uuid=Column(UUID(as_uuid=True),primary_key=True,unique=True,index=True,server_default=text('gen_random_uuid()'))
    plant_name=Column(String,unique=False,nullable=False)
    plant_status=Column(String,unique=False,nullable=True)
    plant_to_task=relationship("Tasks",back_populates='task_to_plant')