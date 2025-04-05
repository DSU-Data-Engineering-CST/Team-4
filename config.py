# config.py

import os

# List of top 10 cryptocurrency symbols (USDT pairs)
COINS = [
    "BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT",
    "SOLUSDT", "DOGEUSDT", "AVAXUSDT", "DOTUSDT", "MATICUSDT"
]

# Binance API endpoint for historical klines (candlestick) data
BINANCE_API_URL = "https://api.binance.com/api/v3/klines"

# Request parameters
INTERVAL = "1d"             # Daily data
LIMIT = 1000                # Max rows per request
START_DATE = "2017-01-01"   # Historical start date

# Paths
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")
EXCEL_PATH = os.path.join(DESKTOP_PATH, "top_10_crypto_data.xlsx")
IMAGE_FOLDER = os.path.join(DESKTOP_PATH, "TopCryptoDashboards")
