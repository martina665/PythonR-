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
##### BOXPLOT
# Distribution of covid cases by month
data %>% 
  ggplot(aes(x = month, y = cases, fill = I("skyblue2"))) + 
  geom_boxplot(position = "dodge") +
  labs(x = "") +
  theme_bw() +
  theme(axis.text.x = element_text(angle = 90,  vjust = .4, size = 10))

#Distribution of deaths by month
data%>%
  ggplot(aes(x=month, y=deaths, fill=I("blue")))+
  geom_boxplot(position="dodge")+
  labs(x="")+
  theme_bw()+
  theme(axis.text.x=element_text(angle=90, vjust=.4, size=10))

#visualise changes, changes in number of cases x continent and month
ggplot(data, aes(month, cases))+
  geom_line(aes(group= continent), colour="grey50")+
  geom_point(aes(colour=continent))


#summary statistics
by(data$cases, data$deaths, summary)
by(data$cases, data$deaths, sd)

data %>% 
  group_by(deaths) %>% 
  summarise(
    Minimum = min(cases),
    Q1 = quantile(cases, probs = .25),
    Median = quantile(cases, probs = .5),
    Mean = mean(cases),
    Q3 = quantile(cases, probs = .75),
    Maximum = max(cases),
    SD = sd(cases),
    CV = abs(Mean)/SD,
    IQR = Q3 - Q1
  )
### GROUPED BOXPLOT
# Distribution of cases by continent and month

data%>% 
  filter(
    month %in% c("01", "02", "03", "04", "05","06", "07", "08", "09", "10", "11", "12"),
    grepl("*[aeiouy]$", country)
  ) %>% 
  ggplot(aes(x = continent, y = cases, fill = month)) +
  geom_boxplot(positon = "dodge") +
  theme(legend.position = "top", axis.text.x = element_text(angle = 90))

# Time series for one country 
data %>% filter(country == "Belgium") %>% 
  ggplot(aes(x =date, y = cases, color = date)) + geom_point() + geom_line() +
  scale_y_continuous(labels = scales::percent) +
  theme_bw() +
  theme(legend.position = "bottom")

#DATA MANIPULTION DPLYR
data%>%glimpse
# How many countries?
length(unique(data$country))#214 countries
#or
data %>% distinct(country) %>% nrow

# How many months?
range(data$month)  #from january to december
data%>% distinct(year) #tells the years
#another to way the number of months
length(unique(data$month))

# How many years?
r_ys <- range(data$year)
data %>% distinct(year) %>% nrow
r_ys[2] - r_ys[1] + 1

# How many country-month combinations?
data %>% distinct(country, month) %>% nrow

#DPLYR
#joints
#filtering joins
#set operations
#Imagine that from the "data" I want to select just 
#population cases and deaths
#I can use select() function with dplyr
data2<- select(data, deaths, population, cases)
View(data2)
#rename() function to rename the col, in this case from death to KO
data3<- rename(data2, KO= deaths)
View(data3)

#filter(), if you want a subset data. use filter to retain only
#those values in which death is equal to 10
data4<-filter(data, deaths == "10")
View(data4)