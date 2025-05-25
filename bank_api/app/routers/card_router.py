from fastapi import APIRouter, HTTPException
from ..schemas import *
from typing import List
from ..models import *
from ..database import db_dependency

router=APIRouter(
    prefix='/cards',
    tags=['Cards']
)

@router.get('/{user_uuid}',response_model=List[CardRead])
async def get_user_cards(db:db_dependency,user_uuid:str):
    user_cards=db.query(Cards).filter(Cards.user_uuid==user_uuid).all()
    if not user_cards:
        raise HTTPException(status_code=404,detail="User dont have cards")
    return user_cards
    
@router.post('/{user_uuid}')
async def add_card(db:db_dependency,user_uuid:str):
    user_cards=db.query(Cards).filter(Cards.user_uuid==user_uuid).all()
    if len(user_cards)>=3:
        raise HTTPException(status_code=400,detail='Sorry you cant have more then 3 cards')
    user_card=CardPost(
        user_uuid=user_uuid,   
        card_sum=float(100000)
    )
    db_card=Cards(**user_card.model_dump())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)

@router.patch('/{card_uuid}',response_model=CardUpdate)
async def update_sum(db:db_dependency,card_uuid:str,new_card_sum):
    db_card=db.query(Cards).filter(Cards.card_uuid==card_uuid).first()
    if not db_card:
        raise HTTPException(status_code=404,detail="Such card dont found")
    db_card.card_sum=new_card_sum
    db.commit()
    db.refresh(db_card)
    return db_card

@router.delete('/{card_uuid}')
async def delete_card(db:db_dependency,card_uuid:str):
    db_card=db.query(Cards).filter(Cards.card_uuid==card_uuid).first()
    if not db_card:
        raise HTTPException(status_code=404,detail="Card not found")
    user_deposits=db.query(Deposits).filter(Deposits.card_uuid==card_uuid).all()
    user_credits=db.query(Credits).filter(Credits.card_uuid==card_uuid).all()
    if (len(user_deposits)!=0)|(len(user_credits)!=0):
        raise HTTPException(status_code=400,detail="Card cant be deleted because its currently used for deposits or credits")
    db.delete(db_card)
    db.commit()
    return "Card deleted succesfully"
    