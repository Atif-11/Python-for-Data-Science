import numpy as np
import pandas as pd
from scipy import stats

data = [100, 20, 5, 20, 45, -100, 46]
# Find the mean of given data
mean_ = np.mean(data)
print("Mean of array:", mean_)

# Whenever the median is different from mean, it means that you are dealing with skewed distribution
median_ = np.median(data)
print("Median of array is:", median_)

# Mode is the most repeated value inside your data
mode_ = stats.mode(data)
print("Mode of array:", mode_)

# Variance and standard deviation help us get an idea of deviation of data from the mean value
variance_ = np.var(data)
print("Variance of array:", variance_)

std_ = np.std(data)
print("Standard deviation of array:", std_)

# To get the descriptive statistics of a data frame
data_csv = pd.read("perccent-bachelors-degrees-women-usa.csv")
print(data_csv.describe())