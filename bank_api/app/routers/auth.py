from fastapi import APIRouter, HTTPException
from ..schemas import *
from ..models import *
from ..database import db_dependency

router=APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post('/log_in',response_model=UserRead)
async def log_in_user(db:db_dependency,user_to_log:UserBase):
    db_user=db.query(Users).filter(
        Users.user_name==user_to_log.user_name,
        Users.user_surname==user_to_log.user_surname,
        Users.user_password==user_to_log.user_password,
        Users.user_email==user_to_log.user_email).first()
    if not db_user:
        raise HTTPException(status_code=404,detail='Some fields are wrong, try again')
    return db_user

@router.post('/sign_in',response_model=UserRead)
async def sing_in_user(db:db_dependency,user_to_sign:UserPost):
    exist_user=db.query(Users).filter(Users.user_email==user_to_sign.user_email).first()
    if exist_user:
        raise HTTPException(status_code=400,detail='User with this email aready exists, try other one')
    db_user=Users(**user_to_sign.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post('/submit_password/{user_uuid}')
async def submit_password(db:db_dependency,password_to_check:str,user_uuid:str):
    db_user=db.query(Users).filter(Users.user_uuid==user_uuid).first()
    if not db_user:
        raise HTTPException(status_code=404,detail='User not found')
    return db_user.user_password==password_to_check
