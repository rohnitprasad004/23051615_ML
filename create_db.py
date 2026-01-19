import sqlite3

connection = sqlite3.connect("university.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    branch TEXT,
    year INTEGER,
    cgpa REAL
)
""")

cursor.execute("INSERT INTO students (name, branch, year, cgpa) VALUES ('rahul', 'cse', 3, 8.5)")
cursor.execute("INSERT INTO students (name, branch, year, cgpa) VALUES ('riya', 'civil', 3, 7.8)")
cursor.execute("INSERT INTO students (name, branch, year, cgpa) VALUES ('sagar', 'mech', 4, 7.2)")
cursor.execute("INSERT INTO students (name, branch, year, cgpa) VALUES ('aditya', 'it', 2, 9.0)")

connection.commit()
connection.close()

print("Database created successfully!")
