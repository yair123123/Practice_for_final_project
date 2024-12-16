from elasticsearch import Elasticsearch
from neo4j import GraphDatabase
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# psql
engine = create_engine("postgresql://postgres:1234@172.29.168.75:5432/college")


def session_factory():
    Session = sessionmaker(bind=engine)
    return Session()


# mongodb
mongo_client = MongoClient("mongodb://172.29.168.75:27017/")
mongo_db = mongo_client["college"]
classes_collection = mongo_db["classes"]
relationships_collection = mongo_db["relationships"]
students_collection = mongo_db["students"]
teachers_collection = mongo_db["teachers"]

# neo4g
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "pwd1234567890"
driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

# elastic
elastic_client = Elasticsearch(['http://localhost:9200'])

#kafka
BOOTSTRAP_SERVER="localhost:9092,localhost:9093,localhost:9094"
