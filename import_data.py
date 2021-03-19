#import all the necessary libraries

%matplotlib inline
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})

#import the data set
data = pd.read_csv("college data set - Sheet2.csv", sep=',')
salary = data["Starting Median Salary"]
data.head(7)
