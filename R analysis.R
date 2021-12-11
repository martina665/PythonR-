library(readr)
library(ggplot2)
library(dplyr)
library(tidyr)
covid <- read_csv("covid.csv")
View(covid)
data<- covid[,-1]
View(data)

#DATA VISUALIZATION WITH GGPLOT 
data%>% glimpse
#The dataset is made of 12 columns and 61,900 rows, I excluded the index
#the range(year) function gives informations about the year range, which in this case is 2020
range(data$year) #2020
data%>% distinct(year)
length(unique(data$country)) #there are 214 countries in the dataset
data%>% distinct(year, cases)
#Checking for missing values
sum(is.na(data$deaths))
sum(is.na(data$cases))
length(unique(data$continent))

##### HISTOGRAMS
# Marginal distribution of cases_cum 
phist <- data %>% 
  ggplot(
    aes(x = cases_cum, y = ..density.., color = I("white"), fill = I("skyblue2"))
  ) +
  geom_histogram() +
  theme_bw()

plotly::ggplotly(phist)

#Comparing distribution of covid-cases by country

data%>% 
  filter(country %in% c("Belgium", "Spain")) %>% 
  ggplot(
    aes(x = cases_cum, y = ..density.., color = I("white"), fill = country)
  ) +
  geom_histogram(alpha = 0.6, position = "identity") +
  scale_fill_manual(values = c("grey60", "darkorange")) +
  theme_bw()

#Comparing distribution of covid-deaths by country
data %>%
  filter(country %in% c("Belgium", "Spain"))%>%
  ggplot(
    aes(x= deaths_cum, y= ..density.., color=I("white"), fill=country)
  )+
  geom_histogram(alpha=0.6, position="identity")+
  scale_fill_manual(values=c("grey60", "darkorange"))+
  theme_bw()

#deatsh in one country
data%>%
  filter(country%in% c("Belgium"))%>%
  ggplot(
    aes(x= deaths, y=..density.., color=I("white"), fill=country)
  )+
  geom_histogram(alpha=0.6, position="identity")+
  scale_fill_manual(values=c("grey60", "darkorange"))+
  theme_bw()