from dotenv import load_dotenv
from kafka import KafkaConsumer

load_dotenv(verbose=True)
def consume_save_in_elastic():
    consumer = KafkaConsumer(
        os.environ['TOPIC_EXPLOS'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    print('listing...')
    for message in consumer:
        save_to_db(message.value, "E")
        print(f'received: {message.key} : {message.value}')

