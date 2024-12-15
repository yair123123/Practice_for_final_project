from app.dbs.psql.models import Base
from app.dbs.settings.config import engine


def initdb():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
