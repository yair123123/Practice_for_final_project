import json
import os

from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.dbs.elastic.database import insert_review

load_dotenv(verbose=True)
def consume_save_reviews_in_elastic():
    consumer = KafkaConsumer(
        os.environ['TOPIC_ELASTIC_REVIEWS'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    print('listing...')
    for message in consumer:
        insert_review(message.value)
        print(f'received: {message.key} : {message.value}')

