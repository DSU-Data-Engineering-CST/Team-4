#!/bin/bash

echo "🚀 Starting Crypto ETL Pipeline..."

# Activate virtual environment (optional - only if you're using one)
# source venv/bin/activate

# Install dependencies (optional, in case not already installed)
pip install -r requirements.txt

# Run the ETL pipeline
python main.py

echo "✅ ETL process completed!"
