import pandas as pd
import sqlite3


connection = sqlite3.connect("university.db")


df = pd.read_sql_query("SELECT * FROM students", connection)

print(df)

connection.close()
