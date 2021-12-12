# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:38:11 2021

@author: cosim
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

forecast = pd.read_csv("C:/Users/cosim/Desktop/Querini/Data visualization/Forecast_merged.csv")
os.chdir("C:/Users/cosim/Desktop/Querini/Data visualization")

#%%

print(forecast.info)

print(forecast["city"].value_counts())

print(forecast.describe())

#%%

#TUTTE LE TEMPERATURE

#unique_list = list(dict.fromkeys(inp_list))

cities = list(dict.fromkeys(forecast["city"]))

colors = {'Rome':'red', 'Reykjavik':'blue','Jerusalem':'brown','Barcelona':'yellow','Lamezia Terme':'purple','Florence':'deepskyblue','Urbania':'black',
          'San Martino in Pensilis':'pink','Schiavonea':'green','Berlino':'lime','Budapest':'violet','Bruxelles':'sandybrown','Malta':'gold',
          'Parigi':'indigo'}


ax=forecast.plot( kind="scatter", x="time", y="temperature", c = forecast["city"].map(colors))
plt.xticks('')
plt.tight_layout()
plt.savefig( "Temepratures")
plt.show()

#%%

#TEMPERATURA A ROMA

figure, axes = plt.subplots(nrows=3, ncols=3)

axes[0, 0].plot(x, y)
#create specific subplots

axes[0, 1].plot(x1, np.sin(x1))
axes[1, 0].plot(x1, np.cos(x1))
axes[1, 1].plot(range(10))

figure.tight_layout()

for i in cities:
    
Rome = forecast[forecast["city"]=="Rome"]

Rome.plot( kind="scatter", x="time", y="temperature")
plt.tight_layout()
plt.savefig( "Rome_temperature")
plt.show()
