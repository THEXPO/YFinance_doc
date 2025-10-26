import yfinance as yf

tickers = ["MSFT", "AMZN", "TSLA"]  # List of ticker symbols for Microsoft, Amazon, and Tesla
for ticker in tickers:
    stock = yf.Ticker(ticker)  # Create a Ticker object for each company
    print(f"Information for {ticker}:")
    print(stock.info)  # Print detailed information about the stock
    hist = stock.history(period="1mo")  # Retrieve historical market data for the past month
    print(f"Historical data for {ticker}:\n", hist)  # Print the historical market data
    print("\n")  # Add a newline for better readability between different stocks

