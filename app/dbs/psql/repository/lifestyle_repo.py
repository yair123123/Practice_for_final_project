from returns.maybe import Maybe
from returns.result import Success, Failure

from app.dbs.psql.models import Lifestyle
from app.dbs.settings.config import session_factory


def read_all():
    with session_factory() as session:
        return session.query(Lifestyle).all()


def read_lifestyle(lifestyle_id: int):
    with session_factory() as session:
        return Maybe(session.get(Lifestyle, lifestyle_id))


def insert_lifestyle(lifestyle: Lifestyle):
    with session_factory() as session:
        try:
            session.add(lifestyle)
            session.commit()
            session.refresh(lifestyle)
            return Success(lifestyle)
        except Exception as e:
            return Failure(str(e))
