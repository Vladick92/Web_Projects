from pydantic import BaseModel
from uuid import UUID

class CardBase(BaseModel):
    user_uuid:UUID
    card_sum: int

    class Config():
        orm_mode=True

class CardRead(CardBase):
    card_uuid: UUID

class CardPost(CardBase):
    pass

class CardUpdate(CardRead):
    card_uuid: UUID
    card_sum: float

    class Config():
        orm_mode=True