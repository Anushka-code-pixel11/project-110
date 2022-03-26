import plotly.figure_factory as ff
import csv
import plotly.graph_objects as go
import random
import pandas as pd
import statistics

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

def random_setOfMeans(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        data_set.append(value)
        mean = statistics.mean(data_set)
        return mean

def show_fig(meanList):
    df = meanList
    #mean = statistics.mean(df)
    fig = ff.create_distplot([df],["reading_time"],show_hist = False)
    #fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "Mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_setOfMeans(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("sampling mean : ", mean)


setup() 
population_mean = statistics.mean(data)
print("population mean : ", population_mean)
