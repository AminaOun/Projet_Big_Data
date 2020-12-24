import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from sqlite3 import Error

try:
    con = sqlite3.connect("./IoT_DataBase.db")
except Error as e:
    print(e)

# Load the data into a DataFrame
temp_df = pd.read_sql_query("SELECT * from Temperature_Data", con)


# temp_df['Temperature'].plot.hist()

# plt.plot(temp_df['Temperature'],temp_df['TemperatureLevel'],label='Temperature')
