import paho.mqtt.client as mqtt
import time

client=mqtt.Client()

client.connect('',1883)
print('Broker Connected')

client.subscribe('aws/pub1')

def notification(client,userdata,msg):
    print(msg.payload)

client.on_message=notification
client.loop_forever()