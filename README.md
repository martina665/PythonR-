# PythonR-

This is our second part of the project of the Python and R LAB. 
We have analysed two datasets: the first was our own dataset retrieved with the first task of this course, about 7 days weather forecast for Rome, Reykjavik, Jerusalem, Barcelona, Lamezia Terme, Florence, Urbania, San Martino in Pensilis, Schiavonea, Berlino','Budapest, Bruxelles, Malta and Paris, the second dataset has been taken from https://github.com/mirocon/Project_Python_R and it is about covid death and cases in 2020 in different countries around the world.

Regarding the covid dataset, we performed the analysis on R software, therefore we create a pdf document (Rmarkdown) with the markdown technique, and for further information about how we analysed data please refer to the document in question.

Regarding the forecast dataset, we performed the following steps to analyse the data and to display some useful graphs about the variables involved:

First we imported the dataset needed for the analysis:

    import pandas as pd
    import os
    import matplotlib.pyplot as plt
    import seaborn as sns

#------------------------------------------------------------

We explored the data taking a glance at the variables, rows and columns of the dataset:

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

