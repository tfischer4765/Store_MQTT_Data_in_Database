# ------------------------------------------
# --- Author: Pradeep Singh
# --- Date: 20th January 2017
# --- Version: 1.0
# --- Python Ver: 2.7
# --- Details At:
# https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
# ------------------------------------------


import UnknownTopicError
import MySQLdb

# SQLite DB Name
DB_Name = "iot_test"
db_server = "nas"
db_user = "iot_test"
db_past = "Password1"

# ===============================================================
# Database Manager Class


class DatabaseManager():
	def __init__(self):
		self.conn = MySQLdb.connect(host=db_server,
									user=db_user,
									passwd=db_past,
									db=DB_Name)
		# self.conn.execute('pragma foreign_keys = on')
		# self.conn.commit()
		self.cur = self.conn.cursor()

	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		try:
			self.cur.close()
			self.conn.close()
		finally:
			print ("Cleaned up")

# ===============================================================
# Functions to push Sensor Data into Database


# Function to save Temperature to DB Table
def push_temp_data(Temperature,Sensor):
	# Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("""insert into temperatures (source,  temperature) values (%s,%s)""", [Sensor, Temperature])
	del dbObj
	#print ("Inserted Temperature Data into Database.")
	#print ("")


# Function to save Humidity to DB Table
def push_voltage_data(Voltage, Sensor):

	# Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("""insert into voltages (source, voltage) values (%s,%s)""", [Sensor, Voltage])
	del dbObj
	#print ("Inserted Voltage Data into Database.")
	#print ("")


# ===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, data):
	if Topic.find("voltage")>-1:
		push_voltage_data(data,Topic)
	elif Topic.find("temperature")>-1:
		push_temp_data(data,Topic)
	else:
		raise UnknownTopicError(Topic)

# ===============================================================
