from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.mysql import JSON

from app.database.base_class import Base


class MicroAPI(Base):
    __tablename__ = "microapi"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    space_name = Column(String(128))
    uri = Column(String(128))
