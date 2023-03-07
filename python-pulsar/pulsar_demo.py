import pulsar

client = pulsar.Client('pulsar://192.168.1.2:6650')
consumer = client.subscribe('eventos-orden', subscription_name='eventos-orden')

# while True:
#     msg = consumer.receive()
#     print("Received message: '{}'".format(msg.data())
#     consumer.acknowledge(msg)

client.close()

