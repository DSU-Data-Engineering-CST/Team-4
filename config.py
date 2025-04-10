# config.py

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
# Crypto Symbols to Track
# --------------------------------------
SYMBOLS = [
    'BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT',
    'SOLUSDT', 'DOGEUSDT', 'AVAXUSDT', 'DOTUSDT', 'MATICUSDT'
]

# --------------------------------------
# Binance API Configuration
# --------------------------------------
INTERVAL = '1d'
START_DATE = '2017-08-01'
