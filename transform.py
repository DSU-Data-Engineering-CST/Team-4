# transform.py
# Loads the Excel data and performs basic data cleanup or transformation

import pandas as pd
import os

# Load from Desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
excel_file = os.path.join(desktop, "top_10_crypto_data.xlsx")

def load_data():
    print("📂 Loading Excel file...")
    try:
        xl = pd.ExcelFile(excel_file)
        coin_data = {sheet_name: xl.parse(sheet_name) for sheet_name in xl.sheet_names}
        print(f"✅ Loaded data for coins: {', '.join(coin_data.keys())}")
        return coin_data
    except FileNotFoundError:
        print("❌ Excel file not found! Please run `extract.py` first.")
        return {}

def clean_data(data):
    for coin, df in data.items():
        # Ensure correct dtypes and handle missing values
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        df = df.dropna(subset=["Date"])
        df = df.sort_values("Date")

        # Forward fill missing values if any
        df.fillna(method='ffill', inplace=True)
        data[coin] = df
    print("🧹 Cleaned and sorted all data.")
    return data

def transform_main():
    raw_data = load_data()
    if raw_data:
        clean = clean_data(raw_data)
        return clean
    return {}

if __name__ == "__main__":
    transformed_data = transform_main()
