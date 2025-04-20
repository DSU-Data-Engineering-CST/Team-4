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

---
## 🔹 AVAX (Avalanche)
![avax](https://github.com/user-attachments/assets/75173525-244c-48e1-b462-39eb168f2038)

1\. Price Action (Top Chart - Blue Line):

- Initial Growth and Significant Bull Run (Late 2020 - Late 2021): We see a relatively low starting price followed by a significant and rapid increase throughout 2021, culminating in a clear peak in late 2021. This indicates a period of strong positive sentiment and adoption for AVAX.
- Sharp Correction and Subsequent Volatility (Late 2021 - Present): Following the peak, there's a sharp correction in price. The subsequent period shows significant volatility with smaller rallies and declines, never quite reaching the previous high.
- Recent Upswing (Early 2025): Similar to ADA, we observe a notable upward trend starting in early 2025, suggesting renewed buying interest.

2\. Trading Volume (Second Chart - Orange Bars):

- High Volume During the Bull Run: The trading volume was exceptionally high during the 2021 price surge, reinforcing the idea of strong market participation and speculative activity.
- Volume Spikes Correlate with Price Movements: We can see that significant price swings, both up and down, are often accompanied by increases in trading volume, indicating that these moves are backed by more substantial trading activity.
- Decreasing Volume Post-Peak: After the price peak and correction, the overall trading volume appears to decrease compared to the 2021 highs, although there are still periods of increased activity.

3\. High-Low Price Spread (Third Chart - Green Line):

- Volatility Spikes Around Price Extremes: The largest spikes in the high-low price spread coincide with the peak in late 2021 and other periods of rapid price change. This signifies high intraday volatility during these times.
- Generally Elevated Volatility Post-Peak: Even after the initial correction, the high-low spread remains generally higher than in the very early stages, indicating sustained higher volatility compared to the initial trading period.
- Recent Increase in Volatility: The recent price increase in early 2025 also seems to be accompanied by a rise in the high-low spread, suggesting increased intraday price fluctuations.

4\. Number of Trades (Bottom Chart - Purple Line):

- Trade Count Follows Volume Trends: The number of trades generally mirrors the trading volume patterns, with a significant increase during the 2021 bull run and subsequent fluctuations.
- Increased Trading Activity Post-2021 (Relative to Early Stages): While not as high as the peak, the number of trades after the 2021 surge remains generally higher than in the initial period, indicating a larger and more active trading base for AVAX.
- Recent Uptick in Trades: The recent positive price movement in early 2025 is also accompanied by a noticeable increase in the number of trades.

Overall Observations:

- 2021 was a defining year for AVAX: The dashboard clearly illustrates the massive price appreciation, high trading volume, and significant volatility that characterized AVAX's market in 2021.
- Strong Correction Followed the Peak: The sharp price correction after the 2021 peak highlights the often-volatile nature of cryptocurrency markets.
- Sustained, Albeit Lower, Activity: While the extreme highs of 2021 weren't revisited, the trading volume and number of trades remained at a generally higher level in the subsequent years compared to the initial trading period.
- Renewed Positive Momentum in 2025: The recent increase in price, volume, and trade activity in early 2025 suggests a potential resurgence of interest in AVAX.

  ---
## 🔹 BNB (Binance Coin)
![bnb](https://github.com/user-attachments/assets/c25468f8-d5c1-41a2-adea-0a2aac76af1a)

1\. Price Action (Top Chart - Blue Line):

- Early Stability and Initial Growth (2018 - Early 2021): The price starts relatively low and experiences gradual growth over the initial years.
- Significant Bull Run (Early 2021 - Mid 2021): Similar to ADA and AVAX, BNB saw a substantial and rapid price increase in the first half of 2021, indicating strong market enthusiasm.
- Sustained Higher Price Levels with Volatility (Mid 2021 - Present): After the mid-2021 peak, the price corrected but generally maintained significantly higher levels compared to the pre-2021 period. We observe periods of both upward and downward volatility.
- Strong Recovery and New Highs (Late 2024 - Early 2025): Notably, BNB experienced a strong upward trend in late 2024 and early 2025, surpassing its previous 2021 peak and reaching new all-time highs.

2\. Trading Volume (Second Chart - Orange Bars):

- Volume Surge During the 2021 Bull Run: The trading volume spiked dramatically during the 2021 price surge, aligning with the increased buying and selling activity.
- Elevated Volume Post-Peak: Even after the price correction in mid-2021, the trading volume generally remained higher than the levels seen before 2021, indicating increased market participation.
- Strong Volume Accompanying Recent Price Surge: The recent climb to new highs in late 2024 and early 2025 is also supported by significant increases in trading volume, suggesting strong conviction behind the price movement.

3\. High-Low Price Spread (Third Chart - Green Line):

- Volatility Spikes Around Major Price Movements: We see significant increases in the high-low price spread coinciding with the 2021 bull run and the recent surge to new highs. This indicates heightened intraday price volatility during these periods of rapid price change.
- Generally Higher Volatility Post-2021: Compared to the initial years, the high-low spread appears generally elevated after the 2021 bull run, suggesting a more volatile trading environment for BNB.
- Increased Volatility During Recent Rally: The recent price surge is also marked by increased intraday volatility, as shown by the higher high-low spreads.

4\. Number of Trades (Bottom Chart - Purple Line):

- Trade Count Mirrors Volume Patterns: The number of trades closely follows the trends in trading volume, showing significant increases during the 2021 bull run and the recent price surge.
- Increased Trading Activity Post-2021: Similar to volume, the number of trades remained generally higher after the 2021 peak compared to earlier years, indicating a larger and more active trading community for BNB.
- Strong Increase in Trades During Recent Rally: The recent push to new price highs is accompanied by a substantial increase in the number of trades, reflecting strong market activity.

Overall Observations:

- Strong Growth Trajectory: BNB has shown a strong overall growth trajectory since its inception, with significant milestones in 2021 and again in late 2024/early 2025.
- Key Role of the Binance Ecosystem: The performance of BNB is likely closely tied to the growth and adoption of the Binance ecosystem, including the exchange, Binance Smart Chain (now BNB Chain), and other related services.
- Increased Market Maturity: The sustained higher levels of trading volume and number of trades after the initial bull run suggest a maturing market for BNB with greater participation.
- Recent Breakout to New Highs: The recent surge to new all-time highs, supported by strong volume and increased trading activity, indicates significant positive momentum and potentially new levels of interest in BNB.

---
## 🔹 BTC (Bitcoin)
![Figure_1](https://github.com/user-attachments/assets/df2ebcef-a594-4f2e-8e1e-6b296272765e)
1\. Price Action (Top Chart - Blue Line):

- Early Growth and First Major Bull Run (2017): Bitcoin shows initial growth followed by its first significant bull run in 2017, reaching a notable peak.
- Subsequent Correction and Consolidation (2018 - 2020): Following the 2017 peak, BTC experienced a substantial correction and then a prolonged period of consolidation with lower price levels.
- Major Bull Run (Late 2020 - Late 2021): Bitcoin then embarked on a significant and sustained bull run, reaching new all-time highs in late 2021. This period was likely driven by increased institutional interest, corporate adoption, and broader macroeconomic factors.
- Correction and Volatility at Higher Levels (2022 - 2023): After the 2021 peak, BTC underwent a significant correction. However, it generally traded at much higher levels than before the 2020-2021 bull run, exhibiting continued volatility.
- Strong Recovery and New All-Time Highs (Late 2023 - Early 2025): Bitcoin showed a strong recovery starting in late 2023, eventually breaking its previous all-time high and reaching new peaks in early 2025. This recent surge could be attributed to factors like the approval of spot Bitcoin ETFs in the US and renewed institutional interest.

2\. Trading Volume (Second Chart - Orange Bars):

- Volume Spikes During Bull Runs and Corrections: Significant spikes in trading volume coincide with both major bull runs (2017 and 2020-2021) and the subsequent major corrections, indicating high activity during periods of significant price change.
- Sustained Higher Volume Post-2020: After the 2020 bull run, the trading volume generally remained higher than the levels seen in the earlier years, suggesting increased overall market interest and participation in BTC.
- Strong Volume Accompanying Recent Upswing: The recent surge to new all-time highs in late 2023 and early 2025 is supported by noticeable increases in trading volume, indicating strong conviction behind the upward movement.

3\. High-Low Price Spread (Third Chart - Green Line):

- Volatility Spikes Around Major Price Movements: The largest spikes in the high-low price spread align with the major bull runs and corrections, signifying high intraday price volatility during these periods.
- Generally Elevated Volatility Post-2020: Compared to the earlier years, the high-low spread appears generally higher after the 2020 bull run, indicating a more volatile trading environment for BTC at these higher price levels.
- Increased Volatility During Recent Rally: The recent price increase to new highs is also accompanied by a rise in the high-low spread, suggesting increased intraday price fluctuations.

4\. Number of Trades (Bottom Chart - Purple Line):

- Increased Trade Activity During Bull Runs and Corrections: The number of trades shows significant increases during the major bull runs and corrections, mirroring the volume trends.
- Sustained Higher Number of Trades Post-2020: Similar to volume, the number of trades has generally remained higher after the 2020 bull run, indicating a larger and more active trading community for BTC.
- Strong Increase in Trades During Recent Upswing: The recent positive price movement to new highs is accompanied by a substantial increase in the number of trades, reflecting strong market activity.

Overall Observations:

- The Dominant Cryptocurrency: As the leading cryptocurrency, Bitcoin's price action often sets the trend for the broader market.
- Maturing Market with Increased Institutional Participation: The higher sustained trading volume and price levels post-2020 suggest a maturing market with greater institutional involvement.
- Strong Reaction to Macroeconomic Factors: Bitcoin's price has become increasingly sensitive to macroeconomic events, regulatory developments, and institutional news.
- Recent Breakout to New Highs: The recent surge to new all-time highs, supported by strong volume and trade activity, signifies a significant bullish phase. The approval of spot Bitcoin ETFs in the US has likely played a crucial role in this recent price action.

---
## 🔹 DOGE (Dogecoin)
![doge](https://github.com/user-attachments/assets/0041495d-8fff-467d-9d41-64f8a2e8b78c)
1\. Price Action (Top Chart - Blue Line):

- Relatively Flat Until Early 2021: For a significant period, the price of Dogecoin remained very low and relatively stable.
- Explosive Surge in Early 2021: We see an unprecedented and rapid price increase in early 2021, catapulting Dogecoin to levels significantly higher than its previous trading range. This period was largely driven by social media hype and increased retail interest.
- Sharp Correction and Subsequent Volatility (Mid 2021 - Mid 2024): Following the massive surge, the price experienced a sharp correction. The subsequent years show a pattern of lower highs and lower lows, with periods of volatility but generally trending downwards from the peak.
- Renewed Volatility and Smaller Rallies (Late 2024 - Early 2025): We observe some renewed price volatility and smaller upward movements in late 2024 and early 2025, although not reaching the highs of 2021.

2\. Trading Volume (Second Chart - Orange Bars):

- Massive Volume Spike During the 2021 Surge: The trading volume experienced an enormous spike coinciding with the explosive price increase in early 2021, indicating a frenzy of buying and selling.
- Significantly Lower Volume Post-Peak: After the price correction, the trading volume decreased dramatically and remained at much lower levels compared to the 2021 peak.
- Occasional Volume Spikes During Rallies: We can see smaller spikes in volume corresponding to the smaller price rallies in late 2024 and early 2025, suggesting some renewed interest during these periods.

3\. High-Low Price Spread (Third Chart - Green Line):

- Extreme Volatility During the 2021 Surge: The high-low price spread shows a massive spike during the early 2021 price explosion, indicating extreme intraday price swings.
- Lower Volatility Post-Peak: Following the correction, the high-low price spread generally decreased significantly, reflecting the lower overall price volatility compared to the surge period.
- Increased Volatility During Recent Rallies: The smaller price rallies in late 2024 and early 2025 are also accompanied by noticeable increases in the high-low spread, indicating higher intraday volatility during these movements.

4\. Number of Trades (Bottom Chart - Purple Line):

- Huge Increase in Trades During the 2021 Surge: The number of trades mirrored the trading volume, showing a massive spike in early 2021 as many participants traded Dogecoin.
- Substantially Fewer Trades Post-Peak: After the price correction, the number of trades dropped significantly and remained at much lower levels.
- Smaller Increases in Trades During Recent Activity: The minor price rallies in late 2024 and early 2025 also show corresponding increases in the number of trades, although nowhere near the levels of the 2021 peak.

Overall Observations:

- Meme-Driven Phenomenon: The 2021 price surge in Dogecoin was largely attributed to social media trends and community enthusiasm, rather than fundamental developments.
- Unsustainable Peak and Subsequent Correction: The explosive growth proved unsustainable, leading to a significant price correction.
- Lower Sustained Interest: After the initial hype subsided, trading volume and price levels remained significantly lower.
- Recurring Volatility: While the overall interest has decreased, Dogecoin continues to exhibit periods of heightened volatility, often influenced by social media trends or endorsements.
- Recent Minor Revivals: The small rallies in late 2024 and early 2025 suggest that there is still some speculative interest in Dogecoin, although it hasn't reached its previous highs.

---
## 🔹 DOT (Polkadot)
![dot](https://github.com/user-attachments/assets/255cd2b6-b9f7-47c5-bc27-fd153b1f2949)
1\. Price Action (Top Chart - Blue Line):

- Initial Growth and Significant Bull Run (Late 2020 - Mid 2021): Similar to other cryptocurrencies, DOT experienced a substantial price increase starting in late 2020 and peaking around mid-2021. This indicates strong early interest and investment.
- Sharp Correction and Extended Downtrend (Mid 2021 - Late 2023): Following the peak, DOT underwent a significant price correction and then a prolonged period of downtrend, reaching lower lows over an extended period. This suggests a decrease in market enthusiasm or broader market headwinds affecting DOT.
- Period of Relative Stability and Recent Upswing (Late 2023 - Early 2025): From late 2023 onwards, the price appears to stabilize somewhat before showing a noticeable upward trend in late 2024 and early 2025, indicating renewed buying interest.

2\. Trading Volume (Second Chart - Orange Bars):

- High Volume During the 2021 Bull Run: The trading volume spiked significantly during the 2021 price surge, aligning with increased market activity and speculation.
- Decreasing Volume During Downtrend: As the price corrected and trended downwards, the trading volume generally decreased, suggesting less active participation during this period.
- Increased Volume During Recent Upswing: The recent price increase in late 2024 and early 2025 is accompanied by a noticeable increase in trading volume, indicating stronger conviction behind the upward movement.

3\. High-Low Price Spread (Third Chart - Green Line):

- Volatility Spikes Around Price Extremes: The largest spikes in the high-low price spread coincide with the 2021 price peak and the recent upward movement, indicating higher intraday volatility during these periods of significant price change.
- Lower Volatility During Downtrend and Stability: During the extended downtrend and the period of relative price stability, the high-low spread appears generally lower, suggesting less intraday price fluctuation.
- Increased Volatility with Recent Rally: The recent price increase is also marked by a rise in the high-low spread, indicating increased intraday price swings.

4\. Number of Trades (Bottom Chart - Purple Line):

- High Number of Trades During 2021 Bull Run: The number of trades mirrored the trading volume, showing a significant increase during the 2021 price surge.
- Decreased Number of Trades During Downtrend: As the price declined, the number of trades also generally decreased, reflecting lower market activity.
- Increased Number of Trades During Recent Upswing: The recent positive price movement in late 2024 and early 2025 is accompanied by a noticeable increase in the number of trades, suggesting more active participation.

Overall Observations:

- Followed Broader Market Trends: DOT's price action in 2021 aligns with the broader cryptocurrency market bull run, followed by a correction and extended downturn that affected many altcoins.
- Period of Consolidation: The period of relative price stability after the downtrend could represent a phase of consolidation before the recent upward movement.
- Renewed Interest: The recent increase in price, volume, and number of trades suggests renewed interest in Polkadot. This could be driven by specific developments within the Polkadot ecosystem, improving market sentiment, or other factors.
- Volatility Reflects Market Sentiment: The spikes in the high-low price spread correlate with periods of significant price change and increased trading activity, indicating higher market uncertainty and speculation during these times.

---
## 🔹 ETH (Ethereum)
![etc](https://github.com/user-attachments/assets/f908e2ed-4208-4786-a486-9afb66db7e3f)
1\. Price Action (Top Chart - Blue Line):

- Early Growth and First Bull Run (2017 - Early 2018): Ethereum shows initial growth followed by its first significant bull run in late 2017 and early 2018, reaching a notable peak.
- Subsequent Correction and Consolidation (2018 - Mid 2020): Following the 2018 peak, ETH experienced a substantial correction and then a prolonged period of consolidation with lower price levels.
- Major Bull Run (Mid 2020 - Late 2021): Ethereum then embarked on a significant and sustained bull run, reaching new all-time highs in late 2021. This period likely reflected increased adoption, the rise of DeFi and NFTs, and broader market enthusiasm.
- Correction and Volatility at Higher Levels (2022 - Present): After the 2021 peak, ETH underwent a significant correction. While it hasn't returned to its peak, it has generally traded at much higher levels than before the 2020-2021 bull run, exhibiting continued volatility with periods of both upward and downward movement. We can see a strong upward trend resuming in late 2024 and early 2025.

2\. Trading Volume (Second Chart - Orange Bars):

- Volume Spikes During Bull Runs and Corrections: We see significant spikes in trading volume coinciding with both the major bull runs (2017-2018 and 2020-2021) and the subsequent major corrections. This indicates high activity during periods of significant price change.
- Sustained Higher Volume Post-2021 Peak: Even after the 2021 peak and correction, the trading volume generally remains higher than the levels seen before the 2020-2021 bull run, suggesting increased overall market interest and participation in ETH.
- Strong Volume Accompanying Recent Upswing: The recent upward trend in late 2024 and early 2025 is also supported by noticeable increases in trading volume, indicating strong buying interest.

3\. High-Low Price Spread (Third Chart - Green Line):

- Volatility Spikes Around Major Price Movements: The largest spikes in the high-low price spread align with the major bull runs and corrections, signifying high intraday price volatility during these periods.
- Generally Elevated Volatility Post-2021 Peak: Compared to the earlier years, the high-low spread appears generally higher after the 2021 peak, indicating a more volatile trading environment for ETH at these higher price levels.
- Increased Volatility During Recent Rally: The recent price increase is also accompanied by a rise in the high-low spread, suggesting increased intraday price fluctuations.

4\. Number of Trades (Bottom Chart - Purple Line):

- Increased Trade Activity During Bull Runs and Corrections: The number of trades shows significant increases during the major bull runs and corrections, mirroring the volume trends.
- Sustained Higher Number of Trades Post-2021 Peak: Similar to volume, the number of trades has generally remained higher after the 2021 peak, indicating a larger and more active trading community for ETH.
- Strong Increase in Trades During Recent Upswing: The recent positive price movement in late 2024 and early 2025 is accompanied by a substantial increase in the number of trades, reflecting strong market activity.

Overall Observations:

- Established Cryptocurrency with Multiple Bull Cycles: Ethereum has demonstrated multiple significant bull and bear cycles, indicating its maturity and importance within the cryptocurrency space.
- Strong Correlation with Market Trends: ETH's price action often reflects broader trends in the cryptocurrency market, but its performance can also be influenced by its own ecosystem developments and adoption.
- Increased Adoption and Utility: The sustained higher price and trading volume after the 2020-2021 bull run likely reflect the increasing adoption and utility of the Ethereum network through DeFi, NFTs, and other applications.
- Recent Positive Momentum: The strong upward trend in late 2024 and early 2025, supported by high volume and trade activity, suggests renewed bullish sentiment towards Ethereum.

---
## 🔹 MATIC (Polygon)
![matic](https://github.com/user-attachments/assets/97d3cc40-5582-4b90-95ca-7e195c349cab)
1\. Price Action (Top Chart - Blue Line):

- Relatively Low and Stable Until Early 2021: For a significant period, the price of MATIC (now known as Polygon) remained quite low and relatively stable.
- Explosive Bull Run in Early-Mid 2021: Similar to many other altcoins, MATIC experienced a massive and rapid price surge in early to mid-2021, reaching its historical peak. This likely coincided with increased interest in Layer-2 scaling solutions for Ethereum and growing adoption of the Polygon network.
- Significant Correction and Subsequent Volatility (Late 2021 - Present): Following the peak, the price underwent a substantial correction. While it has seen periods of recovery and volatility, it has generally traded below its 2021 high. We can observe some upward momentum in late 2024 and early 2025.

2\. Trading Volume (Second Chart - Orange Bars):

- Massive Volume Spike During the 2021 Surge: The trading volume experienced an enormous spike corresponding with the explosive price increase in early-mid 2021, indicating a frenzy of buying and selling.
- Significantly Lower Volume Post-Peak: After the price correction, the trading volume decreased considerably and remained at much lower levels compared to the 2021 peak.
- Occasional Volume Spikes During Rallies: We see smaller spikes in volume coinciding with the price rallies in late 2021 and into 2022, as well as the more recent upward movement in late 2024 and early 2025, suggesting some renewed interest during these periods.

3\. High-Low Price Spread (Third Chart - Green Line):

- Extreme Volatility During the 2021 Surge: The high-low price spread shows a massive spike during the early-mid 2021 price explosion, indicating extreme intraday price swings.
- Lower Volatility Post-Peak: Following the correction, the high-low price spread generally decreased significantly, reflecting the lower overall price volatility compared to the surge period.
- Increased Volatility During Recent Rallies: The smaller price rallies in late 2024 and early 2025 are also accompanied by noticeable increases in the high-low spread, indicating higher intraday volatility during these movements.

4\. Number of Trades (Bottom Chart - Purple Line):

- Huge Increase in Trades During the 2021 Surge: The number of trades mirrored the trading volume, showing a massive spike in early-mid 2021 as many participants traded MATIC.
- Substantially Fewer Trades Post-Peak: After the price correction, the number of trades dropped significantly and remained at much lower levels.
- Smaller Increases in Trades During Recent Activity: The minor price rallies in late 2024 and early 2025 also show corresponding increases in the number of trades, although nowhere near the levels of the 2021 peak.

Overall Observations:

- Strong Reaction to Layer-2 Narrative: MATIC's significant price surge in 2021 highlights the market's enthusiasm for Ethereum scaling solutions.
- Unsustainable Peak and Subsequent Correction: The explosive growth proved unsustainable, leading to a significant price correction, common for many altcoins after parabolic runs.
- Lower Sustained Interest Compared to Peak: While the Polygon network continues to develop and see adoption, the trading volume and price levels haven't returned to their 2021 highs.
- Renewed Positive Momentum: The recent upward movement in late 2024 and early 2025, accompanied by increased volume and trades, suggests renewed positive sentiment, potentially driven by new developments or broader market trends.

---
## 🔹 SOL (Solana)
![sol](https://github.com/user-attachments/assets/a712f8cb-0b16-4099-90e7-48c7ac7fe972)
1\. Price Action (Top Chart - Blue Line):

- Initial Growth and Significant Bull Run (Early 2021 - Late 2021): Solana experienced rapid and substantial price growth throughout 2021, culminating in a clear peak in late 2021. This period likely reflected increasing adoption of the Solana blockchain due to its speed and low transaction costs.
- Sharp Correction and Extended Downtrend (Late 2021 - Late 2022): Following the peak, SOL underwent a significant price correction and a prolonged downtrend, reaching a low point in late 2022. This period coincided with broader market downturns and specific concerns surrounding the Solana ecosystem, including network outages.
- Strong Recovery and Renewed Volatility (2023 - Present): Starting in 2023, Solana showed a strong recovery, regaining significant price levels. The period from late 2023 into early 2025 shows considerable volatility with strong upward and downward swings, eventually reaching levels approaching its previous high.

2\. Trading Volume (Second Chart - Orange Bars):

- High Volume During the 2021 Bull Run: The trading volume was exceptionally high during the 2021 price surge, indicating strong market participation and speculative activity.
- Decreased Volume During Downtrend: As the price corrected and trended downwards in 2022, the trading volume generally decreased, suggesting less active participation during this period.
- Increased Volume During Recovery and Volatility: The recovery in 2023 and the subsequent volatile period show significant increases in trading volume, indicating renewed interest and active trading. The recent price swings in late 2024 and early 2025 are also accompanied by high volume.

3\. High-Low Price Spread (Third Chart - Green Line):

- Volatility Spikes Around Price Extremes: The largest spikes in the high-low price spread coincide with the 2021 price peak, the low point in late 2022, and the periods of rapid price movement in 2023 and into 2025. This signifies high intraday volatility during these times.
- Generally Elevated Volatility Post-2021: Even after the initial correction, the high-low spread remains generally higher than in the very early stages, indicating sustained higher volatility compared to the initial trading period.
- Significant Volatility During Recent Price Swings: The recent strong upward and downward price movements are accompanied by significant increases in the high-low spread, highlighting the current volatile nature of SOL trading.

4\. Number of Trades (Bottom Chart - Purple Line):

- High Number of Trades During 2021 Bull Run: The number of trades followed the trading volume, showing a significant increase during the 2021 price surge.
- Decreased Number of Trades During Downtrend: As the price declined in 2022, the number of trades also generally decreased.
- Increased Number of Trades During Recovery and Volatility: The recovery and subsequent volatile trading periods show a significant increase in the number of trades, indicating more active participation. The recent price swings in late 2024 and early 2025 also show a high number of trades.

Overall Observations:

- High Growth and High Volatility Asset: Solana has demonstrated the potential for rapid growth but also significant price volatility, making it a higher-risk asset.
- Impact of Network Developments and Issues: The price downturn in 2022 likely reflects the impact of network outages and broader market sentiment. The subsequent recovery suggests resilience and renewed confidence in the technology.
- Strong Community and Ecosystem: The recovery and sustained trading activity indicate a strong underlying community and developing ecosystem.
- Recent Volatility Suggests Ongoing Market Discovery: The significant price swings and high trading volume in late 2024 and early 2025 suggest that the market is still actively evaluating Solana's long-term value.

---
## 🔹 XRP (Ripple)
![xrp](https://github.com/user-attachments/assets/04c31c5a-3f8d-469c-afe3-e5c18c41f00d)
1\. Price Action (Top Chart - Blue Line):

- Relatively Stable with Occasional Spikes (2018 - Early 2021): For a prolonged period, XRP's price remained relatively stable, with occasional short-lived price spikes.
- Significant Bull Run in Early 2021: XRP experienced a notable price surge in early 2021, although it didn't reach the heights of many other cryptocurrencies during that broader market rally.
- Correction and Subsequent Volatility (Mid 2021 - Late 2024): Following the early 2021 peak, the price corrected and entered a period of volatility with no clear sustained upward trend. The price action appears somewhat subdued compared to other major cryptocurrencies during this time.
- Sharp Price Increase in Late 2024 - Early 2025: XRP shows a significant and rapid price increase starting in late 2024 and continuing into early 2025, reaching levels not seen since the 2018 bull run. This surge likely correlates with positive developments in the ongoing SEC lawsuit against Ripple.

2\. Trading Volume (Second Chart - Orange Bars):

- Volume Spikes Correlate with Price Movements: We see noticeable spikes in trading volume aligning with the price surges in early 2021 and the more recent rally in late 2024 - early 2025, indicating increased market activity during these periods.
- Relatively Lower Volume During Stable Periods: During the extended periods of price stability or sideways movement, the trading volume appears generally lower.
- Significant Volume Increase During Recent Rally: The recent sharp price increase is accompanied by a substantial surge in trading volume, suggesting strong market participation and conviction behind the move.

3\. High-Low Price Spread (Third Chart - Green Line):

- Volatility Spikes Around Price Changes: The high-low price spread shows increases during the price surges, indicating higher intraday volatility during these periods of rapid price movement. The recent rally shows a particularly significant spike in the spread.
- Lower Volatility During Stable Periods: During the extended periods of price stability, the high-low spread tends to be smaller, indicating less intraday price fluctuation.
- High Volatility During Recent Rally: The recent sharp price increase is marked by significant intraday volatility, as evidenced by the large high-low spread.

4\. Number of Trades (Bottom Chart - Purple Line):

- Increased Trade Activity During Price Surges: The number of trades shows increases corresponding to the price surges in early 2021 and the recent rally, mirroring the volume trends.
- Lower Number of Trades During Stable Periods: During the extended periods of price stability, the number of trades appears generally lower.
- Significant Increase in Trades During Recent Rally: The recent sharp price increase is accompanied by a substantial increase in the number of trades, reflecting strong market activity.

Overall Observations:

- Impact of the SEC Lawsuit: XRP's price action has been heavily influenced by the ongoing lawsuit with the SEC. The subdued price performance between mid-2021 and late 2024 likely reflects the uncertainty surrounding the legal proceedings.
- Event-Driven Price Action: The significant price surges appear to be strongly correlated with perceived positive developments or increased optimism regarding the lawsuit's outcome. The recent rally strongly suggests a market reaction to such news.
- Periods of Low Volatility and Interest: Outside of these event-driven spikes, XRP has experienced extended periods of relatively low volatility and trading interest.
- Strong Market Reaction to Recent Positive Developments: The sharp price increase and significant volume and trade activity in late 2024 and early 2025 indicate a strong market reaction to recent positive news or sentiment surrounding the SEC case.











