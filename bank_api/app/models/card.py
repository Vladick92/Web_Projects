from sqlalchemy import Column, String,ForeignKey,Float
from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text

class Cards(Base):
    __tablename__='cards'
    card_uuid=Column(UUID(as_uuid=True),primary_key=True,index=True,server_default=text('gen_random_uuid()'))
    user_uuid=Column(UUID(as_uuid=True),ForeignKey("users.user_uuid"),index=True,nullable=False)
    card_sum=Column(Float,index=True)
    card_to_user=relationship('Users',back_populates='user_to_cards')
    card_to_credit=relationship('Credits',back_populates='credit_to_card')
    card_to_deposit=relationship('Deposits',back_populates='deposit_to_card')

