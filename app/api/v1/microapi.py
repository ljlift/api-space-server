from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from app import schema, crud
from sqlalchemy.orm import Session
from app.api.deps import get_db

router = APIRouter(prefix="/microapi")


@router.get("", response_model=schema.MicroAPIResponse)
def get(*, db: Session = Depends(get_db), microapi_in: schema.MicroAPIGet) -> Any:
    microapi = crud.microapi.get_by_filter(db, microapi_in.name, microapi_in.space_name)
    return microapi


@router.post("", response_model=schema.MicroAPIResponse)
def create(*, db: Session = Depends(get_db), microapi_in: schema.MicroAPICreate) -> Any:
    microapi = crud.microapi.get_by_filter(db, name=microapi_in.name, space_name=microapi_in.space_name)
    if microapi is None:
        microapi = crud.microapi.create(db, obj_in=microapi_in)
    else:
        microapi = crud.microapi.update(db, db_obj=microapi, obj_in=microapi_in)
    return microapi


@router.put("", response_model=schema.MicroAPIResponse)
def update(*, db: Session = Depends(get_db), microapi_in: schema.MicroAPIUpdate) -> Any:
    microapi = crud.microapi.get_by_filter(db, name=microapi_in.name, space_name=microapi_in.space_name)
    if microapi is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The microapi is not found"
        )
    
    microapi = crud.microapi.update(db, db_obj=microapi, obj_in=microapi_in)
    return microapi

