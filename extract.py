# extract.py
# Fetches historical OHLCV data from Binance for top 10 cryptos and stores it in Excel

import requests
import pandas as pd
import time
from datetime import datetime
import os

# Set up coin list and output path
TOP_10_COINS = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT',
                'SOLUSDT', 'DOGEUSDT', 'AVAXUSDT', 'DOTUSDT', 'MATICUSDT']
BASE_URL = "https://api.binance.com/api/v3/klines"
INTERVAL = "1d"
LIMIT = 1000

# Create output directory on Desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
output_path = os.path.join(desktop, "top_10_crypto_data.xlsx")

def fetch_ohlcv(symbol, start_str):
    data = []
    start_ts = int(pd.to_datetime(start_str).timestamp() * 1000)
    while True:
        url = f"{BASE_URL}?symbol={symbol}&interval={INTERVAL}&startTime={start_ts}&limit={LIMIT}"
        response = requests.get(url)
        raw = response.json()

        if not raw:
            break

        for entry in raw:
            data.append({
                "Date": pd.to_datetime(entry[0], unit='ms'),
                "Open": float(entry[1]),
                "High": float(entry[2]),
                "Low": float(entry[3]),
                "Close": float(entry[4]),
                "Volume": float(entry[5]),
                "Trades": int(entry[8])
            })

        start_ts = raw[-1][0] + 1
        time.sleep(0.5)  # Respect rate limits

    return pd.DataFrame(data)

def save_to_excel(all_data):
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        for symbol, df in all_data.items():
            df.to_excel(writer, sheet_name=symbol.replace("USDT", ""), index=False)
    print(f"\n✅ Data saved to Excel at: {output_path}")

def main():
    print("📥 Fetching historical data from Binance...")
    all_data = {}
    for symbol in TOP_10_COINS:
        print(f"→ {symbol}")
        df = fetch_ohlcv(symbol, start_str="2017-01-01")
        all_data[symbol] = df
    save_to_excel(all_data)

if __name__ == "__main__":
    main()
