# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:38:11 2021

@author: cosim
"""

#Import the library we need

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

#import the dataset (please note to change the directory coherently with the computer in use)

forecast = pd.read_csv("C:/Users/marti/PythonProject/covid/PythonR-/Forecast_merged.csv")
os.chdir("C:/Users/marti/PythonProject/covid/PythonR-")

#%%

#Display some info to explore the data

print(forecast.info)

print(forecast["city"].value_counts())

print(forecast.describe())

#%%

#Plotting the temperatures for all the cities in the last 7 days in one plot

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

#%%

#Jerusalem Pressure

plt.plot(Jerusalem.time, Jerusalem.pressure)
plt.title('Pressure evolution in Jerusalem')
plt.xlabel('Time')
plt.ylabel('Pressure')
plt.xticks('')
plt.show()

#%%

#One graph with three lines for Paris and Reykjavik temperature, precpitation and dewpoint
plt.title('Paris dew-temp-prec')
plt.plot(Paris.time, Paris.temperature, 'r.-')
plt.plot(Paris.time, Paris.precipitation, 'b.-')
plt.plot(Paris.time, Paris.dewpoint, 'g.-')
plt.xticks('')
plt.xlabel('time')
labels= 'temperature', 'precipitation', 'dewpoint'
plt.legend(labels)
plt.show()


plt.title('Reykjavik dew-temp-prec')
plt.plot(Reykjavik.time, Reykjavik.temperature, 'r.-')
plt.plot(Reykjavik.time, Reykjavik.precipitation, 'b.-')
plt.plot(Reykjavik.time, Reykjavik.dewpoint, 'g.-')
labels= 'temperature', 'precipitation', 'dewpoint'
plt.xticks('')
plt.xlabel('Time')
plt.legend(labels)
plt.show()

#Histogram for the dewpoint values in Rome

plt.hist(Rome['dewpoint'], bins = 30)
plt.title('Distribution of dewpoint values in Rome')
plt.show()

#Histogram for the dewpoint values in Rome

plt.hist(Malta['relative humidity'], bins=50)
plt.title('Distribution of relative humidity in Malta')
plt.show()

#%%

#Correlation matrix

corr = forecast.corr()
print(corr)

#Plot of the correlation matrix using matplotlib.pyplot library
plt.matshow(corr)
plt.title('Correlation matrix')

#Plot of the correlation matrix using seaborn library
cormap = sns.heatmap(corr, annot=True)


#%%
#pandas manipulation

#Rename col
forecast.rename(mapper=None, index=None, columns={'pressure': 'pressione', 'temperature':'temp'}, axis=None, copy=True, inplace=False, level=None, errors='ignore')

#Sort columns
forecast.sort_values(by= 'temperature') 

#sort by position
forecast.loc[2], ['dewpoint']












