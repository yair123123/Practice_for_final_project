from typing import Dict

from returns.maybe import Maybe
from returns.result import Result
from toolz import pipe
from toolz.curried import partial

from app.dbs.models_data_class.class_model import Class
from app.dbs.models_data_class.teacher import Teacher
from app.dbs.settings.config import driver

def convert_to_model_teacher(letter,record):
    def convert(teacher:Dict)-> Class:
        return Class(**teacher)
    return pipe(
        record,
        lambda x: x.map(lambda y: y.get(f"{letter}")),
        lambda x: x.map(lambda y: dict(y)),
        lambda x: x.map(lambda y: convert(y))
    )

def insert_teacher(teacher:Teacher) -> Result[str,str]:
    with driver.session() as session:
        query = """
        create (t:Teacher {teacher_id: $teacher_id,            
        course_name: $course_name,
            name: $name,
            department: $department,
            title: $title,
            office: $office,
            email: $email,
        })
        return t
        """
        params = {
            "teacher_id": teacher.id,
            "course_name": teacher.id,
            "name": teacher.name,
            "department": teacher.department,
            "title": teacher.title,
            "office": teacher.office,
            "email": teacher.email,
        }
        res = Maybe.from_optional(session.run(query,params).single())
        return pipe(
            res,
            partial(convert_to_model_teacher,"t")
        )
