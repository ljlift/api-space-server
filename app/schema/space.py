from typing import Optional
from pydantic import BaseModel


class SpaceBase(BaseModel):
    name: Optional[str]
    ruleset: Optional[dict]


class SpaceCreate(SpaceBase):
    name: str
    ruleset: dict


class SpaceUpdate(SpaceCreate):
    pass


class SpaceGet(SpaceBase):
    name: str


class SpaceResponse(SpaceBase):
    class Config:
        orm_mode = True


