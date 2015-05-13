from pandas import *
from ggplot import *
from datetime import datetime
import numpy as np
import random

def plot_weather_data(turnstile_weather):
    
    pandas.options.mode.chained_assignment = None
    
    df = turnstile_weather
    df.is_copy = False
    
    df_rain = df[(df.rain == 1)]
                
    df_norain = df[(df.rain == 0)].reset_index()
    
    df_rain['freq'] = df_rain.groupby('ENTRIESn_hourly')['ENTRIESn_hourly'].transform('count')
    df_norain['freq'] = df_norain.groupby('ENTRIESn_hourly')['ENTRIESn_hourly'].transform('count') 
    
                                                      
    df['freq'] = df.groupby('ENTRIESn_hourly')['ENTRIESn_hourly'].transform('count') 

     
    plot =  ggplot(df, aes('ENTRIESn_hourly','freq')) +\
            geom_histogram(data=df_rain,binwidth=100,fill='red',color='green',position='identity',alpha=0.2)+\
            geom_histogram(data=df_norain,binwidth=100,fill='blue',color='yellow',position='identity',alpha=0.2)+\
            xlim(0, 7500) +\
            ggtitle('Entries_Hourly for rainy and non rainy days')+xlab('Entries_Hourly')+ylab('Frequency')
    
    #print plot

    return plot


if __name__ == "__main__":

    filename = 'C:/Users/324007232/Documents/D_Drive/Siva Files/Data/Udacity/Project 1/turnstile_weather_v2.csv'
    df = pandas.DataFrame.from_csv(filename, index_col=0)

    #rows = random.sample(df.index, 15000)

    #df_subset = df.ix[rows]
    
    #df_subset = df.iloc[:10000]

    #print len(df_subset)
    
    plot = plot_weather_data(df)

    print plot
