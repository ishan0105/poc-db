import psycopg2
import os

# Database connection details
db_host = "poc-demo-database.cbqubpabumzf.eu-west-1.rds.amazonaws.com"
db_name = "test_db"
db_user = "postgres"
db_password = "Tatva4848#"

# Table and column details
table_name = "tasks"
column_name = "task_deadline"
column_type = "VARCHAR(255)"  # Adjust as needed

# SQL query to add a column
add_column_query = f'ALTER TABLE "{table_name}" ADD COLUMN "{column_name}" {column_type};'

connection = None  # Initialize connection variable

try:
    # Connect to the database
    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()

    # Execute the query
    cursor.execute(add_column_query)
    connection.commit()
    print(f"Column '{column_name}' added to table '{table_name}' successfully.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection safely
    if connection is not None:
        cursor.close()
        connection.close()
        print("Database connection closed.")