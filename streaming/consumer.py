from kafka import KafkaConsumer
import json
import psycopg2

print("Starting Kafka Consumer...")

consumer = KafkaConsumer(
    'retail_topic',
    bootstrap_servers='127.0.0.1:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Connecting to PostgreSQL...")

conn = psycopg2.connect(
    host="localhost",
    database="retail_dw",
    user="postgres",
    password="Devdeep6200"
)

cursor = conn.cursor()

print("Listening for messages...")

for message in consumer:

    data = message.value

    print(f"Received: {data}")

    customer_id = data['customer_id']
    amount = data['amount']

    cursor.execute(
        """
        INSERT INTO realtime_transactions(customer_id, amount)
        VALUES (%s, %s)
        """,
        (customer_id, amount)
    )

    conn.commit()

    print("Inserted into PostgreSQL")