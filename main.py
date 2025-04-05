# main.py
# Master script to run the full crypto data pipeline

from extract import extract_main
from transform import transform_main
from dashboard_plotter import plot_dashboards

def main():
    print("🚀 Starting Top 10 Crypto Analyzer Pipeline...\n")

    print("📥 [1/3] Extracting data from Binance API...")
    extract_main()

    print("\n🧹 [2/3] Transforming and cleaning data...")
    cleaned_data = transform_main()

    print("\n📊 [3/3] Generating and saving dashboards...")
    plot_dashboards(cleaned_data)

    print("\n✅ Pipeline completed successfully!")

if __name__ == "__main__":
    main()
