import mysql.connector
from mysql.connector import Error

# 1. This function connects to the database (what you did earlier)
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="9951146683", # Make sure to change this back to 9951146683 if it doesn't copy over
            database="slot_booking"
        )
        print("Success! Connected to the database.")
        return connection
    except Error as e:
        print(f"Error: '{e}' occurred")
        return None

# 2. This NEW function acts as our messenger to fetch the slots
def get_available_slots(connection):
    cursor = connection.cursor(dictionary=True) # Creates the messenger
    cursor.execute("SELECT * FROM slots WHERE booked = 0;") # Gives it the SQL command
    records = cursor.fetchall() # Grabs all the results
    
    print("\n--- Available Time Slots ---")
    for row in records:
        # Prints out each slot one by one
        print(f"Slot ID: {row['id']} | Time: {row['slot_time']}")

# 3. This is the main starting point of the script
if __name__ == "__main__":
    conn = create_connection() # Connect first
    if conn:
        get_available_slots(conn) # If connection worked, fetch the slots!