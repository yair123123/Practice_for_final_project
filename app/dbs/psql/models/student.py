from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from app.dbs.psql.models import Base


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String,  nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)

    relationships = relationship("Relationship",back_populates="student")
    lifestyle = relationship("Lifestyle", back_populates="student")
    course_performance = relationship("CoursePerformance",back_populates="student")
