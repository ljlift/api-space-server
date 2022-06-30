from app.crud.base import CRUDBase, ModelType
from app.model import MicroAPI
from sqlalchemy.orm import Session
from typing import Optional

from app.schema.microapi import MicroAPICreate, MicroAPIUpdate


class CRUDMicroAPI(CRUDBase[MicroAPI, MicroAPICreate, MicroAPIUpdate]):
    
    def get_by_filter(self, db: Session, name: str, space_name: str) -> Optional[ModelType]:
        return db.query(self.model).filter_by(name=name, space_name=space_name).one_or_none()

    def get_by_uri(self, db: Session, uri: str) -> Optional[ModelType]:
        return db.query(self.model).filter_by(uri=uri).one_or_none()

microapi = CRUDMicroAPI(MicroAPI)