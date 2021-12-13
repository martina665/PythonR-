# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:38:11 2021

@author: cosim
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

forecast = pd.read_csv("C:/Users/marti/PythonProject/covid/PythonR-/Forecast_merged.csv")
os.chdir("C:/Users/marti/PythonProject/covid/PythonR-")

#%%

print(forecast.info)

print(forecast["city"].value_counts())

print(forecast.describe())

#%%

#Plotting the temperatures for all the cities in the last 7 days in one plot

#unique_list = list(dict.fromkeys(inp_list))

cities = list(dict.fromkeys(forecast["city"]))

colors = {'Rome':'red', 'Reykjavik':'blue','Jerusalem':'brown','Barcelona':'yellow','Lamezia Terme':'purple','Florence':'deepskyblue','Urbania':'black',
          'San Martino in Pensilis':'pink','Schiavonea':'green','Berlino':'lime','Budapest':'violet','Bruxelles':'sandybrown','Malta':'gold',
          'Parigi':'indigo'}


ax = forecast.plot( kind="scatter", x="time", y="temperature", c = forecast["city"].map(colors))
plt.xticks('')
plt.tight_layout()
plt.savefig( "Temepratures")
plt.show()

#%%

#Plot of temperatures for 9 cities using subplots

Rome = forecast[forecast["city"]=="Rome"]
Paris = forecast[forecast["city"]=="Parigi"]
Reykjavik = forecast[forecast["city"]=="Reykjavik"]
Jerusalem = forecast[forecast["city"]=="Jerusalem"]
Barcelona = forecast[forecast["city"]=="Barcelona"]
Florence = forecast[forecast["city"]=="Florence"]
Malta = forecast[forecast["city"]=="Malta"]
SanMartinoinPensilis = forecast[forecast["city"]=="San Martino in Pensilis"]
Budapest = forecast[forecast["city"]=="Budapest"]

figure, axes = plt.subplots(nrows=3, ncols=3, dpi = 300)

axes[0, 0].plot(Rome["time"], Rome["temperature"], c = 'red')
axes[0,0].xaxis.set(ticks='')
axes[0,0].set(title= 'Rome', xlabel = 'time', ylabel = 'temp')

axes[1, 0].plot(Paris["time"], Paris["temperature"], c = 'indigo')
axes[1,0].xaxis.set(ticks='')
axes[1,0].set(title= 'Paris', xlabel = 'time', ylabel = 'temp')

axes[2, 0].plot(Reykjavik["time"], Reykjavik["temperature"], c = 'blue')
axes[2,0].xaxis.set(ticks='')
axes[2,0].set(title= 'Reykjavik', xlabel = 'time', ylabel = 'temp')

axes[0, 1].plot(Jerusalem["time"], Jerusalem["temperature"], c = 'brown', )
axes[0,1].xaxis.set(ticks='')
axes[0,1].set(title= 'Jerusalem', xlabel = 'time', ylabel = 'temp')

axes[1, 1].plot(Barcelona["time"], Barcelona["temperature"], c = 'yellow')
axes[1,1].xaxis.set(ticks='')
axes[1,1].set(title= 'Barcelona', xlabel = 'time', ylabel = 'temp')

axes[2, 1].plot(Florence["time"], Florence["temperature"], c = 'deepskyblue')
axes[2,1].xaxis.set(ticks='')
axes[2,1].set(title= 'Florence', xlabel = 'time', ylabel = 'temp')

axes[0, 2].plot(Malta["time"], Malta["temperature"], c = 'gold')
axes[0,2].xaxis.set(ticks='')
axes[0,2].set(title= 'Malta', xlabel = 'time', ylabel = 'temp')

axes[1, 2].plot(SanMartinoinPensilis["time"], SanMartinoinPensilis["temperature"], c = 'pink')
axes[1,2].xaxis.set(ticks='')
axes[1,2].set(title= 'San Martino in Pensilis', xlabel = 'time', ylabel = 'temp')

axes[2, 2].plot(Budapest["time"], Budapest["temperature"], c = 'violet')
axes[2,2].xaxis.set(ticks='')
axes[2,2].set(title= 'Budapest', xlabel = 'time', ylabel = 'temp')

plt.tight_layout()
plt.savefig('temp_merg')
plt.show()


temp = plt.plot(Barcelona.temperature, Barcelona.dewpoint)
plt.show

plt.plot(Jerusalem.time, Jerusalem.pressure)
plt.show()
#One graph with three lines for Paris temperature, precpitation and dewpoint
plt.title('Paris dew-temp-prec')
plt.plot(Paris.time, Paris.temperature, 'r.-')
plt.plot(Paris.time, Paris.precipitation, 'b.-')
plt.plot(Paris.time, Paris.dewpoint, 'g.-')
plt.xticks(Paris.time)
plt.show()





#%%

#Correlation matrix

corr = forecast.corr()
print(corr)

plt.matshow(corr)

cormap = sns.heatmap(corr, annot=True)

#%%