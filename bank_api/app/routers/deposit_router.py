from fastapi import APIRouter, HTTPException
from ..schemas import *
from typing import List
from ..models import *
from ..database import db_dependency

router=APIRouter(
    prefix='/deposits',
    tags=['Deposit']
)

@router.get('/{user_uuid}',response_model=List[DepositRead])
async def get_users_deposits(db:db_dependency,user_uuid:str):
    user_deposist=db.query(Deposits).filter(Deposits.user_uuid==user_uuid,Deposits.deposit_status!="terminated").all()
    if not user_deposist:
        raise HTTPException(status_code=404,detail="User dont have deposits")
    return user_deposist

@router.post('/',response_model=DepositRead)
async def add_deposit(db:db_dependency,deposit_to_add:DepositBase):
    db_card=db.query(Cards).filter(Cards.card_uuid==deposit_to_add.card_uuid).first()
    if not db_card:
        raise HTTPException(status_code=404,detail="There is not such cards")
    if db_card.user_uuid!=deposit_to_add.user_uuid:
        raise HTTPException(status_code=400,detail='User dont have access to this card')
    if db_card.card_sum<=deposit_to_add.deposit_sum:
        raise HTTPException(status_code=400,detail="Not enought money")
    db_card.card_sum-=deposit_to_add.deposit_sum
    db.commit()
    db.refresh(db_card)
    db_deposit=Deposits(**deposit_to_add.model_dump())
    db.add(db_deposit)
    db.commit()
    db.refresh(db_deposit)
    return db_deposit
    

@router.delete('/{deposit_uuid}')
async def terminate_deposit(db:db_dependency,deposit_uuid:str):
    db_deposit=db.query(Deposits).filter(Deposits.deposit_uuid==deposit_uuid).first()
    if not db_deposit:
        raise HTTPException(status_code=404,detail="There is not such deposit")
    db_card=db.query(Cards).filter(Cards.card_uuid==db_deposit.card_uuid).first()
    if not db_card:
        raise HTTPException(status_code=404,detail="There is not such cards")
    if db_card.user_uuid!=db_deposit.user_uuid:
        raise HTTPException(status_code=400,detail='User dont have access to this card')
    if db_deposit.deposit_can_terminate!=db_deposit.deposit_can_terminate:
        raise HTTPException(status_code=400,detail='Deposit cant be terminated')
    db_card.card_sum+=db_deposit.deposit_sum
    db.delete(db_deposit)
    db.commit()
    db.refresh(db_card)