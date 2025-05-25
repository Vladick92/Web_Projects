from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class CreditBase(BaseModel):
    user_uuid: UUID
    card_uuid: UUID
    banker_uuid: Optional[UUID]=None
    secured_by: Optional[UUID]=None 
    credit_sum: int
    credit_paid_sum: int
    credit_rate: float
    open_credits: bool
    credit_purpose: str
    credit_start_date: datetime
    credit_end_date: datetime
    credit_status: str= "Waiting"

    class Config():
        orm_mode=True

class CreditRead(CreditBase):
    credit_uuid: UUID

class CreditPost(CreditBase):
    pass

class CreditUpdate(BaseModel):
    credit_uuid: UUID
    sum_to_pay: int

    class Config():
        orm_mode=True