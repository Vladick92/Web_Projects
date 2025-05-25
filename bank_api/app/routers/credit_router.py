from fastapi import APIRouter, HTTPException
from ..schemas import *
from typing import List
from ..models import *
from ..database import db_dependency

router=APIRouter(
    prefix='/credits',
    tags=['Credit']
)

@router.get('/{user_uuid}',response_model=List[CreditRead])
async def get_user_credits(db:db_dependency,user_uuid:str):
    db_credits=db.query(Credits).filter(Credits.user_uuid==user_uuid,Credits.credit_status=="Approved").all()
    if not db_credits:
        raise HTTPException(status_code=404,detail='User dont have credits')
    return db_credits


@router.get('/to_approve/{banker_uuid}',response_model=List[CreditRead])
async def get_credits_to_approve(db:db_dependency,banker_uuid:str):
    user_banker=db.query(Bankers).filter(Bankers.banker_uuid==banker_uuid).first()
    credits_to_approve=db.query(Credits).filter(Credits.credit_status=="Waiting",Credits.banker_uuid!=user_banker.banker_user_uuid).all()
    return credits_to_approve

@router.post('/pay_for_credit/{credit_uuid}')
async def pay_for_credit(db:db_dependency,sum_to_pay:int,credit_uuid:str):
    db_credit=db.query(Credits).filter(Credits.credit_uuid==credit_uuid).first()
    if not db_credit:
        raise HTTPException(status_code=404,detail='credit not found')
    db_card=db.query(Cards).filter(Cards.card_uuid==db_credit.card_uuid).first()
    if not db_card:
        raise HTTPException(status_code=404,detail='card not found')
    if db_card.card_sum<sum_to_pay:
        raise HTTPException(status_code=400,detail='not enought money to pap for credit')
    if db_credit.credit_status=='Approved':
        db_credit.credit_paid_sum+=sum_to_pay
        db.commit()
        db.refresh(db_credit)
        db_card.card_sum-=sum_to_pay
        db.commit()
        db.refresh(db_card)
    if (db_credit.credit_status=='Approved')&(db_credit.credit_paid_sum>=db_credit.credit_sum):
        db_credit.credit_status='Completed'
        db.commit()
        db.refresh(db_credit)
    


@router.post('/',response_model=CreditRead)
async def add_credit(db:db_dependency,credit_to_add:CreditPost):
    db_card=db.query(Cards).filter(Cards.card_uuid==credit_to_add.card_uuid).first()
    if not db_card:
        raise HTTPException(status_code=404,detail="There is not such cards")
    if db_card.user_uuid!=credit_to_add.user_uuid:
        raise HTTPException(status_code=400,detail='User dont have access to this card')

    secured_by=None
    db_real_estate=db.query(Real_estates).filter(Real_estates.real_estate_uuid==credit_to_add.secured_by).first()
    if db_real_estate:
        if db_real_estate.user_uuid!=credit_to_add.user_uuid:
            raise HTTPException(status_code=400,detail='User dont have access to this property')
        secured_by=credit_to_add.secured_by

    credit_status=None
    if credit_to_add.banker_uuid==None:
        credit_status='Waiting'

    open_credits=False
    user_credits=db.query(Credits).filter(Credits.user_uuid==credit_to_add.user_uuid).all()
    if not user_credits:
        open_credits=False
    else:
        open_credits=True

    db_credit=Credits(
            user_uuid=credit_to_add.user_uuid,
            card_uuid=credit_to_add.card_uuid,
            credit_sum=credit_to_add.credit_sum,
            credit_paid_sum=0,
            credit_rate=credit_to_add.credit_rate,
            credit_purpose=credit_to_add.credit_purpose,
            credit_start_date=credit_to_add.credit_start_date,
            credit_end_date=credit_to_add.credit_end_date,
            secured_by=secured_by,
            credit_status=credit_status,
            open_credits=open_credits,
            banker_uuid=credit_to_add.banker_uuid
    )
    db.commit()
    db.refresh(db_card)
    db.add(db_credit)
    db.commit()
    db.refresh(db_credit)
    return db_credit


@router.post('/{credit_uuid}',response_model=CreditRead)
async def approve_credit(db:db_dependency,credit_uuid:str,banker_uuid:str):
    db_banker=db.query(Bankers).filter(Bankers.banker_uuid==banker_uuid).first()
    db_credit=db.query(Credits).filter(Credits.credit_uuid==credit_uuid).first()
    if not db_credit:
        raise HTTPException(status_code=404,detail='Credit not found')
    if db_banker.banker_user_uuid==db_credit.user_uuid:
        raise HTTPException(status_code=400,detail="Banker cant approve its onw credit")
    db_card=db.query(Cards).filter(Cards.card_uuid==db_credit.card_uuid).first()
    if not db_card:
        raise HTTPException(status_code=404,detail="card not found")
    db_credit.banker_uuid=db_credit.banker_uuid
    db_credit.credit_status='Approved'
    db.commit()
    db.refresh(db_credit)
    db_credit.banker_uuid=banker_uuid
    db.commit()
    db.refresh(db_credit)
    db_card.card_sum+=db_credit.credit_sum
    db.commit()
    db.refresh(db_card)
    return db_credit

