from sqlalchemy import Column, String,ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text

class Users(Base):
    __tablename__='users'
    user_uuid=Column(UUID(as_uuid=True),primary_key=True,index=True,server_default=text('gen_random_uuid()'))
    user_name=Column(String,nullable=False)
    user_surname=Column(String,nullable=False)
    user_password=Column(String,nullable=False)
    user_email=Column(String,nullable=False,unique=True)
    user_to_cards=relationship('Cards',back_populates='card_to_user')
    user_to_real_estates=relationship('Real_estates',back_populates='real_estate_to_user') 
    user_to_banker=relationship('Bankers',back_populates='banker_to_user')
    user_to_deposits=relationship('Deposits',back_populates='deposit_to_user')
    user_to_credits=relationship('Credits',back_populates='credit_to_user')


