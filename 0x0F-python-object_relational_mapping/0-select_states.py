#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Parse command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL server on localhost
        db = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database,
            host='localhost',
            port=3306
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id")

        # Fetch all the results
        states = cursor.fetchall()

        # Display the states
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()
