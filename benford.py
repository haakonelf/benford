import numpy as np
import pandas as pd
import random
from numpy.random import default_rng
import matplotlib.pyplot as plt
import math


##WIPWIP
#features? ditch certain digits in numbers, and certain data maybe.
#automatically discard first digits not over multiple magnitudes
#as main with input, run plots? no input, show random numbers

# Generates random numbers. Seed however isn't perfect as of yet. 
def numpy_random_data(decimals,min,max,size_1,size_2):

    # Creating the generator.
    seed = random.randint(1, 100)
    generator = default_rng(seed)

    # Tuple size of dimensions, because that is what default rng requires.
    if size_2 > 1:
        dimension_of_data = [size_1,size_2]
    else:
        dimension_of_data = size_1

    # Running it, and scaling from min to max
    data = (max-min) * generator.random(dimension_of_data) + min
    
    return np.round(data,decimals)

def occurence_2_digit_percentage(data):

    # Initialize to zero. Index number of the series denotes the number
    # of occurences of that digit.

    occurence_series = [0 in range(10)]
    print(occurence_series)
    return
    for i, occurence in enumerate(data):
        current_value = occurence_series[occurence]
        occurence_series[occurence]= current_value+1

    return occurence_series



# Prints plots of random series of numbers just to show it. 
def testing_plots():
    
    random_series_data = pd.Series(numpy_random_data(2,0,10,10,1))
    benford = pd.Series(generate_benford_line())
    print(benford)
    plt.plot(benford)
    occurence_2_digit_percentage(random_series_data)
    #plt.plot(occurence_2_digit_percentage(random_series_data))

    #plt.show()




# Generate line of probability of numbers.
def generate_benford_line():
    benford_series = np.zeros(10)
    
    for i in range(1,10):
        probability = math.log10(1+1/i)
        benford_series[i] = probability
    return benford_series

def digit_counter(time_series):

    results = np.zeros(10)

    for i in time_series:
        for j in i:
            print("hey")
            
        
#to check if data is according to benford, and to create benford random numbers
if __name__ == '__main__':
    print("Running as main")
    
    # Presumably other things have been running before
    plt.close("all")
    # Testing the plotting?
    testing_plots()
    
