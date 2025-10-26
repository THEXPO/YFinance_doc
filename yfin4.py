import yfinance as yf 

aapl = yf.Ticker("AAPL")
history = aapl.history(period="1mo", prepost=True)
print(history)
history.to_csv("AAPL_data.csv")