import json
import time
from kafka import KafkaProducer
from data import get_registered_user


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(
                        bootstrap_servers=['192.168.0.106:9092'],
                        value_serializer=json_serializer
                        )

if __name__ == "__main__":
    while True:
        registered_user = get_registered_user()
        print("[x]Sending "+str(registered_user))
        producer.send("registered_user", registered_user)
        time.sleep(4)