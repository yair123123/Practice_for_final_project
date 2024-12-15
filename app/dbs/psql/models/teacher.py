from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.dbs.psql.models import Base


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(String, primary_key=True)
    name = Column(String,  nullable=False)
    department = Column(String, nullable=False)
    title = Column(String, nullable=False)
    office = Column(String, nullable=False)
    email = Column(String, nullable=False)

    relationships = relationship("Relationship",back_populates="teacher")
