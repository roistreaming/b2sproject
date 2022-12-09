#!/usr/bin/env python3

from kafka import KafkaConsumer
serverip = "10.128.11.250"  # Change to Server IP
serverport = "9092"
kafkaserver = [serverip + ":" + serverport]
topicname = 'storesalestest'
timeoutseconds = 60*1000

print("Connecting to Consumer")
consumer = KafkaConsumer(
    topicname,
    auto_offset_reset="earliest",
    bootstrap_servers=kafkaserver,
    consumer_timeout_ms=timeoutseconds
    )
for msg in consumer:
    print (msg)
