import pandas as pd

# Create a sample DataFrame
data = pd.DataFrame({'Name': ["Anna", "Karen", "John", "Alice", "Kevin", "Sanna", "Bob", "Emily"],
                     'Age': [35, 30, 57, 65, 25, 19, 20, 65],
                     'Salary': [20000, 60000, 145000, 170000, 30000, 10000, 220000, 120000],
                     'Department': ["Tech", "Tech", "Tech", "Healthcare", "Operations", "Operations", "Tech", "Tech"]})

# Ascending: smallest values at the top and values increasing
print(data.sort_values(by= 'Salary', ascending= True))

# Descending: largest values at the top and values decreasing
print("\n", data.sort_values(by= 'Salary', ascending= False))

# Group data on the basis of department
print("\n", data.groupby("Department")["Name"].count())

# Average salary per department
print("\n", data.groupby("Department")["Salary"].mean())

# Minimum and maximum salary of each department
print("\n", data.groupby("Department")["Salary"].min())
print("\n", data.groupby("Department")["Salary"].max())

# Filtering based on specific material
print("\n",data[data["Salary"] > 100000])

# Multiple filtering
print("\n", data[(data["Salary"] > 100000) & (data["Salary"] < 200000)])

# Multiple filtering with integers
print("/n", data[data["Age"].isin([20, 65])])
