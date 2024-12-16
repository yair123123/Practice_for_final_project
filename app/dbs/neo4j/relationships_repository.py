from typing import Dict

from returns.maybe import Maybe
from returns.result import Result
from toolz import pipe
from toolz.curried import partial

from app.dbs.models_data_class.relationship import Relationship
from app.dbs.settings.config import driver


def convert_to_model_relationship(letter, record):
    def convert(class_data: Dict) -> Relationship:
        return Relationship(**class_data)

    return pipe(
        record,
        lambda x: x.map(lambda y: y.get(f"{letter}")),
        lambda x: x.map(lambda y: dict(y)),
        lambda x: x.map(lambda y: convert(y))
    )


def insert_relationship(relationship: Relationship) -> Result[str, str]:
    with driver.session() as session:
        query = """
        match (s : Student {student_id = $student_id}),
                (c : Class {class_id = $class_id})
        merge (s) - [r:LEARN_IN {relation_id = relation_id, enrollment_date = $enrollment_date, relationship_type= $relationship_type}] -> (c) 
        return r
        """
        params = {
            "student_id": relationship.student_id,
            "class_id": relationship.class_id,
            "enrollment_date": relationship.enrollment_date,
            "relationship_type": relationship.relationship_type,
        }
        res = Maybe.from_optional(session.run(query, params).single())
        return pipe(
            res,
            partial(convert_to_model_relationship, "r")
        )
