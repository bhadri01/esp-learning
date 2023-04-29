import paho.mqtt.client as mqtt

# define MQTT broker and topic
broker_address = "192.168.0.135"
topic = "test_1"

# create client instance
client = mqtt.Client()

# connect to broker
client.connect(broker_address)

# publish a message to the topic
message = "Hello, world!"
client.publish(topic, message)

# disconnect from broker
client.disconnect()
