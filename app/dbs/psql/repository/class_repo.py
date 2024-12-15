from returns.maybe import Maybe
from returns.result import Success, Failure

from app.dbs.psql.models import Class
from app.dbs.settings.config import session_factory


def read_all_classes():
    with session_factory() as session:
        return session.query(Class).all()


def read_class(class_id: int):
    with session_factory() as session:
        return Maybe(session.get(Class, class_id))


def insert_class(class_model: Class):
    with session_factory() as session:
        try:
            session.add(class_model)
            session.commit()
            session.refresh(class_model)
            return Success(class_model)
        except Exception as e:
            return Failure(str(e))
