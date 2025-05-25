from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class DepositBase(BaseModel):
    user_uuid: UUID
    card_uuid: UUID
    deposit_sum: int
    deposit_rate: float
    deposit_start_date: datetime
    deposit_end_date: datetime
    deposit_can_terminate: bool
    deposit_send_to: str
    deposit_status: str='Approved'

    class Config():
        orm_mode=True

class DepositRead(DepositBase):
    deposit_uuid: UUID

class DepositPost(DepositBase):
    pass

class DepositUpdate(DepositRead):
    pass

class DepositDelete(DepositRead):
    pass