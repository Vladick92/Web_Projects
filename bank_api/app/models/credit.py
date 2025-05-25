from sqlalchemy import Column, String,ForeignKey,Float,DateTime,Boolean,Integer
from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text

class Credits(Base):
    __tablename__='credits'
    credit_uuid=Column(UUID(as_uuid=True),primary_key=True,index=True,server_default=text('gen_random_uuid()'))
    card_uuid=Column(UUID(as_uuid=True),ForeignKey('cards.card_uuid'),index=True,nullable=False)
    banker_uuid=Column(UUID(as_uuid=True),ForeignKey('bankers.banker_uuid'),index=True,nullable=True)
    secured_by =Column(UUID(as_uuid=True),ForeignKey('real_estates.real_estate_uuid'),index=True,nullable=True)
    user_uuid=Column(UUID(as_uuid=True),ForeignKey('users.user_uuid'),index=True,nullable=False)
    credit_sum=Column(Integer,index=True,nullable=False)
    credit_paid_sum=Column(Integer,index=True,nullable=False)
    credit_rate=Column(Float,index=True,nullable=False)
    open_credits=Column(Boolean,index=True,nullable=False)
    credit_purpose=Column(String,index=True,nullable=False)
    credit_start_date=Column(DateTime,index=True,nullable=False)
    credit_end_date=Column(DateTime,index=True,nullable=False)
    credit_status=Column(String,index=True,nullable=False)
    credit_to_card=relationship('Cards',back_populates='card_to_credit') 
    credit_to_real_estate=relationship('Real_estates',back_populates='real_estate_to_credit') 
    credit_to_banker=relationship('Bankers',back_populates='banker_to_credit') 
    credit_to_user=relationship('Users',back_populates='user_to_credits')   