# dashboard_plotter.py
import os
import matplotlib.pyplot as plt
import pandas as pd
from config import OUTPUT_IMAGE_FOLDER

def plot_dashboards(coin_data_dict):
    os.makedirs(OUTPUT_IMAGE_FOLDER, exist_ok=True)

    for coin, df in coin_data_dict.items():
        print(f"📊 Plotting dashboard for {coin}...")

        # Create figure and axes (2x2 grid)
        fig, axs = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle(f"{coin} Dashboard (2017–Present)", fontsize=16, fontweight="bold")

        # Plot 1 – Closing Price Over Time
        axs[0, 0].plot(df['Date'], df['Close'], color='blue', linewidth=1)
        axs[0, 0].set_title("📈 Closing Price Over Time")
        axs[0, 0].set_xlabel("Date")
        axs[0, 0].set_ylabel("Close (USD)")
        axs[0, 0].grid(True)

        # Plot 2 – Trading Volume Over Time
        axs[0, 1].bar(df['Date'], df['Volume'], color='orange', width=2)
        axs[0, 1].set_title("📊 Trading Volume Over Time")
        axs[0, 1].set_xlabel("Date")
        axs[0, 1].set_ylabel("Volume")
        axs[0, 1].grid(True)

        # Plot 3 – High-Low Price Spread
        spread = df['High'] - df['Low']
        axs[1, 0].plot(df['Date'], spread, color='green')
        axs[1, 0].set_title("🔼 High-Low Price Spread Over Time")
        axs[1, 0].set_xlabel("Date")
        axs[1, 0].set_ylabel("Price Spread")
        axs[1, 0].grid(True)

        # Plot 4 – Number of Trades Over Time
        axs[1, 1].plot(df['Date'], df['Trades'], color='purple')
        axs[1, 1].set_title("🔁 Number of Trades Over Time")
        axs[1, 1].set_xlabel("Date")
        axs[1, 1].set_ylabel("Number of Trades")
        axs[1, 1].grid(True)

        # Format x-axis labels
        for ax in axs.flat:
            ax.tick_params(axis='x', rotation=30)

        # Adjust layout and save image
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        output_path = os.path.join(OUTPUT_IMAGE_FOLDER, f"{coin}_dashboard.png")
        plt.savefig(output_path, dpi=300)
        plt.close()

        print(f"✅ Dashboard saved: {output_path}")
