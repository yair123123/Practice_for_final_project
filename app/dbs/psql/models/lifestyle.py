from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.dbs.psql.models import Base


class Lifestyle(Base):
    __tablename__ = 'lifestyle'
    id = Column(Integer, primary_key=True,autoincrement=True)
    Student_ID = Column(Integer,ForeignKey("student.id"), nullable=False)
    Study_Hours_Per_Day = Column(Float,  nullable=False)
    Extracurricular_Hours_Per_Day = Column(Float, nullable=False)
    Sleep_Hours_Per_Day = Column(Float, nullable=False)
    Social_Hours_Per_Day = Column(Float, nullable=False)
    Physical_Activity_Hours_Per_Day = Column(Float, nullable=False)
    GPA = Column(Float, nullable=False)
    Stress_Level = Column(String, nullable=False)

    student = relationship("Student", back_populates="lifestyle")
