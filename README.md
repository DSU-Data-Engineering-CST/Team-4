# 📈 Top 10 Crypto Analyzer (Binance API)

This project fetches historical **daily price data** of the top 10 most popular cryptocurrencies from the **Binance API**, stores it in an **Excel spreadsheet**, and generates beautiful **visual dashboards** (charts) per coin. It helps visualize market trends over time and can be used for analysis or reporting.

---

## 🔧 Features

### ✅ Data Collection:
- Collects historical data from **2017 to present** using Binance API
- Fetches OHLCV data for each coin
- Handles pagination of data using timestamps
- Includes Open, High, Low, Close, Volume, and Number of Trades

### ✅ Storage:
- Saves data into a single Excel file (`top_10_crypto_data.xlsx`)
- One **sheet per coin**, neatly formatted
- Saved directly to your Desktop

### ✅ Visualization:
- Plots **4 informative charts per coin**:
  1. 📈 Closing Price Over Time
  2. 📊 Trading Volume Over Time
  3. 🔼 High-Low Price Spread Over Time
  4. 🔁 Number of Trades Over Time
- Each coin’s dashboard is saved as a **PNG image**
- All images saved into a folder on Desktop: `TopCryptoDashboards`

---

## 📂 Coins Covered

- BTC (Bitcoin)
- ETH (Ethereum)
- BNB (Binance Coin)
- XRP (Ripple)
- ADA (Cardano)
- SOL (Solana)
- DOGE (Dogecoin)
- AVAX (Avalanche)
- DOT (Polkadot)
- MATIC (Polygon)

---

## 🚀 How to Run

### Step 1: Install Required Packages

```bash
pip install pandas matplotlib openpyxl requests
```

### Step 2: Run the Python Script

#### 🧾 `top_10_crypto_data.py`
- Fetches historical data
- Stores it in `top_10_crypto_data.xlsx` on your Desktop
- Generates plots per coin
- Saves dashboards in `TopCryptoDashboards` folder
---

## 📝 Notes

- The Excel file may show `######` for dates if column width is too small. Just auto-fit the columns.
- If you get **permission errors**, ensure the Excel file is **closed** before re-running the script.
- Candlestick plots were removed for simplicity; only line/bar plots are used.
- Font warnings like `Glyph 8419` are safe to ignore or can be suppressed by changing the font if needed.

---

## 💡 Customization Ideas

- Add technical indicators like Moving Averages or RSI
- Export dashboards to PDF instead of PNG
- Combine all coin dashboards into a single report
- Add command-line arguments to select coins or date ranges

---

## 🧠 Use Cases

- Crypto Market Analysis & Research
- Trading Dashboards
- Investment Presentations
- Academic or Student Projects
- Personal Portfolios

---

## 🛠️ Built With

- 🟨 [Binance API](https://binance-docs.github.io/apidocs/spot/en/)
- 🐼 Pandas
- 📊 Matplotlib
- 📓 OpenPyXL

---
Built with ❤️ using Binance API, Pandas, Matplotlib, and Excel.
