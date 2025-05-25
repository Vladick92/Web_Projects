from fastapi import APIRouter,HTTPException
from ..schemas import *
from typing import List
from .. import models
from ..database import db_dependency
from uuid import UUID

router=APIRouter(
    prefix='/item',
    tags=['Items']
)


@router.get('/get',response_model=List[ItemRead])
async def get_items(cat_uuid:UUID,db:db_dependency):
    db_items=db.query(models.Items).filter(models.Items.cat_uuid==cat_uuid).all()
    if not db_items:
        raise HTTPException(status_code=404,detail="Items not found")
    return db_items

@router.post('/post')
async def add_item(elemToAdd:ItemCreate,db:db_dependency):
    db_item=models.Items(**elemToAdd.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

@router.delete('/remove')
async def remove_item(item_uuid:UUID,db:db_dependency):
    toDelete=db.query(models.Items).filter(models.Items.item_uuid==item_uuid).first()
    if not toDelete:
        raise HTTPException(status_code=404,detail="Item not found")
    db.delete(toDelete)
    db.commit()

@router.patch('/patch')
async def edit_item(elemToUpd:ItemEdit,db:db_dependency):
    db_item=db.query(models.Items).filter(models.Items.item_uuid==elemToUpd.item_uuid).first()
    if not db_item:
        raise HTTPException(status_code=404,detail="Categories not found")
    db.delete(db_item)
    upd_item=models.Items(
        item_uuid=elemToUpd.item_uuid,
        cat_uuid=elemToUpd.cat_uuid,
        item_name=elemToUpd.item_name,
        item_quantity=elemToUpd.item_quantity,
        item_price=elemToUpd.item_price
    )
    db.add(upd_item)
    db.commit()
    db.refresh(upd_item)
