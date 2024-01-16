
import pyodbc
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

import os

server = os.getenv("server")
database = os.getenv("database")
username= os.getenv("user_name")
password = os.getenv("password")

print(server,database,username,password)



# Construct the connection string
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Establish a connection
    connection = pyodbc.connect(connection_string)

    # Create a cursor
    cursor = connection.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM table_A AS A JOIN table_B AS B ON A.emp_id = B.emp_id")

    # Fetch the results
    results = cursor.fetchall()

    # Print the column headers
    columns = [column[0] for column in cursor.description]
    print("\t".join(columns))
    # Print the data rows
    for row in results:
        # Format each row as a tab-separated string
        formatted_row = "\t".join(map(str, row))
        print(formatted_row)

    # Close the cursor and connection when you're done
    cursor.close()
    connection.close()

except pyodbc.Error as e:
    print(f"An error occurred: {e}")