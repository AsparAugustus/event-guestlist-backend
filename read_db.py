import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('guests.db')
cursor = conn.cursor()

# Execute a SELECT query to fetch all values from a table
cursor.execute('SELECT * FROM guests')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the fetched values
for row in rows:
    print(row)

# Close the database connection
conn.close()