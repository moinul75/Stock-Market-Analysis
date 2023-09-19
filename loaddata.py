import sqlite3
import json

# Define a function to load JSON data into SQLite3
def load_data_from_json(json_file, db_file, table_name):
    # Read JSON data from the file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Connect to the SQLite3 database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "date TEXT, "
                "trade_code TEXT, "
                "high REAL, "
                "low REAL, "
                "open REAL, "
                "close REAL, "
                "volume TEXT)")


    for entry in data:
        volume = entry['volume']
        open_value = entry['open']
        high = entry['high']
        low = entry['low']
        close = entry['close']
        cursor.execute(f"INSERT INTO {table_name} (date, trade_code, high, low, open, close, volume) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (entry['date'], entry['trade_code'], high,
                        low, open_value, close, volume))


    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Specify the JSON file, SQLite3 database file, and table name
json_file = 'stock_market_data.json'
db_file = 'db.sqlite3'
table_name = 'JanataWifi_stock'

# Call the function to load data from JSON to SQLite3
load_data_from_json(json_file, db_file, table_name)

print("Data loaded successfully.")