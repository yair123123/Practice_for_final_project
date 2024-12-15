from sqlalchemy.orm import declarative_base

Base = declarative_base()
from .classes import Class
from .student import Student
from .teacher import Teacher
from .relationship import Relationship
from .lifestyle import Lifestyle
from .course_performance import CoursePerformance
