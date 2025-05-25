from fastapi import APIRouter,HTTPException
from typing import List
from .task import Tasks
from .database import db_dependency
from .task_schema import *

router=APIRouter(tags=['Tasks'],prefix='/task')

@router.get('/',response_model=List[TaskRead])
async def get_all_tasks(db:db_dependency):
    db_tasks=db.query(Tasks).all()
    if not db_tasks:
        raise HTTPException(status_code=404,detail='tasks not found')
    return db_tasks

@router.post('/')
async def add_task(db:db_dependency,task_to_add:TaskPost):
    db_task=Tasks(**task_to_add.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

@router.put('/{task_uuid}')
async def edit_task(db:db_dependency,task_uuid:str,task_status:str,message:str):
    db_task=db.query(Tasks).filter(Tasks.task_uuid==task_uuid).first()
    if not db_task:
        raise HTTPException(status_code=404,detail='No such task')
    db_task.task_status=task_status
    db_task.task_message_to_owner=message
    db.commit()
    db.refresh(db_task)

@router.get('/ranger_tasks/{ranger_uuid}',response_model=List[TaskReadRanger])
async def get_ranger_task(db:db_dependency,ranger_uuid):
    ranger_tasks=db.query(Tasks).filter(Tasks.task_receiver==ranger_uuid,Tasks.task_status=='Waiting').all()
    if not ranger_tasks:
        raise HTTPException(status_code=404,detail='Ranger dont have tasks to do')
    return [TaskReadRanger.model_validate(elem) for elem in ranger_tasks]

@router.get('/owner_tasks/{owner_uuid}',response_model=List[TaskReadOwner])
async def get_owner_tasks(db:db_dependency,owner_uuid:str):
    owner_tasks=db.query(Tasks).filter(Tasks.task_giver==owner_uuid,Tasks.task_status=='Completed').all()
    if not owner_tasks:
        raise HTTPException(status_code=404,detail='Owner dont have tasks')
    return [TaskReadOwner.model_validate(elem) for elem in owner_tasks]

@router.delete('/{task_uuid}')
async def delete_task(db:db_dependency,task_uuid:str):
    db_task=db.query(Tasks).filter(Tasks.task_uuid==task_uuid).first()
    if not db_task:
        raise HTTPException(status_code=404,detail='Task not found')
    db.delete(db_task)
    db.commit()