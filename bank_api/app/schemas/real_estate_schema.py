from pydantic import BaseModel
from uuid import UUID

class RealEstateBase(BaseModel):
    user_uuid: UUID
    real_estate_type: str
    real_estate_price: int
    real_estate_constr: str
    real_estate_units: str

    class Config():
        orm_mode=True

class RealEstateRead(RealEstateBase):
    real_estate_uuid: UUID

class RealEstatePost(RealEstateBase):
    pass

class RealEstateUpdate(BaseModel):
    real_estate_type: str
    real_estate_price: int
    real_estate_constr: str
    real_estate_units: str

    class Config():
        orm_mode=True