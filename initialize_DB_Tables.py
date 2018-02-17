# ------------------------------------------
# --- Author: Pradeep Singh
# --- Date: 20th January 2017
# --- Version: 1.0
# --- Python Ver: 2.7
# --- Details At:
# https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
# ------------------------------------------

import MySQLdb

# SQLite DB Name
DB_Name = "iot_test"

# SQLite DB Table Schema
TableSchema = """
drop table if exists DHT22_Temperature_Data ;
create table DHT22_Temperature_Data (
  id integer primary key autoincrement,
  SensorID text,
  Date_n_Time text,
  Temperature text
);


drop table if exists DHT22_Humidity_Data ;
create table DHT22_Humidity_Data (
  id integer primary key autoincrement,
  SensorID text,
  Date_n_Time text,
  Humidity text
);
"""

# Connect or Create DB File
conn = MySQLdb.connect(DB_Name)
curs = conn.cursor()

# Create Tables
MySQLdb.complete_statement(TableSchema)
curs.executescript(TableSchema)

# Close DB
curs.close()
conn.close()
