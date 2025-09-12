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
  
### Installing

* How/where to download your program:
  - Clone the repo with git, or download the ZIP from GitHub and unzip it into a folder.
  - Example git commands:
    git clone https://github.com/Jadette32/miniproject1JanelleHolcomb.git
    cd miniproject1JanelleHolcomb

* Any modifications needed to be made to files/folders:
  - None. The program creates the “charts” folder automatically.
  - The “charts” folder is ignored by git so images are not uploaded.

### Executing program

* How to run the program:
  - Use the Conda interpreter in PyCharm, or open a terminal in the project folder.

* Step-by-step:
  1) Make sure yfinance is installed (see Dependencies).
  2) Run the script:
     python main.py
  3) You should see a message about the NumPy array shape (5, 10) and five “Saved:” lines.
  4) Look in the “charts” folder for the PNG files.

## Help

Any advice for common problems or issues.

Common issues:
- ImportError for numpy/matplotlib/pandas/yfinance → make sure you’re using the Conda interpreter.
- Not enough data points → switch to very liquid tickers (AAPL, MSFT, GOOGL, AMZN, META).
- No images saved → check that the run printed 5 “Saved:” lines and that the “charts” folder exists.

## Authors

Contributors names and contact info

Janelle Holcomb
GitHub: @Jadette32

## Version History

* 0.2
    * Reserved for future small improvements
    * See commit history on GitHub
* 0.1
    * Initial Release

## License

This project is for class use. No license file included.

## Acknowledgments

Inspiration, code snippets, etc.
* yfinance docs
* NumPy docs
* Matplotlib docs
* Class mini-project videos