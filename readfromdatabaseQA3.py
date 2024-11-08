###pulls database that was  created by databasecreation

import sqlite3

def read_data_from_db(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Retrieve and print all table names from the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Print out all the tables in the database
    print("Tables in the database:")
    for table in tables:
        print(table[0])  # table[0] contains the table name

    # Ask the user which table they want data from
    table_name = input("Enter the name of the table you want data from: ")

    # Retrieve and print all data from the selected table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Check if the table has any data
    if rows:
        print(f"\nData from the '{table_name}' table:")
        for row in rows:
            print(row)
    else:
        print(f"No data found in the '{table_name}' table.")

    # Close the connection
    conn.close()

# Call the function with your database file
read_data_from_db('solar_system_questions.db')
