from pydantic import BaseModel
from uuid import UUID

class OwnerBase(BaseModel):
    owner_name:str

    class Config():
        from_attributes=True

class OwnerRead(OwnerBase):
    owner_uuid:UUID