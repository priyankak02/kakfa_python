#Python code to write message in form of key value pair
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
topic_name='test2'
producer.send(topic_name, key=b'goo', value=b'bar') #Note :key & value serialization we are doing while publishing the message
                                                    #itself , so explicitly not mentioning the key or value serializer
producer.send(topic_name, key=b'sooo', value=b'chocolate')
producer.close()
