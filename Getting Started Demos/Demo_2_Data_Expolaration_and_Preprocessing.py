import pandas as pd

# 1. Data Exploration
# Loading CSV file with header 
data_csv = pd.read_csv("percent-bachelors-degrees-women-usa.csv")
# Try using different parameters inside head() and tail()
print(data_csv.head())
print(data_csv.tail())
# Provide the information like column name, null count and type
print(data_csv.info())

# 2. Data Preprocessing
# Drop the NA field
print(data_csv.dropna())
# Fill NAs with NULL
print(data_csv.fillna("NULL"))
# Remove all duplicates from your data frame
data_csv.drop_duplicates()

# Accessing certain rows
print(data_csv.iloc[10]) # iloc is for integers (positions)

# loc is for labels or strings
data = pd.DataFrame({'A1': [1, 2, 3],
                     'A2': [4, 5, 6],
                     'A3': [7, 8, 9]},
                     index=['X', 'Y', 'Z'])

print(data)

print(data.loc["X"])

print(data.loc[:, 'A2'])

print(data.loc['Y', 'A2'])