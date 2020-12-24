# 1-Graph in GUI
# 2-Linking data to graphs
# 3-Refreshing graphs
import tkinter as tk
from pandas import DataFrame
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
from sqlite3 import Error
# import datetime as dt

try:
    con = sqlite3.connect("./IoT_DataBase.db")
except Error as e:
    print(e)

# Load the data into a DataFrame
temp_df = pd.read_sql_query("SELECT * from Temperature_Data", con)
humy_df = pd.read_sql_query("SELECT * from Humidity_Data", con)
accel_df = pd.read_sql_query("SELECT * from Acceleration_Data", con,parse_dates=False)
df01 = DataFrame(temp_df,columns=['Temperature','TemperatureLevel'])

class Data:
    def __init__(self):
        self.temp_df = pd.read_sql_query("SELECT * from Temperature_Data", con)
        self.humy_df = pd.read_sql_query("SELECT * from Humidity_Data", con)
        self.accel_df = pd.read_sql_query("SELECT * from Acceleration_Data", con, parse_dates=False)

        self.df01 = DataFrame(temp_df,columns=['Temperature','TemperatureLevel'])
        self.df02 = DataFrame(humy_df,columns=['Humidity','HumidityLevel'])
        self.df03 = DataFrame(accel_df,columns=['Date_Time','accX','accY','accZ'])
        self.fig1 = self.df01[['TemperatureLevel','Temperature']].groupby('TemperatureLevel').mean().to_dict()
        self.fig2 = self.df02[['HumidityLevel','Humidity']].groupby('HumidityLevel').mean().to_dict()
        self.fig4 = self.df03[['accX','accY','accZ','Date_Time']].groupby('Date_Time').mean().to_dict()

    @staticmethod
    def refreshTemperatureData():
        temp_df = pd.read_sql_query("SELECT * from Temperature_Data", con)
        df01 = DataFrame(temp_df,columns=['Temperature','TemperatureLevel'])
        fig1 = df01[['TemperatureLevel','Temperature']].groupby('TemperatureLevel').mean().to_dict()
        return fig1

    @staticmethod
    def refreshHumidityData():
        humy_df = pd.read_sql_query("SELECT * from Humidity_Data", con)
        df02 = DataFrame(humy_df,columns=['Humidity','HumidityLevel'])
        fig2 = df02[['HumidityLevel','Humidity']].groupby('HumidityLevel').mean().to_dict()
        return fig2

    @staticmethod
    def refreshAccelerationData():
        accel_df = pd.read_sql_query("SELECT * from Acceleration_Data", con,parse_dates=False)
        df03 = DataFrame(accel_df,columns=['Date_Time','accX','accY','accZ'])
        df03['Date_Time'] = pd.to_datetime(df03['Date_Time'],errors='coerce', format='%d-%b-%Y %H:%M:%S:%f').dt.strftime('%d-%b-%Y %H:%M')
        fig4 = df03[['accX','accY','accZ','Date_Time']].groupby('Date_Time').mean().to_dict()
        return fig4

    @staticmethod
    def drawAcc(fig4,root,figure4):
        figure4.clear()
        subplot4 = figure4.add_subplot(111)
        subplot4.plot([*fig4['accX']],list(fig4['accX'].values()))
        subplot4.plot([*fig4['accY']],list(fig4['accY'].values()))
        subplot4.plot([*fig4['accZ']],list(fig4['accZ'].values()))
        subplot4.set_xlabel('m/s2')
        subplot4.set_ylabel('time')
        subplot4.set_xticklabels([*fig4['accX']],rotation=45)
        multiplot = FigureCanvasTkAgg(figure4, root)
        multiplot.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

    @staticmethod
    def drawHumidity(fig2,root,figure2):
        fig2 = Data.refreshHumidityData()
        subplot2 = figure2.add_subplot(111)
        labels2 = fig2['Humidity'].keys() 
        pieSizes = fig2['Humidity'].values()
        my_colors2 = ["#48f3db", "#51c4e9", "#6150c1"]
        explode2 = (0.1, 0.1, 0.1)  
        subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90) 
        subplot2.axis('equal')  
        subplot2.set_title('Pie Chart of Humidity')
        pie2 = FigureCanvasTkAgg(figure2, root)
        pie2.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH)

    @staticmethod
    def drawTemperature(fig3,root,figure3):
        subplot3 = figure3.add_subplot(111) 
        labels3 = fig3['Temperature'].keys() 
        pieSizes3 = fig3['Temperature'].values()
        my_colors3 = ["#3f51b5", "#3848a2", "#324091","#1d87da", "#2196f3"]
        explode3 = (0.1, 0.1, 0.1, 0.1, 0.1)  
        subplot3.pie(pieSizes3, colors=my_colors3, explode=explode3, labels=labels3, autopct='%1.1f%%', shadow=True, startangle=90) 
        subplot3.axis('equal')  
        subplot3.set_title('Pie Chart of Temperature')
        pie3 = FigureCanvasTkAgg(figure3, root)
        pie3.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

# print(fig4['accX'].values())
# print(fig3)

root= tk.Tk() 
root.wm_iconbitmap('Royal-sun.ico')
root.wm_title('IoT Sensors')

figure1 = plt.Figure(figsize=(4,8), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH)
data = Data()
df01 = data.df01
df01 = df01[['Temperature','TemperatureLevel']].groupby('TemperatureLevel').mean()
df01.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Average of temperature')

# print(fig4)

fig2 = Data.refreshHumidityData()
fig3 = Data.refreshTemperatureData()
fig4 = Data.refreshAccelerationData()

figure2 = plt.Figure(figsize=(5,5), dpi=100) 
figure3 = plt.Figure(figsize=(5,5), dpi=100) 
figure4 = plt.Figure(figsize=(5,5), dpi=100)

Data.drawAcc(fig4,root,figure4)
Data.drawHumidity(fig2,root,figure2)
Data.drawTemperature(fig3,root,figure3)

while True:
    fig3 = Data.refreshTemperatureData()
    fig2 = Data.refreshHumidityData()
    fig4 = Data.refreshAccelerationData()
    Data.drawAcc(fig4,root,figure4)
    plt.pause(8)
    print(fig4)
    root.update_idletasks()
    root.update()