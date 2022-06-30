from lib2to3.pgen2.token import OP
from typing import Optional
from pydantic import BaseModel


class MicroAPIBase(BaseModel):
    name: Optional[str]
    space_name: Optional[str]
    uri: Optional[str]


class MicroAPICreate(MicroAPIBase):
    name: str
    space_name: str
    uri: str


class MicroAPIUpdate(MicroAPICreate):
    pass


class MicroAPIGet(MicroAPIBase):
    name: str
    space_name: str


class MicroAPIResponse(MicroAPIBase):
    class Config:
        orm_mode = True


