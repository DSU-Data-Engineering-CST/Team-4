# load.py

import pymysql
from config import DB_CONFIG

# --------------------------------------
# Save DataFrame to MySQL
# --------------------------------------
def save_to_mysql(df, symbol, connection=None):
    close_connection = False

    # Create a new connection if not passed
    if connection is None:
        connection = pymysql.connect(**DB_CONFIG)
        close_connection = True

    cursor = connection.cursor()
    table_name = symbol.lower().replace('usdt', '') + '_data'

    # Create table if it doesn't exist
    create_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        date DATETIME PRIMARY KEY,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume FLOAT,
        number_of_trades INT
    );
    """
    cursor.execute(create_query)

    # Insert or update records
    for _, row in df.iterrows():
        insert_query = f"""
        INSERT INTO {table_name} (date, open, high, low, close, volume, number_of_trades)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            open = VALUES(open),
            high = VALUES(high),
            low = VALUES(low),
            close = VALUES(close),
            volume = VALUES(volume),
            number_of_trades = VALUES(number_of_trades)
        """
        cursor.execute(insert_query, (
            row['Date'], row['Open'], row['High'], row['Low'],
            row['Close'], row['Volume'], row['Number of Trades']
        ))

    connection.commit()
    cursor.close()
    if close_connection:
        connection.close()
        print(f"✅ Saved data and closed connection for: {table_name}")
    else:
        print(f"✅ Saved data to MySQL table: {table_name}")
