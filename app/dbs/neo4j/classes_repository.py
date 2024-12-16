from typing import Dict

from returns.maybe import Maybe
from returns.result import Result
from toolz import pipe
from toolz.curried import partial

from app.dbs.models_data_class.class_model import Class
from app.dbs.settings.config import driver

def convert_to_model_class(letter,record):
    def convert(class_data:Dict)-> Class:
        return Class(**class_data)
    return pipe(
        record,
        lambda x: x.map(lambda y: y.get(f"{letter}")),
        lambda x: x.map(lambda y: dict(y)),
        lambda x: x.map(lambda y: convert(y))
    )

def insert_class(class_model:Class) -> Result[str,str]:
    with driver.session() as session:
        query = """
        match (t:Teacher {teacher_id = $teacher_id})
        create (c:Class {class_id: $class_id,            
        course_name: $course_name,
            section: $section,
            department: $department,
            semester: $semester,
            room: $room,
            schedule: $schedule,
        })
        merge t - [TEACHING_IN] ->  C
        return c
        """
        params = {
            "class_id": class_model.id,
            "course_name": class_model.course_name,
            "section": class_model.section,
            "department": class_model.department,
            "semester": class_model.semester,
            "room": class_model.room,
            "schedule": class_model.schedule,
            "teacher_id": class_model.teacher_id,
        }
        res = Maybe.from_optional(session.run(query,params).single())
        return pipe(
            res,
            partial(convert_to_model_class,"c")
        )
