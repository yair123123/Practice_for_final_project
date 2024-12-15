from returns.maybe import Maybe
from returns.result import Success, Failure

from app.dbs.psql.models import Teacher
from app.dbs.settings.config import session_factory


def read_all():
    with session_factory() as session:
        return session.query(Teacher).all()


def read_teacher(teacher_id: int):
    with session_factory() as session:
        return Maybe(session.get(Teacher, teacher_id))


def insert_teacher(teacher: Teacher):
    with session_factory() as session:
        try:
            session.add(teacher)
            session.commit()
            session.refresh(teacher)
            return Success(teacher)
        except Exception as e:
            return Failure(str(e))
