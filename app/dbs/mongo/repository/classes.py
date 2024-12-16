from typing import Dict, List

from pymongo.errors import PyMongoError
from returns.result import Result, Success, Failure

from app.dbs.settings.config import classes_collection


def insert_class(class_data: Dict[str, str]) -> Result[Success, str]:
    try:
        res = classes_collection.insert_one(class_data).inserted_id
        return Success(res)
    except PyMongoError as e:
        return Failure(str(e))


def insert_many_class(class_data: List[Dict[str, str]]) -> Result[Success, str]:
    try:
        classes_collection.insert_many(class_data)
        return Success({"message": "Classes inserted successfully"})
    except PyMongoError as e:
        return Failure(str(e))


def read_classes() -> Result[Success, str]:
    try:
        res = classes_collection.find().inserted_id
        return Success(res)
    except PyMongoError as e:
        return Failure(str(e))
