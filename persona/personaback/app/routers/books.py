from fastapi import APIRouter,HTTPException
from ..schemas import *
from typing import List
from .. import models
from ..database import db_dependency

router=APIRouter(
    prefix='/book',
    tags=['Books']
)

@router.post('/addbook')
async def add_book(elemToAdd:BookCreate,db:db_dependency):
    db_book=models.Books(**elemToAdd.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

@router.get("/getbooks",response_model=List[BookRead])
async def get_books(user_uuid:str,db:db_dependency):
    db_books=db.query(models.Books).filter(models.Books.user_uuid==user_uuid).all()
    if not db_books:
        raise HTTPException(status_code=404,detail="Books not found")
    return db_books

@router.delete("/removebook")
async def remove_book(book_uuid:str,db:db_dependency):
    toDelete=db.query(models.Books).filter(models.Books.book_uuid==book_uuid).first()
    if not toDelete:
        raise HTTPException(status_code=404,detail="Book not found")
    db.delete(toDelete)
    db.commit()

@router.patch("books/editbook")
async def edit_book(elemToEdit:BookEdit,db:db_dependency):
    db_book=db.query(models.Books).filter(models.Books.book_uuid==elemToEdit.book_uuid).first()
    if not db_book:
        raise HTTPException(status_code=404,detail="Book not found")
    db_book.book_name=elemToEdit.book_name
    db_book.book_author=elemToEdit.book_author
    db_book.book_desc=elemToEdit.book_desc
    db.commit()
    db.refresh(db_book)
