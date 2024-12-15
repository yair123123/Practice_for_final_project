from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.dbs.psql.models import Base


class Class(Base):
    __tablename__ = 'class'
    id = Column(String, primary_key=True)
    course_name = Column(String, nullable=False)
    section = Column(Integer,  nullable=False)
    department = Column(String, nullable=False)
    semester = Column(String, nullable=False)
    room = Column(String, nullable=False)
    schedule = Column(String, nullable=False)
    teacher_id = Column(String, nullable=False)

    relationships = relationship("Relationship",back_populates="class_data")
