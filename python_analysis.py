# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:38:11 2021

@author: cosim
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

forecast = pd.read_csv("C:/Users/cosim/Desktop/Querini/PythonR-/Forecast_merged.csv")
os.chdir("C:/Users/cosim/Desktop/Querini/PythonR-")

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

Rome = forecast[forecast["city"]=="Rome"]
Paris = forecast[forecast["city"]=="Parigi"]
Reykjavik = forecast[forecast["city"]=="Reykjavik"]
Jerusalem = forecast[forecast["city"]=="Jerusalem"]
Barcelona = forecast[forecast["city"]=="Barcelona"]
Florence = forecast[forecast["city"]=="Florence"]
Malta = forecast[forecast["city"]=="Malta"]
SanMartinoinPensilis = forecast[forecast["city"]=="San Martino in Pensilis"]
Budapest = forecast[forecast["city"]=="Budapest"]

figure, axes = plt.subplots(nrows=3, ncols=3)
axes[0, 0].plot(Rome["time"], Rome["temperature"], c = 'red')
axes[0,0].xaxis.set(ticks='')
axes[0,0].set(title= 'Rome')

axes[1, 0].plot(Paris["time"], Paris["temperature"], c = 'indigo')
axes[1,0].xaxis.set(ticks='')
axes[1,0].set(title= 'Paris')

axes[2, 0].plot(Reykjavik["time"], Reykjavik["temperature"], c = 'blue')
axes[2,0].xaxis.set(ticks='')
axes[2,0].set(title= 'Reykjavik')

axes[0, 1].plot(Jerusalem["time"], Jerusalem["temperature"], c = 'brown', )
axes[0,0].xaxis.set(ticks='')
axes[0,0].set(title= 'Rome')

axes[1, 1].plot(Barcelona["time"], Barcelona["temperature"], c = 'yellow')

axes[2, 1].plot(Florence["time"], Florence["temperature"], c = 'deepskyblue')

axes[0, 2].plot(Malta["time"], Malta["temperature"], c = 'gold')

axes[1, 2].plot(SanMartinoinPensilis["time"], SanMartinoinPensilis["temperature"], c = 'pink')

axes[2, 2].plot(Budapest["time"], Budapest["temperature"], c = 'violet')

plt.tight_layout()

for ax in axes:
    ax.set_xticks([])



figure.tight_layout()
    
Rome = forecast[forecast["city"]=="Rome"]
