from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from app import schema, crud
from sqlalchemy.orm import Session
from app.api.deps import get_db

router = APIRouter(prefix="/space")


@router.get("", response_model=schema.SpaceResponse)
def get(*, db: Session = Depends(get_db), space_in: schema.SpaceGet) -> Any:
    space = crud.space.get_by_filter(db, space_in.name)
    return space


@router.post("", response_model=schema.SpaceResponse)
def create(*, db: Session = Depends(get_db), space_in: schema.SpaceCreate) -> Any:
    space = crud.space.get_by_filter(db, name=space_in.name)
    if space is None:
        space = crud.space.create(db, obj_in=space_in)
    else:
        space = crud.space.update(db, db_obj=space, obj_in=space_in)
    return space


@router.put("", response_model=schema.SpaceResponse)
def update(*, db: Session = Depends(get_db), space_in: schema.SpaceUpdate) -> Any:
    space = crud.space.get_by_filter(db, name=space_in.name)
    if space is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The space is not found"
        )
    
    space = crud.space.update(db, db_obj=space, obj_in=space_in)
    return space

