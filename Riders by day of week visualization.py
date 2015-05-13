from pandas import *
from ggplot import *
from datetime import datetime
import numpy as np
import random

def plot_weather_data(turnstile_weather):
    
    pandas.options.mode.chained_assignment = None
    
    df = turnstile_weather
    df.is_copy = False

    df['day_of_week_alpha'] = df.apply(lambda df:day_of_week(df),axis=1)

       
    plot = ggplot(df, aes(df['day_of_week_alpha'],df['ENTRIESn_hourly']))+geom_bar(size=30)+ggtitle('Ridership by day of week')+xlab('Day of Week')+ylab('ENTRIESn_hourly')
    

    return plot


def day_of_week(df):

    if df['day_week'] == 0:
        return 'Monday'
    if df['day_week'] == 1:
        return 'Tuesday'
    if df['day_week'] == 2:
        return 'Wednesday'
    if df['day_week'] == 3:
        return 'Thursday'
    if df['day_week'] == 4:
        return 'Friday'
    if df['day_week'] == 5:
        return 'Saturday'
    if df['day_week'] == 6:
        return 'Sunday'
    
if __name__ == "__main__":

    filename = 'C:/Users/324007232/Documents/D_Drive/Siva Files/Data/Udacity/Project 1/turnstile_weather_v2.csv'
    df = pandas.DataFrame.from_csv(filename, index_col=0)

    
    plot = plot_weather_data(df)

    print plot


    
