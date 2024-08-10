"""
In this file, we create functions to create, and update a database hosted locally.
On pushing to prod we will replace the database url 
We will also need to create a script that runs the update database function from time to time.(say every 10 minutes)


Steps - Connect to locally hosted MySQL
Create a database in the MySQL playground
Decide on the format of the tables. What columns to be present in it and what not
Create required tables in the database(1NF, 2NF, etc depending on the data)

"""

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()
import mysql.connector
from mysql.connector import Error
import os

def connect_to_database():
    """
    Establishes a connection to a MySQL database using environment variables.
    
    Returns:
        connection (mysql.connector.connection.MySQLConnection): The connection object if successful.
        cursor (mysql.connector.cursor.MySQLCursor): The cursor object for executing SQL queries.
        None: If the connection fails.
    """
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),      # Your MySQL server host (localhost for local)
            database=os.getenv('DB_DATABASE'),  # Name of the database you want to connect to
            user=os.getenv('DB_USER'),  # Your MySQL username
            password=os.getenv('DB_PASSWORD')  # Your MySQL password
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"You're connected to the database: {record}")
            return connection, cursor

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None, None

def close_database_connection(connection, cursor):
    """
    Closes the connection to the MySQL database.

    Args:
        connection (mysql.connector.connection.MySQLConnection): The connection object to close.
        cursor (mysql.connector.cursor.MySQLCursor): The cursor object to close.
    """
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    except Error as e:
        print(f"Error while closing the connection to MySQL: {e}")

# Example usage:
connection, cursor = connect_to_database()

if connection and cursor:
    # Perform database operations here
    # ...

    # Close the connection when done
    close_database_connection(connection, cursor)
