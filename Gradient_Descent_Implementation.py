import numpy as np
import pandas
from ggplot import *
import random


def normalize_features(df):
    """
    Normalize the features in the data set.
    """
    mu = df.mean()
    sigma = df.std()
    
    if (sigma == 0).any():
        raise Exception("One or more features had the same value for all samples, and thus could " + \
                         "not be normalized. Please do not include features with only a single value " + \
                         "in your model.")
    df_normalized = (df - df.mean()) / df.std()

    return df_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, 
    and the values for our thetas.
    
    """
    
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    
    """
    
    m = len(values)
    cost_history = []

    for i in range(num_iterations):
        # your code here
        predicted_values = np.dot(features, theta)
        theta = theta + (alpha/m)*np.dot((values - predicted_values),features)
        cost_history.append(compute_cost(features, values, theta))
        
    return theta, pandas.Series(cost_history)

def predictions(dataframe):
    '''
    Uses the improved dataset provided for the project at the Udacity dropbox location
    '''
    
    # Select Features (try different features!)
    features = dataframe[['rain','hour', 'weekday']]
                
    # Add conds to features using dummy variables
    dummy_conds = pandas.get_dummies(dataframe['conds'], prefix='conds')
    features = features.join(dummy_conds)
      
    # Add station to features using dummy variables
    dummy_station = pandas.get_dummies(dataframe['station'], prefix='station')
    features = features.join(dummy_station)
     
    # Add UNIT to features using dummy variables
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)

    # Values
    values = dataframe['ENTRIESn_hourly']
    m = len(values)

    features, mu, sigma = normalize_features(features)
    features['ones'] = np.ones(m) # Add a column of 1s (y intercept)
    
    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values)

        
    # Set values for alpha, number of iterations.
    alpha = 0.1 # please feel free to change this value
    num_iterations = 30 # please feel free to change this value

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    
    theta_gradient_descent, cost_history = gradient_descent(features_array, 
                                                            values_array, 
                                                            theta_gradient_descent, 
                                                            alpha, 
                                                            num_iterations)

       
    plot = None
    # -------------------------------------------------
    # Uncomment the next line to see your cost history
    # -------------------------------------------------
    #plot = plot_cost_history(alpha, cost_history)
    # 
    # Please note, there is a possibility that plotting
    # this in addition to your calculation will exceed 
    # the 30 second limit on the compute servers.

    predictions = np.dot(features_array, theta_gradient_descent)
    #return predictions, plot
    
    #print plot

    return predictions
    

def plot_cost_history(alpha, cost_history):
   """This function is for viewing the plot of your cost history.
   You can run it by uncommenting this

       plot_cost_history(alpha, cost_history) 

   call in predictions.
   
   If you want to run this locally, you should print the return value
   from this function.
   """
   cost_df = pandas.DataFrame({
      'Cost_History': cost_history,
      'Iteration': range(len(cost_history))
   })
   return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
      geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha )


if __name__ == "__main__":
    
    filename = 'C:/Users/324007232/Documents/D_Drive/Siva Files/Data/Udacity/Project 1/turnstile_weather_v2.csv'

    df = pandas.DataFrame.from_csv(filename, index_col=None)

    #rows = random.sample(df.index, 25000)

    #df_subset = df.ix[rows]

    #print len(df_subset)
    
    df_subset = df.iloc[:25000]
    
    predictions = predictions(df_subset)

    df_mean = np.mean(df_subset['ENTRIESn_hourly'])

      
    data_array = np.array(df_subset['ENTRIESn_hourly'])
    
    numerator = np.square(data_array - predictions).sum()
        
    denominator = np.square(data_array - df_mean).sum()
       
    r_square = 1 - (numerator/denominator)

    print r_square
