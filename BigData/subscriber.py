import paho.mqtt.client as mqtt
import sqlite3
from storeData import sensor_Data_Handler

def on_connect(mosq, obj, rc):
    if rc==0:
        print("connected")
        mqttc.subscribe(MQTT_Topic, 0) #Subscribe to all Sensors at Base Topic
    else:
        print("bad connection")

def on_message(mosq, obj, msg):
    # This is the Master Call for saving MQTT Data into DB
    print ("MQTT Data Received...")
    print ("MQTT Topic: " + msg.topic)
    print ("Data: " + str(msg.payload))
    sensor_Data_Handler(msg.topic, msg.payload) #Save Data into DB Table

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

# MQTT Settings
MQTT_Broker = "mqtt.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 30
MQTT_Topic = "Home/BedRoom/#"
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect & subscribe
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
mqttc.subscribe(MQTT_Topic, 0)
mqttc.loop_forever() # Continue the network loop