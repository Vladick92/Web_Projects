from pydantic import BaseModel
from uuid import UUID

class BankerPost(BaseModel):
    banker_user_uuid:UUID

    class Config():
        orm_mode=True

class BankerRead(BankerPost):
    banker_uuid: UUID

class BankerUpdate(BankerRead):
    pass

class BankerDelete(BankerRead):
    pass