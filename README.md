### INF601 - Advanced Programming in Python
### Janelle Holcomb
### Mini Project 1
 
# Stock Data Visualization with NumPy & Matplotlib
 
Simple overview: Pull last 10 trading-day close prices for 5 tickers, convert lists → NumPy array, make 5 charts with Matplotlib, and save PNGs in `charts/`.  
**Repo name must be:** `miniproject1JanelleHolcomb`
 
## Description
 
This project practices basic data work:
- Get stock data from `yfinance`
- Store values in Python lists, then convert to a NumPy array (shape 5 × 10)
- Plot each ticker’s 10 closes to its own chart with Matplotlib
- Save all PNGs to a `charts/` folder created at runtime
 
## Getting Started
 
### Dependencies
- Windows 10/11 (or macOS)
- **Anaconda Distribution** (Conda base environment)
- PyCharm (Community is fine)
- Python 3.10+
- Packages: `numpy`, `matplotlib`, `pandas` (included with Anaconda), and `yfinance`
  
Install the one extra package:
```bash
pip install yfinance
# (or) conda install -c conda-forge yfinance
