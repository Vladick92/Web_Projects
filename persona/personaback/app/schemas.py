from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class UserBase(BaseModel):
    username: str
    user_pass: str
    email: str

    class Config():
        orm_mode=True

class UserRead(UserBase):
    user_uuid: UUID

class TodoBase(BaseModel):
    todo_name: str
    todo_desc: Optional[str]=None
    todo_urge: Optional[str]=None
    todo_diff: Optional[str]=None
    creation_date: datetime
    due_date: Optional[datetime]=None

    class Config():
        orm_mode=True

class TodoCreate(TodoBase):
    user_uuid: UUID

class TodoRead(TodoBase):
    todo_uuid:UUID

class TodoEdit(TodoBase):
    user_uuid: UUID
    todo_uuid:UUID


class BookBase(BaseModel):
    book_name:str
    book_author:Optional[str]=None
    book_desc:Optional[str]=None

    class Config():
        orm_mode=True

class BookCreate(BookBase):
    user_uuid:UUID

class BookRead(BookBase):
    book_uuid: UUID

class BookEdit(BookBase):
    user_uuid:UUID
    book_uuid:UUID

class CategBase(BaseModel):
    cat_name: str

    class Config():
        orm_mode=True

class CategCreate(CategBase):
    user_uuid:UUID

class CategRead(CategBase):
    cat_uuid:UUID

class CategEdit(CategBase):
    user_uuid:UUID
    cat_uuid:UUID

class ItemBase(BaseModel):
    item_name: str
    item_quantity: int
    item_price: int

    class Config():
        orm_mode=True

class ItemCreate(ItemBase):
    cat_uuid: UUID

class ItemRead(ItemBase):
    item_uuid:UUID

class ItemEdit(ItemBase):
    cat_uuid:UUID
    item_uuid:UUID