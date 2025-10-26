import yfinance as yf # This line imports the yfinance library

data = yf.download("GOOG", start = "2025-01-01", end = "2025-9-25") # This line downloads historical stock data for google(GOOG) from January 1, 2025 to September 25, 2025
print(data) #This prints  close,open,high,low,volumn of google stock for the specified date ranges