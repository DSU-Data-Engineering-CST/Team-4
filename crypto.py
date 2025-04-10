import requests
import time
import pymysql
import pandas as pd
from datetime import datetime

# --------------------------------------
# MySQL Configuration
# --------------------------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'rootsrushti8',
    'database': 'crypto_data',
    'charset': 'utf8mb4'
}

# --------------------------------------
# Crypto Symbols
# --------------------------------------
symbols = [
    'BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT',
    'SOLUSDT', 'DOGEUSDT', 'AVAXUSDT', 'DOTUSDT', 'MATICUSDT'
]
interval = '1d'
start_str = '2017-08-01'

# --------------------------------------
# Helper Functions
# --------------------------------------
def date_to_ms(date_str):
    return int(datetime.strptime(date_str, "%Y-%m-%d").timestamp() * 1000)

def ms_to_date(ms):
    return datetime.utcfromtimestamp(ms / 1000.0)

def fetch_coin_data(symbol):
    url = 'https://api.binance.com/api/v3/klines'
    start_ms = date_to_ms(start_str)
    end_ms = int(time.time() * 1000)
    all_data = []

    print(f"\n🔄 Fetching data for {symbol}...")
    while start_ms < end_ms:
        params = {
            'symbol': symbol,
            'interval': interval,
            'startTime': start_ms,
            'limit': 1000
        }
        response = requests.get(url, params=params)
        data = response.json()

        if not data or 'code' in data:
            print(f"⚠️ Error or no data for {symbol}")
            break

        for k in data:
            all_data.append({
                'Date': ms_to_date(k[0]),
                'Open': float(k[1]),
                'High': float(k[2]),
                'Low': float(k[3]),
                'Close': float(k[4]),
                'Volume': float(k[5]),
                'Number of Trades': int(k[8])
            })

        start_ms = data[-1][6] + 1
        time.sleep(0.4)

    return pd.DataFrame(all_data)

# --------------------------------------
# Store in MySQL
# --------------------------------------
def save_to_mysql(df, symbol, connection):
    table_name = symbol.lower().replace('usdt', '') + '_data'

    cursor = connection.cursor()

    # Create table if not exists
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

    # Insert data
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
    print(f"✅ Saved data to MySQL table: {table_name}")

# --------------------------------------
# Main Execution
# --------------------------------------
connection = pymysql.connect(**DB_CONFIG)

for symbol in symbols:
    df = fetch_coin_data(symbol)
    if not df.empty:
        save_to_mysql(df, symbol, connection)

connection.close()
print("\n🎉 All data saved to MySQL successfully.")
