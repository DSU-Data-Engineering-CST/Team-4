# load.py
# Loads the cleaned cryptocurrency Excel data for further use (e.g., plotting, analysis)

import pandas as pd
import os

def get_excel_path():
    # Set the path to the Excel file on Desktop
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    return os.path.join(desktop, "top_10_crypto_data.xlsx")

def load_crypto_data():
    excel_file = get_excel_path()
    
    if not os.path.exists(excel_file):
        raise FileNotFoundError(f"❌ Excel file not found at {excel_file}. Please run `extract.py` first.")

    print(f"📥 Loading Excel data from: {excel_file}")
    
    # Load all sheets as a dictionary of DataFrames
    xl = pd.ExcelFile(excel_file)
    data = {sheet: xl.parse(sheet) for sheet in xl.sheet_names}

    print(f"✅ Loaded {len(data)} sheets: {', '.join(data.keys())}")
    return data

if __name__ == "__main__":
    crypto_data = load_crypto_data()
