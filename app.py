import streamlit as st # type: ignore
from nl_to_sql import convert_nl_to_sql,clean_sql_output  # Importing the function
import sqlite3
DATABASE_NAME = "student_database.db"
# Streamlit UI
st.title("Conversational SQL Interface")
st.write("Ask your database in natural language!")

# User input
user_query = st.text_input("Enter your query in natural language:")

if st.button("Submit") and user_query:
    # Convert NL query to SQL
    sql_query = convert_nl_to_sql(user_query)
    sql_query = clean_sql_output(sql_query)

    if sql_query:
        st.write("Generated SQL Query:")
        st.code(sql_query, language="sql")

        # Connect to SQLite and execute the query
        try:
            conn = sqlite3.connect(DATABASE_NAME)
            cursor = conn.cursor()
            cursor.execute(sql_query)
            results = cursor.fetchall()

            if results:
                st.write("Query Results:")
                st.dataframe(results)  # Display results in a table
            else:
                st.write("No results found.")

            conn.close()
        except Exception as e:
            st.error(f"Error executing query: {e}")
    else:
        st.error("Failed to generate SQL query.")
