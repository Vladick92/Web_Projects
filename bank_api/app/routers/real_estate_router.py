from fastapi import APIRouter, HTTPException
from ..schemas import *
from typing import List
from ..models import *
from ..database import db_dependency

router=APIRouter(
    prefix='/real_estate',
    tags=['Real estate']
)

@router.get('/{user_uuid}',response_model=List[RealEstateRead])
async def get_user_homes(db:db_dependency,user_uuid):
    db_homes=db.query(Real_estates).filter(Real_estates.user_uuid==user_uuid).all()
    if not db_homes:
        raise HTTPException(status_code=404,detail="User dont have homes")
    return db_homes

@router.post('/',response_model=RealEstateRead)
async def add_user_home(db:db_dependency,home_to_add:RealEstatePost):
    db_home=Real_estates(**home_to_add.model_dump())
    db.add(db_home)
    db.commit()
    db.refresh(db_home)
    return db_home

@router.delete('/{home_uuid}')
async def delete_home(db:db_dependency,home_uuid:str):
    db_home=db.query(Real_estates).filter(Real_estates.real_estate_uuid==home_uuid).first()
    if not db_home:
        raise HTTPException(status_code=404,detail="Home not found")
    db.delete(db_home)
    db.commit()
    return 'Home deleted'

@router.put('/{home_uuid}',response_model=RealEstateUpdate)
async def edit_home(db:db_dependency,home_uuid:str,home_to_edit:RealEstateUpdate):
    db_home=db.query(Real_estates).filter(Real_estates.real_estate_uuid==home_uuid).first()
    if not db_home:
        raise HTTPException(status_code=404,detail="Home not found")
    db_home.real_estate_constr=home_to_edit.real_estate_constr
    db_home.real_estate_type=home_to_edit.real_estate_type
    db_home.real_estate_price=home_to_edit.real_estate_price
    db_home.real_estate_units=home_to_edit.real_estate_units
    db.commit()
    db.refresh(db_home)
    return db_home