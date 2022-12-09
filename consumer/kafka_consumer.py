#!/usr/bin/env python3

from kafka import KafkaConsumer
import json
import requests
import os

os.environ['POST_TO_URL'] = 'http://0.0.0.0:8081'

serverip = "10.128.11.250"  # Change to Server IP
serverport = "9092"
kafkaserver = [serverip + ":" + serverport]
topicname = 'storesalesdev'
# timeoutseconds = 60*1000000

class KafkaConsumerMessenger():
    def __init__():

        pass

    @staticmethod
    def run_kafka_consumer():
        print("Connecting to Consumer")
        consumer = KafkaConsumer(
            topicname,
            auto_offset_reset="earliest",
            bootstrap_servers=kafkaserver,
            # consumer_timeout_ms=timeoutseconds,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
            )
        
        for msg in consumer:
            # print(msg)

            # d[i] = (json.dumps(dict(msg.value), indent = 4))
            # requests.post(url=str(os.getenv("POST_TO_URL") + "/readMsg"), data=str(msg))
            requests.post(url=str(os.getenv("POST_TO_URL") + "/model"), data=str(msg.value))
            
        
if __name__ == "__main__":
    KafkaConsumerMessenger.run_kafka_consumer()  