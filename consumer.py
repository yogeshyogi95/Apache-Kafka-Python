from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "registered_user", 
        bootstrap_servers=['192.168.0.106:9092'], 
        auto_offset_reset='earliest',
        group_id='consumer-group-a')
    print("[*] Waiting for Messages")
    for msg in consumer:
        print("Received User = {}".format(json.loads(msg.value)))
    