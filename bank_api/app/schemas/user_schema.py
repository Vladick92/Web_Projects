from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    user_name: str
    user_surname: str
    user_password: str
    user_email:str

    class Config():
        orm_mode=True

class UserRead(UserBase):
    user_uuid: UUID

class UserPost(UserBase):
    pass

class UserDelete(UserRead):
    pass