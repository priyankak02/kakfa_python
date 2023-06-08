from kafka import KafkaConsumer

consumer = KafkaConsumer('my-topic',bootstrap_servers=['localhost:9092'])

for m in consumer:
        print(m.value)
        print ("%s:%d:%d: key=%s value=%s" % (m.topic, m.partition,
                                          m.offset, m.key,
                                          m.value))
