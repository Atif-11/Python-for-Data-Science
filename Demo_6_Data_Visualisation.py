import matplotlib.pyplot as plt
x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [1,4,6,8,10,12,14,16,18,20]

# Line plots
plt.plot(x_values, y_values, color = 'green')
plt.xlabel("X-axis placeholder")
plt.ylabel("Y-axis placeholder")
plt.title("Title Placeholder")
# plt.show()

# Scatter plots: Visualise the correlation between two features
plt.scatter(x_values, y_values, color='green')
plt.xlabel("X-axis placeholder")
plt.ylabel("Y-axis placeholder")
plt.title("Title Placeholder")
# plt.show()

# Barcharts, handy for categorical data
cat = ["cat", "dog", "horse", "mouse"]
cat_value = [10, 30, 100, 1]

plt.bar(cat, cat_value, color='forestgreen')
plt.xlabel("Animals")
plt.ylabel("Weight of an Animal")
plt.title("Weight per Animal")
plt.show()

# Histograms: Visualisation of sample data (Distribution)
import numpy as np
X_normal = np.random.normal(0, 1, 1000)
plt.hist(X_normal, color='forestgreen')
plt.xlabel("X")
plt.ylabel("Frequency")
plt.title("Randomly Sampled Data from Standard Normal Distribution")
plt.show()

# Population distribution
from scipy.stats import norm
x_values = np.arange(-5, 5, 0.01)
y_values = norm.pdf(x_values)

counts, bins, ignored = plt.hist(X_normal, 30, density = True, color='purple', label='Sampling Distribution')
plt.plot(x_values, y_values, color='y', linewidth = 2.5, label = 'Population Distribution')
plt.title("Randomly generating 1000 obs from Normal Distribution mu = 0, sigma = 1")
plt.ylabel("Probability")
plt.legend()
plt.show()
