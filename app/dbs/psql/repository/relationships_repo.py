from returns.maybe import Maybe
from returns.result import Success, Failure

from app.dbs.psql.models import Relationship
from app.dbs.settings.config import session_factory


def read_all():
    with session_factory() as session:
        return session.query(Relationship).all()


def read_relationship(relationship_id: int):
    with session_factory() as session:
        return Maybe(session.get(Relationship, relationship_id))


def insert_relationship(relationship: Relationship):
    with session_factory() as session:
        try:
            session.add(relationship)
            session.commit()
            session.refresh(relationship)
            return Success(relationship)
        except Exception as e:
            return Failure(str(e))
