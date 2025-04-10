from extract import fetch_coin_data
from load import save_to_mysql
from config import DB_CONFIG, SYMBOLS
import pymysql

def main():
    connection = pymysql.connect(**DB_CONFIG)
    for symbol in SYMBOLS:
        df = fetch_coin_data(symbol)
        if not df.empty:
            save_to_mysql(df, symbol, connection)
    connection.close()
    print("\n🎉 All data saved to MySQL successfully.")

if __name__ == '__main__':
    main()
