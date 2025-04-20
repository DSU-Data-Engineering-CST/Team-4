# 🪙 Crypto ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that collects historical cryptocurrency data from the Binance API and stores it in a MySQL database for further analysis and visualization.

---

## 📦 Features

- Fetches OHLCV data + number of trades for selected crypto pairs (e.g., BTC/USDT)
- Cleans and transforms data (e.g., adds moving averages, returns)
- Stores data in MySQL with automatic table creation
- Handles API rate limits and duplicates gracefully
- Modular codebase (extract, transform, load)
- `.env` support for managing secrets

---

## 🛠 Tech Stack

- Python
- MySQL
- Pandas
- Requests
- PyMySQL
- dotenv

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
https://github.com/DSU-Data-Engineering-CST/Team-4.git
cd Team-4
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` File

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=crypto_data
DB_CHARSET=utf8mb4
```

> ⚠️ Don't forget to update `yourpassword` with your MySQL root password.

### 4. Run the ETL Pipeline

```bash
./run_etl.sh
```

---

## 🧪 Example Use Cases

- Load crypto data into Power BI, Tableau, or Jupyter for visualization
- Build forecasting or trading algorithms
- Analyze crypto volatility or volume patterns over time

---

## 📌 To-Do / Future Ideas

- Add error logging and retry logic
- Add support for more intervals (e.g., `1h`, `15m`)
- Save transformed data as CSV or Parquet
- Dockerize the ETL pipeline

---

# 📊 Cryptocurrency Market Observations (2018–2025)
This report provides a high-level visual and narrative analysis of key cryptocurrencies based on their **price action**, **trading volume**, **high-low price spread**, and **number of trades**.
---
## 🔹 ADA (Cardano)
![ada](https://github.com/user-attachments/assets/5b985f99-5bf2-452e-a459-f46e3cf94428)

1\. Price Action (Top Chart - Blue Line):

- Early Stability and Growth (2018 - Early 2021): The price appears relatively stable at lower levels in the initial years. We then see a significant upward trend starting in early 2021, indicating growing interest and investment in ADA.
- Mid-2021 Peak and Subsequent Correction: There's a clear peak in the price around mid-2021, followed by a substantial correction and period of volatility. This kind of "pump and dump" pattern is not uncommon in the cryptocurrency market.
- Fluctuating Recovery (Late 2021 - Present): After the correction, the price shows periods of recovery and further volatility, never quite reaching the previous peak but generally staying at a higher level than the pre-2021 period. We can see some upward momentum again in early 2025.

2\. Trading Volume (Second Chart - Orange Bars):

- Volume Spikes Correlate with Price Swings: Notice how significant spikes in trading volume often coincide with major price movements, both upward and downward. This makes sense – increased buying and selling pressure drives price changes.
- Higher Volume During the 2021 Bull Run: The trading volume was particularly high during the 2021 price surge, indicating a lot of activity and speculation.
- Sustained Higher Volume Post-Peak: Even after the price correction, the trading volume generally remains higher than the levels seen before 2021, suggesting increased overall interest in ADA.

3\. High-Low Price Spread (Third Chart - Green Line):

- Spread Indicates Volatility: The high-low price spread represents the difference between the highest and lowest price reached within a given period. Larger spreads indicate higher intraday volatility.
- Volatility Spikes Around Key Price Events: We see spikes in the spread around the 2021 price peak and during other periods of significant price change. This suggests that these were times of intense price swings within the trading day.
- Relatively Lower Volatility in Stable Periods: During periods where the price is relatively stable, the high-low spread tends to be smaller.

4\. Number of Trades (Bottom Chart - Purple Line):

- Trade Count Mirrors Volume Trends: The number of trades generally follows a similar pattern to the trading volume. More trades usually accompany higher volume.
- Increased Trading Activity Post-2021: Similar to the volume, the number of trades appears to have increased overall after the 2021 bull run, indicating a larger and more active trading community for ADA.
- Recent Increase in Trading Activity: The uptick in price in early 2025 is also accompanied by a noticeable increase in the number of trades.

Overall Observations:

- 2021 was a pivotal year for ADA: The data clearly shows a significant surge in price, volume, and trading activity during 2021, marking a period of intense interest and speculation.
- Increased Market Participation: Even after the 2021 correction, the trading volume and number of trades have generally remained at higher levels, suggesting increased overall market participation in ADA.
- Volatility is Characteristic: Like many cryptocurrencies, ADA's price is prone to significant volatility, often accompanied by spikes in trading volume and the high-low price spread.
- Recent Positive Momentum: The recent uptick in price and trading activity in early 2025 could indicate renewed interest or a potential new trend.



