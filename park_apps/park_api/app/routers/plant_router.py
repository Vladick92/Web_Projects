from fastapi import APIRouter,HTTPException
from typing import List
from ..models.plant import Plants
from ..database import db_dependency
from ..schemas.plant_schema import *

router=APIRouter(tags=['Plants'],prefix='/plant')

@router.get('/',response_model=List[PlantRead])
async def get_all_plants(db:db_dependency):
    db_plants=db.query(Plants).all()
    if not db_plants:
        raise HTTPException(status_code=404,detail='Plants not found')
    return [PlantRead.model_validate(elem) for elem in db_plants]

@router.post('/')
async def add_plant(db:db_dependency,plant_name:str,plant_status:str):
    db_plant=Plants(plant_name=plant_name,plant_status=plant_status)
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)

@router.put('/{plant_uuid}')
async def edit_plant(db:db_dependency,new_name:str,new_status:str,plant_uuid:str):
    db_plant=db.query(Plants).filter(Plants.plant_uuid==plant_uuid).first()
    if not db_plant:
        raise HTTPException(status_code=404,detail='plant not found')
    db_plant.plant_name=new_name
    db_plant.plant_status=new_status
    db.commit()
    db.refresh(db_plant)

@router.delete('/{plant_uuid}')
async def delete_plant(db:db_dependency,plant_uuid:str):
    db_plant=db.query(Plants).filter(Plants.plant_uuid==plant_uuid).first()
    if not db_plant:
        raise HTTPException(status_code=404,detail='plant not found')
    db.delete(db_plant)
    db.commit()