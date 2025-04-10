# extract.py

import requests
import time
import pandas as pd
from datetime import datetime

# --------------------------------------
# Global Configuration
# --------------------------------------
interval = '1d'
start_str = '2017-08-01'

# --------------------------------------
# Helper Functions
# --------------------------------------
def date_to_ms(date_str):
    return int(datetime.strptime(date_str, "%Y-%m-%d").timestamp() * 1000)

def ms_to_date(ms):
    return datetime.utcfromtimestamp(ms / 1000.0)

# --------------------------------------
# Fetch Data from Binance API
# --------------------------------------
def fetch_coin_data(symbol, interval=interval, start_str=start_str):
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
        time.sleep(0.4)  # To avoid hitting the API rate limit

    return pd.DataFrame(all_data)
