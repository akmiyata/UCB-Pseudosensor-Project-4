from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from pseudoSensor import PseudoSensor
from datetime import datetime
import time
import boto3
import json
import os
import sys

#Define MQTT client
myMQTTClient = AWSIoTMQTTClient("dojodevice1")
myMQTTClient.configureEndpoint("a282wfrznzqkn3-ats.iot.us-east-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("./AmazonRootCA1 (1).pem","#####.pem.key", "#####.pem.crt")
myMQTTClient.connect()
print("Client Connected")

#Create Simple Notofication Service client with Boto3
client = boto3.client('sns',
region_name='us-east-2',aws_access_key_id='########',aws_secret_access_key='SecretSanta')
response = client.list_topics()

#Get timestamp
rn=datetime.now()
timein=str(rn.strftime("%H:%M:%S"))

#Generate weather value, store in 'foo'
ps=PseudoSensor()
for i in range(1):
h,t = ps.generate_values()
foo={"Time":timein, "Humidity":h,"Temperature":t}

#Reformat json to string, so it can be used by 'publish'
json_dump=json.dumps(foo)
msg = json_dump

#Publish to general/inbound topic
topic = "general/inbound"
myMQTTClient.publish(topic, msg, 0)

client.publish(TopicArn='arn:aws:sns:us-east-2:305202504581:Weather',Message=msg,Subject='Weather
',)
print("Message Sent")
time.sleep(2)
myMQTTClient.disconnect()
print("Client Disconnected")