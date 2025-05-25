from pydantic import BaseModel
from uuid import UUID

class RangerBase(BaseModel):
    ranger_name:str

    class Config():
        from_attributes=True

class RangerRead(RangerBase):
    ranger_uuid:UUID