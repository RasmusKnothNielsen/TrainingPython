from plotnine import *
from plotnine.data import diamonds
import pandas as pd
import numpy as np

# Let's start with a scatterplot
print(ggplot(aes(x='carat', y='price'), data=diamonds) + geom_point())

# Now let's add a color
print(ggplot(aes(x='carat', y='price', color='clarity'), data=diamonds) + geom_point())

# Use color brewer for better options
# Start with a sequential color range
print(ggplot(aes(x='carat', y='price', color='clarity'), data=diamonds) + \
      geom_point() + \
      scale_color_brewer(type='seq', palette='Reds'))

# Let's try a diverging color palette
print(ggplot(aes(x='carat', y='price', color='clarity'), data=diamonds) + \
      geom_point() + \
      scale_color_brewer(type='div', palette=2))

# Lastly, try a qualitative palette
print(ggplot(aes(x='carat', y='price', color='clarity'), data=diamonds) + \
      geom_point() + \
      scale_color_brewer(type='qual'))
