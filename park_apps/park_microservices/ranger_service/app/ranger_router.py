from fastapi import APIRouter,HTTPException
from typing import List
from .ranger import Rangers
from .database import db_dependency
from .ranger_schema import *

router=APIRouter(tags=['rangers'],prefix='/ranger')

@router.get('/',response_model=List[RangerRead])
async def get_all_rangers(db:db_dependency):
    db_rangers=db.query(Rangers).all()
    if not db_rangers:
        raise HTTPException(status_code=404,detail='rangers not found')
    return [RangerRead.model_validate(elem) for elem in db_rangers]

@router.post('/')
async def add_ranger(db:db_dependency,ranger_to_add:str):
    db_ranger=Rangers(ranger_name=ranger_to_add)
    db.add(db_ranger)
    db.commit()
    db.refresh(db_ranger)


@router.put('/{ranger_uuid}')
async def edit_ranger(db:db_dependency,ranger_uuid:str,new_ranger_name:str):
    db_ranger=db.query(Rangers).filter(Rangers.ranger_uuid==ranger_uuid).first()
    if not db_ranger:
        raise HTTPException(status_code=404,detail='ranger not found')
    db_ranger.ranger_name=new_ranger_name
    db.commit()
    db.refresh(db_ranger)


@router.delete('/{ranger_uuid}')
async def delete_ranger(db:db_dependency,ranger_uuid:str):
    db_ranger=db.query(Rangers).filter(Rangers.ranger_uuid==ranger_uuid).first()
    if not db_ranger:
        raise HTTPException(status_code=404,detail='ranger not found')
    db.delete(db_ranger)
    db.commit()
