# INF601 - Advanced Programming in Python
# Janelle Holcomb
# Mini Project 1

import os
from datetime import datetime

import numpy as np             # numbers work
import matplotlib.pyplot as plt # charts
import yfinance as yf           # grab stock data

# Five tickers I’m using. Swap these for favorites if you want.
TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]

# Make a place to save the pictures. (ignoring this folder in git.)
os.makedirs("charts", exist_ok=True)

# The rubric wants me to store data in lists first, then convert to NumPy.
all_price_lists = []        # holds 10 closes for each ticker
date_labels_by_ticker = {}  # pretty date labels for the x-axis

for t in TICKERS:
    # Pull extra days so weekends/holidays don’t mess up getting 10 trading days.
    hist = yf.Ticker(t).history(period="30d", interval="1d", auto_adjust=False)

    # only need the last 10 trading-day CLOSE prices.
    closes = hist["Close"].dropna().tail(10)

    # If a ticker is weird/illiquid and doesn’t have 10 points, fail fast.
    if len(closes) < 10:
        raise SystemExit(f"{t}: only {len(closes)} trading days found (need 10). Try a different ticker.")

    # Save the raw list for the rubric.
    all_price_lists.append(closes.tolist())

    # Store labels like 09-12 for the x-axis.
    date_labels_by_ticker[t] = [d.strftime("%m-%d") for d in closes.index.to_pydatetime()]

# Now do the list -> NumPy array step (shape should be 5 x 10).
prices_np = np.array(all_price_lists, dtype=float)
print("NumPy array shape (tickers x days):", prices_np.shape)

# One simple chart per ticker
for i, t in enumerate(TICKERS):
    y = prices_np[i, :]
    x_positions = range(1, len(y) + 1)

    plt.figure(figsize=(8, 4.5))
    plt.plot(x_positions, y, marker="o", linewidth=2)
    plt.title(f"{t} - Last 10 Trading Days (Close)")
    plt.xlabel("Date")
    plt.ylabel("Close (USD)")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.xticks(ticks=x_positions, labels=date_labels_by_ticker[t], rotation=45, ha="right")

    # Timestamp in the filename, so I don’t overwrite charts if I rerun.
    fname = f"{t}_close_last10_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    fpath = os.path.join("charts", fname)

    plt.tight_layout()
    plt.savefig(fpath, dpi=150)
    plt.close()

    print("Saved:", fpath)