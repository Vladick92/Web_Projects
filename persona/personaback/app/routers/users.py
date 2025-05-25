from fastapi import APIRouter,HTTPException
from ..schemas import *
from typing import List
from .. import models
from ..database import db_dependency

router=APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.get("/check")
async def check_username(nameToCheck:str,db:db_dependency):
    is_found=db.query(models.Users).filter(models.Users.username==nameToCheck).first()
    if is_found:
        return "Username alredy taken"
    else:
        return None


@router.get("/all",response_model=List[UserRead])
async def get_all_users(db:db_dependency):
    db_users=db.query(models.Users).all()
    if not db_users:
        raise HTTPException(status_code=404,detail="Users not found")
    users=[UserRead(
        user_uuid=user.user_uuid,
        username=user.username,
        user_pass=user.user_pass,
        email=user.email,
    ) for user in db_users]
    return users

@router.get('/log',response_model=UserRead)
async def log_user(username: str,password:str,db:db_dependency):
    user=db.query(models.Users).filter(models.Users.username==username).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    if user.user_pass!=password:
        raise HTTPException(status_code=400,detail="Wrong password")
    return UserRead(user_uuid=user.user_uuid,username=user.username,user_pass=user.user_pass,email=user.email)


@router.post('/sign',response_model=UserBase)
async def sign_user(userToAdd:UserBase,db:db_dependency):
    res=db.query(models.Users).filter(models.Users.username==userToAdd.username).first()
    if not res:
        db_user=models.Users(
            username=userToAdd.username,
            user_pass=userToAdd.user_pass,
            email=userToAdd.email
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return UserBase(
            username=db_user.username,
            user_pass=db_user.user_pass,
            email=db_user.email
        )
    else:
        raise HTTPException(status_code=400,detail="There is already such username")
