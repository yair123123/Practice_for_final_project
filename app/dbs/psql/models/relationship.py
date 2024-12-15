from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.dbs.psql.models import Base


class Relationship(Base):
    __tablename__ = 'relationship'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    class_id = Column(String, ForeignKey("class.id"), nullable=False)
    teacher_id = Column(String, ForeignKey("teacher.id"), nullable=False)
    enrollment_date = Column(String, nullable=False)
    relationship_type = Column(String, nullable=False)

    student = relationship("Student", back_populates="relationships")
    class_data = relationship("Class", back_populates="relationships")
    teacher = relationship("Teacher", back_populates="relationships")
