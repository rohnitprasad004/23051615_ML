import pandas as pd
import sqlite3

# connect to database
connection = sqlite3.connect("university.db")

# read table into dataframe
df = pd.read_sql_query("SELECT * FROM students", connection)

print(df)

connection.close()
