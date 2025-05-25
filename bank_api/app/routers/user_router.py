from fastapi import APIRouter, HTTPException
from ..schemas import *
from typing import List
from ..models import *
from ..database import db_dependency

router=APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('/',response_model=List[UserRead])
async def get_all_users(db:db_dependency):
    db_users=db.query(Users).all()
    if not db_users:
        raise HTTPException(status_code=404,detail='Users not found')
    return db_users

@router.get('/{user_uuid}',response_model=UserRead)
async def get_user_data(db:db_dependency,user_uuid:str):
    db_user=db.query(Users).filter(Users.user_uuid==user_uuid).first()
    if not db_user:
        raise HTTPException(status_code=404,detail='User with such uuid not found')
    return db_user

@router.put('/{user_uuid}',response_model=UserRead)
async def update_user(db:db_dependency,user_data:UserBase,user_uuid:str):
    db_user=db.query(Users).filter(Users.user_uuid==user_uuid).first()
    if not db_user:
        raise HTTPException(status_code=404,detail='User not found')
    db_user.user_name=user_data.user_name
    db_user.user_surname=user_data.user_surname
    db_user.user_password=user_data.user_password
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete('/{user_uuid}')
async def delete_user(db:db_dependency,user_uuid):
    db_user=db.query(Users).filter(Users.user_uuid==user_uuid).first()
    if not db_user:
        raise HTTPException(status_code=404,detail='User to delete not found')
    db.delete(db_user)
    db.commit()
    return f'User with uuid: {user_uuid} deleted'