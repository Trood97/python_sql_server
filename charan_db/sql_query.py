
import pyodbc
import pandas as pd

server= "216.48.178.172,14533"
database= "RPG_Icodex"
username="powerbi@user"
password= "1qaz!QAZ"

# Construct the connection string
def exectute_sql_query(query):
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        # Establish a connection
        connection = pyodbc.connect(connection_string)

        # Create a cursor
        cursor = connection.cursor()

        # Execute the SQL query
        #cursor.execute("SELECT * FROM table_A AS A JOIN table_B AS B ON A.emp_id = B.emp_id")
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results






        # Print the column headers
        columns = [column[0] for column in cursor.description]
        #print("\t".join(columns))
        # Print the data rows
        formatted_row = ''
        for row in results:
            # Format each row as a tab-separated string
            formatted_row = "\t".join(map(str, row))
            #print(formatted_row)
        return formatted_row
        # Close the cursor and connection when you're done


    except pyodbc.Error as e:
        print(f"An error occurred: {e}")

#print(exectute_sql_query("select count(pagecount) from dbo.tbjobmaster where "))