
from dataclasses import dataclass
from typing import Optional


@dataclass
class Relationship:
    id : int
    student_id : int
    class_id : str
    teacher_id : str
    enrollment_date : str
    relationship_type : str
