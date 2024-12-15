from returns.maybe import Maybe
from returns.result import Success, Failure

from app.dbs.psql.models import Student
from app.dbs.settings.config import session_factory


def read_all():
    with session_factory() as session:
        return session.query(Student).all()


def read_student(student_id: int):
    with session_factory() as session:
        return Maybe(session.get(Student, student_id))


def insert_student(student: Student):
    with session_factory() as session:
        try:
            session.add(student)
            session.commit()
            session.refresh(student)
            return Success(student)
        except Exception as e:
            return Failure(str(e))
