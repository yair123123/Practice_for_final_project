from typing import Dict

from returns.maybe import Maybe
from returns.result import Result
from toolz import pipe
from toolz.curried import partial

from app.dbs.models_data_class.student import Student
from app.dbs.settings.config import driver

def convert_to_model_student(letter,record):
    def convert(student:Dict)-> Student:
        return Student(**student)
    return pipe(
        record,
        lambda x: x.map(lambda y: y.get(f"{letter}")),
        lambda x: x.map(lambda y: dict(y)),
        lambda x: x.map(lambda y: convert(y))
    )

def insert_student(student:Student) -> Result[str,str]:
    with driver.session() as session:
        query = """
        create (c:Student {student_id: $student_id,            
        first_name: $first_name,
            last_name: $last_name,
            age: $age,
            address: $address,
        })
        return c
        """
        params = {
            "$student_id": student.id,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "age": student.age,
            "address": student.address,
        }
        res = Maybe.from_optional(session.run(query,params).single())
        return pipe(
            res,
            partial(convert_to_model_student,"c")
        )
