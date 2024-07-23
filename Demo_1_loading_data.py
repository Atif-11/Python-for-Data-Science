import pandas as pd

# Loading a comma separeted file
data_csv = pd.read_csv("percent-bachelors-degrees-women-usa.csv")
print(data_csv)

# Loading a text file in which records are arranged using a comma
data_txt = pd.read_csv("StudentSchools.txt", header = 0, sep =',')
print(data_txt)

# Loading an excel file include any file from the internet
data_excel = pd.read_excel("file_name.xlsx", sheet_name = "Sheet1")

# Loading a JSON file include any file from the internet
data_json = pd.read_json("file_name.json")

# Loading sql databases include any database from the local environment
import sqlite3
connection_db = sqlite3.connect("database_name.db")
# We can use queries from within inside the python
query_1 = 'SELECT col_1 FROM table_name'
query_2 = 'SELECT * FROM table_name'
data_sql = pd.read_sql(query_2, connection_db)


