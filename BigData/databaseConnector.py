import sqlite3

DB_Name = "IoT_DataBase.db"
TableSchema="""
drop table if exists Temperature_Data ;
create table Temperature_Data (
id integer primary key autoincrement,
SensorID text,
Date_Time text,
Temperature decimal(6,2),
TemperatureLevel text
);
drop table if exists Humidity_Data ;
create table Humidity_Data (
id integer primary key autoincrement,
SensorID text, Date_Time text,
Humidity decimal(6,2),
HumidityLevel text
);
drop table if exists Acceleration_Data ;
create table Acceleration_Data (
id integer primary key autoincrement,
SensorID text,
Date_Time DATETIME, accX decimal(6,2),
accY decimal(6,2), accZ decimal(6,2)
);
"""
#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()
#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)
#Close DB
curs.close()
conn.close()