import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database Configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'crypto_data'),
    'charset': os.getenv('DB_CHARSET', 'utf8mb4')
}

# ETL Configuration
INTERVAL = os.getenv('INTERVAL', '1d')          # default: daily data
START_DATE = os.getenv('START_DATE', '2023-01-01')  # default: Jan 1, 2023
