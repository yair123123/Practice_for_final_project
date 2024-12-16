from dataclasses import asdict

from app.dbs.models_data_class.review import Review
from app.dbs.settings.config import elastic_client

def create_index(index_name):
    if not elastic_client.indices.exists(index=index_name):
        elastic_client.indices.create(index=index_name,body={
            "mappings": {
                "properties": {
                    "review_id": {"type":"text"},
                    "content": {"type":"text"},
                    "score": {"type":"float"},
                    "date_time": {"type":"date","format":"dd-MM-yyyy HH:mm"},
                    "thumbs_up_count": {"type":"integer"},
                    "review_created_version": {"type":"text"},
                    "app_version": {"type":"text"},
                    "student_id": {"type":"integer"},
                }
            }
        })

def insert_review(review:Review):
    try:
        elastic_client.index(index="reviews", body=asdict(review))
    except Exception as e:
        print(e)
a = {
  "review_id": "12345abcde",
  "content": "This app is amazing! The user interface is intuitive and responsive.",
  "score": 4.5,
  "date_time": "15-12-2024 14:30",
  "thumbs_up_count": 125,
  "review_created_version": "1.3.0",
  "app_version": "1.5.2",
  "student_id": 987654
}
