from kafka import KafkaProducer
import json
import time

print("Starting Kafka Producer...")

producer = KafkaProducer(
    bootstrap_servers='127.0.0.1:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

transactions = [
    {"customer_id": 1, "amount": 5000},
    {"customer_id": 2, "amount": 7000},
    {"customer_id": 3, "amount": 9000}
]

for transaction in transactions:
    producer.send('retail_topic', transaction)
    print(f"Sent: {transaction}")
    time.sleep(2)

producer.flush()

print("All messages sent successfully")