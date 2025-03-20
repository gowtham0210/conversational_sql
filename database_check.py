import sqlite3

conn = sqlite3.connect("student_database.db")
cursor = conn.cursor()
# cursor.execute("SELECT * FROM Departments;")
# rows = cursor.fetchall()
# conn.close()

# for row in rows:
#     print(row)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
conn.close()    
print("Tables in the database:")
for table in tables:
    print(table[0])