#------------------------------------------
#--- Author: Pradeep Singh
#--- Date: 20th January 2017
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------

import paho.mqtt.client as mqtt
import UnknownTopicError
from store_Sensor_Data_to_DB import sensor_Data_Handler

# MQTT Settings
MQTT_Broker = "192.168.178.130"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "sensors/#"

#Subscribe to all Sensors at Base Topic
def on_connect(mosq, obj, rc,thingy):
	mqttc.subscribe(MQTT_Topic, 0)

#Save Data into DB Table
def on_message(mosq, obj, msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	# print ("MQTT Data Received...")
	# print ("MQTT Topic: " + msg.topic)
	# print ("Data: " + msg.payload)
	try:
		sensor_Data_Handler(msg.topic, msg.payload)
	except UnknownTopicError as e:
		 print ("unknown topic received: ",str(e.args))

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop
mqttc.loop_forever()
