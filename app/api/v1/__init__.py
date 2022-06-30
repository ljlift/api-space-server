from fastapi import APIRouter
from app.api.v1 import space
from app.api.v1 import validation
from app.api.v1 import microapi

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(space.router)
v1_router.include_router(validation.router)
v1_router.include_router(microapi.router)
