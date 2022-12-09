#!/usr/bin/env python3

from kafka import KafkaConsumer
import json
serverip = "10.128.11.250"  # Change to Server IP
serverport = "9092"
kafkaserver = [serverip + ":" + serverport]
topicname = 'storesalesdev'
timeoutseconds = 60*1000000

print("Connecting to Consumer")
consumer = KafkaConsumer(
    topicname,
    auto_offset_reset="earliest",
    bootstrap_servers=kafkaserver,
    consumer_timeout_ms=timeoutseconds,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
for msg in consumer:
    print(json.dumps(dict(msg.value), indent = 4))
