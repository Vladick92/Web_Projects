from fastapi import APIRouter,HTTPException
from typing import List
from ..models.owner import Owners
from ..database import db_dependency
from ..schemas.owner_schema import *

router=APIRouter(tags=['Owner'],prefix='/owner')

@router.get('/',response_model=List[OwnerRead])
async def get_all_owners(db:db_dependency):
    db_owners=db.query(Owners).all()
    if not db_owners:
        raise HTTPException(status_code=404,detail='Owners not found')
    return [OwnerRead.model_validate(elem) for elem in db_owners]

@router.post('/')
async def add_owner(db:db_dependency,owner_name:str):
    db_owner=Owners(owner_name=owner_name)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)

@router.put('/{owner_uuid}')
async def edit_owner(db:db_dependency,new_name:str,owner_uuid:str):
    db_owner=db.query(Owners).filter(Owners.owner_uuid==owner_uuid).first()
    if not db_owner:
        raise HTTPException(status_code=404,detail='Owner not found')
    db_owner.owner_name=new_name
    db.commit()
    db.refresh(db_owner)

@router.delete('/{owner_uuid}')
async def delete_owner(db:db_dependency,owner_uuid:str):
    db_owner=db.query(Owners).filter(Owners.owner_uuid==owner_uuid).first()
    if not db_owner:
        raise HTTPException(status_code=404,detail='Owner not found')
    db.delete(db_owner)
    db.commit()