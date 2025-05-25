from sqlalchemy import Column, String,ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text

class Tasks(Base):
    __tablename__='tasks'
    task_uuid=Column(UUID(as_uuid=True),primary_key=True,unique=True,index=True,server_default=text('gen_random_uuid()'))
    task_giver=Column(UUID(as_uuid=True),ForeignKey('owners.owner_uuid'),index=True,nullable=False)
    task_receiver=Column(UUID(as_uuid=True),ForeignKey('rangers.ranger_uuid'),index=True,nullable=False)
    task_target=Column(UUID(as_uuid=True),ForeignKey('plants.plant_uuid'),index=True,nullable=False)
    task_status=Column(String,index=True,nullable=False)
    task_message_to_owner=Column(String,index=True)
    task_message_to_ranger=Column(String,index=True)
    task_to_owner=relationship('Owners',back_populates='owner_to_task')
    task_to_ranger=relationship('Rangers',back_populates='ranger_to_task')
    task_to_plant=relationship('Plants',back_populates='plant_to_task')
