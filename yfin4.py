import yfinance as yf 

aapl = yf.Ticker("AAPL") # This line creates a Ticker object for Apple Inc. using the yfinance library
history = aapl.history(period="1mo", prepost=True) # This line retrieves the historical market data for Apple Inc. for the past month including pre and post market data
print(history) #This line prints the historical market data for Apple Inc.
history.to_csv("AAPL_data.csv") # This line saves the historical market data to a CSV file named "AAPL_data.csv"