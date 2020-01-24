from plotnine import *
from plotnine.data import mpg
import pandas as pd
import numpy as np

# Let's start with a scatterplot
print(ggplot(mpg, aes(x='cty', y='hwy')) + geom_point())

# Let's add a title
print(ggplot(mpg, aes(x='cty', y='hwy')) + geom_point() +
      ggtitle("City vs. Highway Miles pr Gallon"))

# Now let's add some custom labels
print(ggplot(mpg, aes(x='cty', y='hwy')) + geom_point() +
      ggtitle("City vs. Highway Miles pr Gallon") +
      xlab("City MPG (Miles per Gallon)") +
      ylab("Highway MPG (Miles per Gallon)"))

# Color might help here
print(ggplot(mpg, aes(x='cty', y='hwy', color='class')) + geom_point() +
      ggtitle("City vs. Highway Miles pr Gallon") +
      xlab("City MPG (Miles per Gallon)") +
      ylab("Highway MPG (Miles per Gallon)") +
      scale_color_brewer(type='qual'))

# How about splitting these out?
print(ggplot(mpg, aes(x='cty', y='hwy', color='class')) + geom_point() +
      ggtitle("City vs. Highway Miles pr Gallon") +
      xlab("City MPG (Miles per Gallon)") +
      ylab("Highway MPG (Miles per Gallon)") +
      scale_color_brewer(type='qual') +
      facet_wrap(('year', 'cyl')))