import paho.mqtt.client as mqtt
import time

client=mqtt.Client()

while True:
    client.connect('',1883)
    client.publish('aws/pub1',' ')
    time.sleep(1)