from pydantic import BaseModel


class PingResponse(BaseModel):
    msg: str
