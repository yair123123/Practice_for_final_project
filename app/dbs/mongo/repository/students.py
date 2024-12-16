from typing import Dict, List

from pymongo.errors import PyMongoError
from returns.result import Result, Success, Failure

from app.dbs.settings.config import classes_collection, students_collection


def insert_student(student: Dict[str, str]) -> Result[Success, str]:
    try:
        res = students_collection.insert_one(student).inserted_id
        return Success(res)
    except PyMongoError as e:
        return Failure(str(e))


def insert_many_students(students: List[Dict[str, str]]) -> Result[Success, str]:
    try:
        students_collection.insert_many(students)
        return Success({"message": "Students inserted successfully"})
    except PyMongoError as e:
        return Failure(str(e))


def read_students() -> Result[Success, str]:
    try:
        res = students_collection.find().inserted_id
        return Success(res)
    except PyMongoError as e:
        return Failure(str(e))
