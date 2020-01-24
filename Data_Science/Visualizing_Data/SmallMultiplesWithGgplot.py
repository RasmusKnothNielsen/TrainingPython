from plotnine import *
from plotnine.data import diamonds
import pandas as pd
import numpy as np

# Now lets build a quick plot
print(qplot(x='price', data=diamonds))

# Create a Facets (trellis) for our chart
print(qplot(x='price', data=diamonds) + facet_wrap('clarity'))

# Lets organize these better into a grid
print(qplot(x='price', data=diamonds) + facet_grid(('clarity', 'cut')))

# Lets look at Anscombe's Quartet
aq = pd.read_csv('../Data/anscombes-quartet-hier.csv', header=[0,1],index_col=[0])
print(aq)

print(aq.mean())
print(aq.var())

df = pd.read_csv('../Data/anscombes-quartet.csv', header=0, index_col=0)

print(ggplot(aes(x='x', y='y'), data=df)+geom_point()+facet_wrap('group'))
