import psycopg2

# Database connection details
db_host = "poc-demo-database.cbqubpabumzf.eu-west-1.rds.amazonaws.com"
db_name = "test_db"
db_user = "postgres"
db_password = "Tatva4848#"

# Table and column details
table_name = "tasks"
column_name = "task_deadline"

# SQL query to drop the column
drop_column_query = f'ALTER TABLE "{table_name}" DROP COLUMN IF EXISTS "{column_name}";'

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

    # Execute the query to drop the column
    cursor.execute(drop_column_query)
    connection.commit()
    print(f"Column '{column_name}' dropped from table '{table_name}' successfully.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection safely
    if connection is not None:
        cursor.close()
        connection.close()
        print("Database connection closed.")
