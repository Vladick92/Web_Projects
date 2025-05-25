from fastapi import APIRouter,HTTPException
from ..schemas import *
from typing import List
from .. import models
from ..database import db_dependency

router=APIRouter(
    prefix="/categs",
    tags=['Categories']
)

@router.post('/addcat')
async def add_categ(elemToAdd:CategCreate,db:db_dependency):
    db_categ=models.Categories(**elemToAdd.model_dump())
    db.add(db_categ)
    db.commit()
    db.refresh(db_categ)

@router.get("/getcategs",response_model=List[CategRead])
async def get_categs(user_uuid:str,db:db_dependency):
    db_categs=db.query(models.Categories).filter(models.Categories.user_uuid==user_uuid).all()
    if not db_categs:
        raise HTTPException(status_code=404,detail="Categories not found")
    return db_categs

@router.delete('/removecateg')
async def remove_categ(categ_uuid:str,db:db_dependency):
    toDelete=db.query(models.Categories).filter(models.Categories.cat_uuid==categ_uuid).first()
    if not toDelete:
        raise HTTPException(status_code=404,detail="Categories not found")
    db.query(models.Items).filter(models.Items.cat_uuid==categ_uuid).delete()
    db.delete(toDelete)
    db.commit()

@router.patch("/editcateg")
async def edit_categ(elemToUpd:CategEdit,db:db_dependency):
    db_cat=db.query(models.Categories).filter(models.Categories.cat_uuid==elemToUpd.cat_uuid).first()
    if not db_cat:
        raise HTTPException(status_code=404,detail="Categories not found")
    db_cat.cat_name=elemToUpd.cat_name
    db.commit()
    db.refresh(db_cat)
