from fastapi import APIRouter, HTTPException
from ..schemas import *
from typing import List
from ..models import *
from ..database import db_dependency

router=APIRouter(
    prefix='/bankers',
    tags=['Banker']
)

@router.get('/',response_model=List[BankerRead])
async def get_all_bankers(db:db_dependency):
    db_bankers=db.query(Bankers).all()
    if not db_bankers:
        raise HTTPException(status_code=404,detail='There is not bankers')
    return db_bankers

@router.get('/{banker_user_uuid}',response_model=BankerRead)
async def get_banker_uuid(db:db_dependency,banker_user_uuid:str):
    db_banker=db.query(Bankers).filter(Bankers.banker_user_uuid==banker_user_uuid).first()
    if not db_banker:
        raise HTTPException(status_code=200,detail='User is not banker')
    return db_banker

@router.post('/{banker_user_uuid}',response_model=BankerRead)
async def add_banker(db:db_dependency,banker_user_uuid:str):
    db_banker=db.query(Bankers).filter(Bankers.banker_user_uuid==banker_user_uuid).first()
    if db_banker:
        raise HTTPException(status_code=404,detail='User is already banker')
    db_banker=Bankers(banker_user_uuid=banker_user_uuid)
    db.add(db_banker)
    db.commit()
    db.refresh(db_banker)
    return db_banker