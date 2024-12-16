from flask import Flask

from app.flow.psql import fill_data_to_psql
from dbs import psql
from app.dbs.psql.repository.database import initdb

app = Flask(__name__)
if __name__ == '__main__':
    initdb()
    fill_data_to_psql()
    app.run()
