from typing import Dict, List

from pymongo.errors import PyMongoError
from returns.result import Result, Success, Failure

from app.dbs.settings.config import classes_collection, relationships_collection


def insert_relationship(relationship: Dict[str, str]) -> Result[Success, str]:
    try:
        res = relationships_collection.insert_one(relationship).inserted_id
        return Success(res)
    except PyMongoError as e:
        return Failure(str(e))


def insert_many_relationships(relationship: List[Dict[str, str]]) -> Result[Success, str]:
    try:
        relationships_collection.insert_many(relationship)
        return Success({"message": "Relationships inserted successfully"})
    except PyMongoError as e:
        return Failure(str(e))


def read_relationships() -> Result[Success, str]:
    try:
        res = relationships_collection.find({}).inserted_id
        return Success(res)
    except PyMongoError as e:
        return Failure(str(e))
