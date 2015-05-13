import numpy as np
import scipy
import scipy.stats
import pandas
from ggplot import *

def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data. 
       
    '''
              
    with_rain_mean = np.mean(turnstile_weather[turnstile_weather.rain==1]['ENTRIESn_hourly'])
    without_rain_mean = np.mean(turnstile_weather[turnstile_weather.rain==0]['ENTRIESn_hourly'])

              
    MW_tuple = scipy.stats.mannwhitneyu(turnstile_weather[turnstile_weather.rain==1]['ENTRIESn_hourly'],turnstile_weather[turnstile_weather.rain==0]['ENTRIESn_hourly'])
    U=MW_tuple[0]
    p=MW_tuple[1]
    
    return with_rain_mean, without_rain_mean, U, p


if __name__ == "__main__":

    filename = 'C:/Users/324007232/Documents/D_Drive/Siva Files/Data/Udacity/Project 1/turnstile_weather_v2.csv'

    df = pandas.DataFrame.from_csv(filename, index_col=0)
    
    with_rain_mean, without_rain_mean, U, p = mann_whitney_plus_means(df)

    print with_rain_mean
    print without_rain_mean
    print U
    print p
