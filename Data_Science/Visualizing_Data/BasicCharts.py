from plotnine import *
from plotnine.data import diamonds
import pandas as pd
import numpy as np

# Show the head of the dataset
print(diamonds.head())

# Show the tail of the dataset
print(diamonds.tail())

# How big is the dataset?
print("Length of dataset: " + str(len(diamonds)))

# Building a quick plot
print(qplot(x='price', data=diamonds))

#print(ggplot(diamonds) + geom_bar(aes(x='cut')))
#print(ggplot(diamonds) + geom_bar(aes(x='price')))
print(ggplot(diamonds) + geom_jitter(aes(x='price', y='carat')))


# Create a seperate line for each clarity
print(ggplot(diamonds, aes(x='price', color='clarity')) + \
    geom_density())