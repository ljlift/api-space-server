from app.crud.base import CRUDBase, ModelType
from app.model import Space
from sqlalchemy.orm import Session
from typing import Optional

from app.schema.space import SpaceCreate, SpaceUpdate


class CRUDSpace(CRUDBase[Space, SpaceCreate, SpaceUpdate]):
    
    def get_by_filter(self, db: Session, name: str) -> Optional[ModelType]:
        return db.query(self.model).filter_by(name=name).one_or_none()


space = CRUDSpace(Space)