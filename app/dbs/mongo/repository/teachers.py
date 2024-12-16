from typing import Dict, List

from pymongo.errors import PyMongoError
from returns.result import Result, Success, Failure

from app.dbs.settings.config import classes_collection, teachers_collection


def insert_teacher(teacher: Dict[str, str]) -> Result[Success, str]:
    try:
        res = teachers_collection.insert_one(teacher).inserted_id
        return Success(res)
    except PyMongoError as e:
        return Failure(str(e))


def insert_many_teachers(teachers: List[Dict[str, str]]) -> Result[Success, str]:
    try:
        teachers_collection.insert_many(teachers)
        return Success({"message": "Teachers inserted successfully"})
    except PyMongoError as e:
        return Failure(str(e))


def read_teachers() -> Result[Success, str]:
    try:
        res = teachers_collection.find().inserted_id
        return Success(res)
    except PyMongoError as e:
        return Failure(str(e))
