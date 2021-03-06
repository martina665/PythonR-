# PythonR-

This is our second part of the project of the Python and R LAB. 
We have analysed two datasets: the first was our own dataset retrieved with the first task of this course, about 7 days weather forecast for Rome, Reykjavik, Jerusalem, Barcelona, Lamezia Terme, Florence, Urbania, San Martino in Pensilis, Schiavonea, Berlino, Budapest, Bruxelles, Malta and Paris, the second dataset has been taken from https://github.com/mirocon/Project_Python_R and it is about covid death and cases in 2020 in different countries around the world.

Regarding the covid dataset, we performed the analysis on R software, therefore we create a pdf document (Rmarkdown) with the markdown technique, for further information about how we analysed data please refer to the document in question.

Regarding the forecast dataset, we performed on Python the following steps to analyse the data and to display some useful graphs about the variables involved:

First we imported the libraries needed for the analysis:

    import pandas as pd
    import os
    import matplotlib.pyplot as plt
    import seaborn as sns

#------------------------------------------------------------

Then we imported the dataset:

        forecast = pd.read_csv("C:/Users/cosim/Desktop/Querini/PythonR-/Forecast_merged.csv")
        os.chdir("C:/Users/cosim/Desktop/Querini/PythonR-")
        
#------------------------------------------------------------

We explored the data taking a glance on the variables, rows and columns of the dataset:

    print(forecast.info)
    
    print(forecast["city"].value_counts())
    
    print(forecast.describe()) 

#------------------------------------------------------------

We started to display the values, starting with plotting the evolution of the temperatures for each city in the dataset, giving a different colour to each line, representing a city, with the help of a dictionary:

    colors = {'Rome':'red', 'Reykjavik':'blue','Jerusalem':'brown','Barcelona':'yellow','Lamezia Terme':'purple','Florence':'deepskyblue','Urbania':'black',
          'San Martino in Pensilis':'pink','Schiavonea':'green','Berlino':'lime','Budapest':'violet','Bruxelles':'sandybrown','Malta':'gold',
          'Parigi':'indigo'}


    ax = forecast.plot( kind="scatter", x="time", y="temperature", c = forecast["city"].map(colors))
    plt.xticks('')
    plt.tight_layout()
    plt.savefig( "Temepratures")
    plt.show()
    

#------------------------------------------------------------

Since from the graphs above we can not properly see anything, we created another plot sublotting 9 different graphs for 9 different cities, again with the evolution of temperatures through 7 days. Before that, we created a sub-dataset containing only the observations relatives to each of the 9 cities:

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

#------------------------------------------------------------

We displaied the evolution of the atmospheric pressure in Jerusalem using a scatter-plot:

        plt.plot(Jerusalem.time, Jerusalem.pressure)
        plt.title('Pressure evolution in Jerusalem')
        plt.xlabel('Time')
        plt.ylabel('Pressure')
        plt.xticks('')
        plt.show()
        
#------------------------------------------------------------

Again with a scatterplot, we displaied together the evolution of dewpoint with temperature and precipitations for Paris and Reykjavik: 

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
        
#------------------------------------------------------------

Then we plotted the distributions of dewpoint and relative humidity respectively for Rome and Malta, using a histogram since we deal with continuous variables:

        plt.hist(Rome['dewpoint'], bins = 30)
        plt.title('Distribution of dewpoint values in Rome')
        plt.show()

        plt.hist(Malta['relative humidity'], bins=50)
        plt.title('Distribution of relative humidity in Malta')
        plt.show()
        
#------------------------------------------------------------

The last plot was about the correlation matrix between all the variables in the dataset. To plot the correlation, we first used matshow from matplotlib library and after heatmap from seaborn:

        corr = forecast.corr()
        print(corr)

        plt.matshow(corr)
        plt.title('Correlation matrix')

        cormap = sns.heatmap(corr, annot=True)
        
#------------------------------------------------------------

In the end, we performed some manipulations on the dataset using pandas library:

        forecast.rename(mapper=None, index=None, columns={'pressure': 'pressione', 'temperature':'temp'}, axis=None, copy=True, inplace=False, level=None, errors='ignore')

        forecast.sort_values(by= 'temperature') 

        forecast.loc[2], ['dewpoint']
