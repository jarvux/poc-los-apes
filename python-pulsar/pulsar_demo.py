import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('test_', subscription_name='my-subscription')

# while True:
#     msg = consumer.receive()
#     print("Received message: '{}'".format(msg.data())
#     consumer.acknowledge(msg)

client.close()

