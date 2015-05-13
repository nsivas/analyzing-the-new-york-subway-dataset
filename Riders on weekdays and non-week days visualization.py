from pandas import *
from ggplot import *
from datetime import datetime
import numpy as np
import random

def plot_weather_data(turnstile_weather):
    

    pandas.options.mode.chained_assignment = None
    
    df = turnstile_weather
    df.is_copy = False
    
    df_weekday = df[(df.weekday == 1)]
                
    df_nonweekday = df[(df.weekday == 0)].reset_index()
    
        
    df_weekday['freq'] = df_weekday.groupby('ENTRIESn_hourly')['ENTRIESn_hourly'].transform('count')
    df_nonweekday['freq'] = df_nonweekday.groupby('ENTRIESn_hourly')['ENTRIESn_hourly'].transform('count')
    
                                                      
    df['freq'] = df.groupby('ENTRIESn_hourly')['ENTRIESn_hourly'].transform('count')

      
     
    plot = ggplot(df, aes('ENTRIESn_hourly','freq')) +\
           geom_histogram(data=df_weekday,binwidth=100,fill='red',color='green',position='identity',alpha=0.2) +\
           geom_histogram(data=df_nonweekday,binwidth=100,fill='blue',color='yellow',position='identity',alpha=0.2) +\
           xlim(0, 7500) +\
           ggtitle('Ridership on weekdays and non-weekdays')+xlab('Entries_Hourly')+ylab('Frequency')
    

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
