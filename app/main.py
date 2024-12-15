from flask import Flask
from dbs import psql
from app.dbs.psql.repository.database import initdb

app = Flask(__name__)
if __name__ == '__main__':
    initdb()
    app.run()
