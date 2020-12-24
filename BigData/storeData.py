import sqlite3
from sqlite3 import Error
import json

def sensor_Data_Handler(topic, payload):
    Humidity_Data = json.loads(payload)
    if ("Humidity" in topic):
        humy = (Humidity_Data["Sensor_ID"],Humidity_Data["Humidity"],Humidity_Data["Date"],Humidity_Data["HumidityLevel"])
        print (humy)
        try:
            conn = sqlite3.connect("./IoT_DataBase.db", isolation_level=None)
            sql = '''INSERT INTO Humidity_Data (SensorID,Humidity,Date_Time,HumidityLevel) values(?,?,?,?)'''
            cur = conn.cursor()
            cur.execute(sql, humy)
            return cur.lastrowid
        except Error as e:
            print(e)
    elif ("Temperature" in topic):
        humy = (Humidity_Data["Sensor_ID"],Humidity_Data["Temperature"],Humidity_Data["Date"],Humidity_Data["TemperatureLevel"])
        print (humy)
        try:
            conn = sqlite3.connect("./IoT_DataBase.db", isolation_level=None)
            sql = '''INSERT INTO Temperature_Data (SensorID,Temperature,Date_Time,TemperatureLevel) values(?,?,?,?)'''
            cur = conn.cursor()
            cur.execute(sql, humy)
            return cur.lastrowid
        except Error as e:
            print(e)
    elif ("Acceleration" in topic):
        humy = (Humidity_Data["Sensor_ID"],Humidity_Data["Date"],Humidity_Data["accX"],Humidity_Data["accY"],Humidity_Data["accZ"])
        print (humy)
        try:
            conn = sqlite3.connect("./IoT_DataBase.db", isolation_level=None)
            sql = '''INSERT INTO Acceleration_Data (SensorID,Date_Time,accX,accY,accZ) values(?,?,?,?,?)'''
            cur = conn.cursor()
            cur.execute(sql, humy)
            return cur.lastrowid
        except Error as e:
            print(e)
