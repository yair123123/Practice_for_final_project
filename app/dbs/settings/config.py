from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#psql
engine = create_engine("postgresql://postgres:1234@172.29.168.75:5432/college")
def session_factory():
    return sessionmaker(bind=engine)
#mongodb

#neo4g

#elastic