from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.mysql import JSON

from app.database.base_class import Base


class Space(Base):
    __tablename__ = "space"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    ruleset = Column(JSON)
