from typing import Any, List
from fastapi import APIRouter
from app.schema.ping import PingResponse


router = APIRouter(prefix="/ping")


@router.get("", response_model=PingResponse)
def ping() -> Any:
    return {"msg": "pong"}
