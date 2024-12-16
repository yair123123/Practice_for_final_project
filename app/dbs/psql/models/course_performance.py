from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.dbs.psql.models import Base


class CoursePerformance(Base):
    __tablename__ = 'course_performance'
    id = Column(Integer, primary_key=True,autoincrement=True)
    student_id = Column(Integer,ForeignKey("student.id"), nullable=False)
    course_name = Column(String,  nullable=False)
    current_grade = Column(Float, nullable=False)
    attendance_rate = Column(Float, nullable=False)
    assignments_completed = Column(Integer, nullable=False)
    missed_deadlines = Column(Integer, nullable=False)
    participation_score = Column(Float, nullable=False)
    midterm_grade = Column(Float, nullable=False)
    study_group_attendance = Column(Float, nullable=False)
    office_hours_visits = Column(Integer, nullable=False)
    extra_credit_completed = Column(Integer, nullable=False)

    student = relationship("Student",back_populates="course_performance")
