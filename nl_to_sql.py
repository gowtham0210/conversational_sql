import ollama
from database import execute_query,get_database_schema
import re
import sqlite3

DATABASE_NAME = "student_database.db"
def convert_nl_to_sql(natural_query):
    schema_info = get_database_schema(DATABASE_NAME)  # Dynamically fetch schema

    prompt = f"""{schema_info}
    Convert the following natural language query into SQL for an SQLite database:
    
    Query: {natural_query}
    
    SQL:

    No explanation is required only return SQL query alone and it should be ready to executable query.

    For example
    Query: count total number of students
    SQL: select count(*) from students;

    """
    response = ollama.chat(model="gemma3:4b", messages=[{"role": "user", "content": prompt}])
    sql_query = response["message"]["content"]
    print("----prompt-----------------")
    print(prompt)
    print("----sql query by llm-----------------")
    print(sql_query)
    return sql_query.strip()

def clean_sql_output(sql_query):
    """Cleans SQL output by removing markdown formatting, unwanted prefixes, and extra spaces."""
    sql_query = sql_query.strip()

    # Remove common SQL markdown formatting (both ```sql and ```sqlite)
    sql_query = re.sub(r"```(?:sql|sqlite)\n?", "", sql_query, flags=re.IGNORECASE)

    # Remove unwanted words like "ite" (from incorrect SQL extraction)
    sql_query = re.sub(r"^\s*(sql|sqlite|ite)\s*", "", sql_query, flags=re.IGNORECASE)

    # Remove trailing triple backticks if they exist
    sql_query = re.sub(r"\n?```$", "", sql_query)

    return sql_query.strip()


def process_user_query(nl_query):
    sql_query = convert_nl_to_sql(nl_query)
    sql_query = clean_sql_output(sql_query)
    print("Generated SQL:", sql_query)

    results = execute_query(sql_query)
    print("Query Results:", results)
    return results

def get_table_names():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()    
    print("Tables in the database:")
    for table in tables:
        print(table[0])

if __name__ == "__main__":
    print("-----Table Name------------------")
    get_table_names()
    user_input = "List all department names"
    print("----query result-----------------")
    process_user_query(user_input)