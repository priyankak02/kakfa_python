from kafka import KafkaConsumer

consumer = KafkaConsumer('my-topic',bootstrap_servers=['localhost:9092'])

for m in consumer:
        print(m.value)
