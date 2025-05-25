from sqlalchemy import Column, String,ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text

class Bankers(Base):
    __tablename__='bankers'
    banker_uuid=Column(UUID(as_uuid=True),primary_key=True,index=True,server_default=text('gen_random_uuid()'))
    banker_user_uuid=Column(UUID(as_uuid=True),ForeignKey('users.user_uuid'),nullable=True,index=True)
    banker_to_user=relationship('Users',back_populates='user_to_banker')
    banker_to_credit=relationship('Credits',back_populates='credit_to_banker')
