from pydantic import BaseModel
from uuid import UUID

class PlantBase(BaseModel):
    plant_name:str
    plant_status:str

    class Config():
        from_attributes=True

class PlantRead(PlantBase):
    plant_uuid:UUID