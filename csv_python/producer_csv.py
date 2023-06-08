from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

while True:
	print("\n Type \"quit\" to exit")
	print("Enter message to be sent :")
	msg = input()
	if msg=="quit":
		print("Exiting..")
		break
	producer.send('test-csv',msg.encode('utf-8'))
	print(f'Sending message {msg} ')
