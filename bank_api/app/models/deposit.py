from sqlalchemy import Column, String,ForeignKey,Float,DateTime,Boolean
from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text

class Deposits(Base):
    __tablename__='deposits'
    deposit_uuid=Column(UUID(as_uuid=True),primary_key=True,index=True,server_default=text('gen_random_uuid()'))
    user_uuid=Column(UUID(as_uuid=True),ForeignKey('users.user_uuid'),index=True,nullable=False)
    card_uuid=Column(UUID(as_uuid=True),ForeignKey('cards.card_uuid'),index=True,nullable=False)
    deposit_sum=Column(Float,index=True,nullable=False)
    deposit_rate=Column(Float,index=True,nullable=False)
    deposit_start_date=Column(DateTime,index=True,nullable=False)
    deposit_end_date=Column(DateTime,index=True,nullable=False)
    deposit_can_terminate=Column(Boolean,index=True,nullable=False)
    deposit_send_to=Column(String,index=True,nullable=False)
    deposit_status=Column(String,index=True,nullable=False) 
    deposit_to_user=relationship('Users',back_populates='user_to_deposits')
    deposit_to_card=relationship('Cards',back_populates='card_to_deposit')