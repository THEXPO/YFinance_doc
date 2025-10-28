import yfinance as yf 

goog = yf.Ticker("GOOG")

hist = goog.history(period="1mo")

close_prices = hist['close'] # This only gives the 'close' prices same can be done for open high low close volume etc.
print(close_prices) 