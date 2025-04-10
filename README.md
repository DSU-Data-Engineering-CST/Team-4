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

## 📁 Project Structure

```
├── config.py
├── extract.py
├── transform.py
├── load.py
├── main.py
├── requirements.txt
├── run_etl.sh
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/crypto-etl.git
cd crypto-etl
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

## 🧑‍💻 Author

Built by **[Your Name]** – feel free to reach out or fork the project!

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
