import sqlite3

DATABASE_NAME = "student_database.db"
def get_database_schema(db_path=DATABASE_NAME):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    schema_info = []
    
    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table[0]
        schema_info.append(f"Table: {table_name}\nColumns:")

        # Get column details
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        for col in columns:
            schema_info.append(f"  - {col[1]} ({col[2]})")  # col[1] = column name, col[2] = data type

    conn.close()
    return "\n".join(schema_info)



def execute_query(sql_query):
    conn = sqlite3.connect(DATABASE_NAME)  # Ensure the correct database is used
    cursor = conn.cursor()

    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        conn.commit()
        return result
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close()

if __name__ == "__main__":
      # Creates the database and inserts sample data
    result = execute_query("SELECT * FROM students")  # Fetch all students
    print(result)  # Print the query results
