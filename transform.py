# transform.py

import pandas as pd

# --------------------------------------
# Transform Crypto DataFrame
# --------------------------------------
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply transformation or feature engineering on the raw crypto DataFrame.

    Example transformations:
    - Add daily returns
    - Add moving averages
    - Rename columns if needed
    """

    if df.empty:
        return df

    df = df.sort_values("Date")

    # Add daily percentage return
    df['Daily Return (%)'] = df['Close'].pct_change() * 100

    # Add 7-day and 30-day moving averages
    df['MA_7'] = df['Close'].rolling(window=7).mean()
    df['MA_30'] = df['Close'].rolling(window=30).mean()

    # Fill NA for moving averages with forward-fill/backward-fill
    df.fillna(method='bfill', inplace=True)

    return df
