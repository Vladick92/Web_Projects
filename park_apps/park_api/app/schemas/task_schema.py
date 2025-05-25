from pydantic import BaseModel
from uuid import UUID

class TaskBase(BaseModel):
    task_giver:UUID
    task_receiver:UUID
    task_status:str
    task_target:UUID

    class Config():
        from_attributes=True

class TaskRead(TaskBase):
    task_uuid:UUID

class TaskPost(TaskBase):
    task_message_to_ranger: str

class TaskReadOwner(TaskRead):
    task_message_to_owner: str


class TaskReadRanger(TaskRead):
    task_message_to_ranger: str
