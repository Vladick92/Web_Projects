from fastapi import APIRouter,HTTPException
from ..schemas import *
from typing import List
from .. import models
from ..database import db_dependency
from uuid import UUID

router=APIRouter(
    prefix='/todo',
    tags=['Todos']
)


@router.get('/gettodos',response_model=List[TodoRead])
async def get_todos(user_uuid: UUID,db:db_dependency):
    user_todos=db.query(models.Todo_items).filter(models.Todo_items.user_uuid==user_uuid).all()
    if not user_todos:
        raise HTTPException(status_code=404,detail="Todos not found")
    return user_todos

@router.post('/addtodo')
async def post_todo(elemToAdd:TodoCreate,db:db_dependency):
    db_todo=models.Todo_items(**elemToAdd.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

@router.delete('/removetodo')
async def remove_todo(todo_uuid:str,db:db_dependency):
    toDelete=db.query(models.Todo_items).filter(models.Todo_items.todo_uuid==todo_uuid).first()
    if not toDelete:
        raise HTTPException(status_code=404,detail="Todo not found")
    db.delete(toDelete)
    db.commit()

@router.patch("/edittodo")
async def edit_todo(elemToUpdate:TodoEdit,db:db_dependency):    
    db_elem=db.query(models.Todo_items).filter(models.Todo_items.todo_uuid==elemToUpdate.todo_uuid).first()
    if not db_elem:
        raise HTTPException(status_code=404,detail="Todo not found")
    db_elem.todo_name=elemToUpdate.todo_name
    db_elem.todo_diff=elemToUpdate.todo_diff
    db_elem.todo_urge=elemToUpdate.todo_urge
    db_elem.todo_desc=elemToUpdate.todo_desc
    db_elem.due_date=elemToUpdate.due_date
    db.commit()
    db.refresh(db_elem)
