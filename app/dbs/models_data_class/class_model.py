from dataclasses import dataclass


@dataclass
class Class:
    id: str
    course_name: str
    section: int
    department: str
    semester: str
    room: str
    schedule: str
    teacher_id: str

