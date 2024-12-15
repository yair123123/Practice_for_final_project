from returns.maybe import Maybe
from returns.result import Success, Failure

from app.dbs.psql.models import CoursePerformance
from app.dbs.settings.config import session_factory


def read_all():
    with session_factory() as session:
        return session.query(CoursePerformance).all()


def read_course_performance(course_performance_id: int):
    with session_factory() as session:
        return Maybe(session.get(CoursePerformance, course_performance_id))


def insert_course_performance(course_performance: CoursePerformance):
    with session_factory() as session:
        try:
            session.add(course_performance)
            session.commit()
            session.refresh(course_performance)
            return Success(course_performance)
        except Exception as e:
            return Failure(str(e))
