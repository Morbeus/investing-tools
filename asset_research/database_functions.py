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

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host = os.getenv("DB_HOST"),      # Your MySQL server host (localhost for local)
        database=os.getenv('DB_DATABASE'),  # Name of the database you want to connect to, in MySQL Workbench this is the schema name
        user=os.getenv('DB_USER'),  # Your MySQL username, usually root if locally hosted
        password=os.getenv('DB_PASSWORD')  # Your MySQL password
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected to MySQL Server version {db_info}")
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print(f"You're connected to the database: {record}")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")