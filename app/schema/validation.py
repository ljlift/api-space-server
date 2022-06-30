from typing import Optional
from pydantic import BaseModel


class ValidationBase(BaseModel):
    uri: Optional[str]
    spec: Optional[dict]

class ValidationPost(ValidationBase):
    uri: str
    spec: dict

class ValidationResponse(BaseModel):
    result: str