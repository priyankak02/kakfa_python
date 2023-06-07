from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

while True:
        msg = input()
        producer.send('my-topic',msg.encode('utf-8'))
        print(f'{msg} sent')
