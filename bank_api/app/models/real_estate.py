from sqlalchemy import Column, String,ForeignKey,Float,Integer
from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text

class Real_estates(Base):
    __tablename__='real_estates'
    real_estate_uuid=Column(UUID(as_uuid=True),primary_key=True,index=True,server_default=text('gen_random_uuid()'))
    user_uuid=Column(UUID(as_uuid=True),ForeignKey('users.user_uuid'),index=True,nullable=False)
    real_estate_type=Column(String,index=True,nullable=False) 
    real_estate_price=Column(Integer,index=True,nullable=False)
    real_estate_constr=Column(String,index=True,nullable=False) 
    real_estate_units=Column(String,index=True,nullable=False)
    real_estate_to_user=relationship('Users',back_populates='user_to_real_estates')
    real_estate_to_credit=relationship('Credits',back_populates='credit_to_real_estate')

