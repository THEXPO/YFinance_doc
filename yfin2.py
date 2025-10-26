import yfinance as yf

aapl = yf.Ticker("AAPL") # This line creates a Ticker object for Apple Inc. using the yfinance library
print(aapl.info) # This line prints detailed information about Apple Inc. stock
hist = aapl.history(period="1mo") # This line retrieves the historical market data for Apple Inc. for the past month
print(hist) # This line prints the historical market data for Apple Inc.
dividends = aapl.dividends # This line retrieves the dividend history for Apple Inc.
print(dividends) # This line prints the dividend history for Apple Inc.
splits = aapl.splits # This line retrieves the stock split history for Apple Inc.
print(splits) # This line prints the stock split history for Apple Inc.
actions = aapl.actions # This line retrieves the corporate actions (dividends and splits) for Apple Inc.
print(actions) # This line prints the corporate actions for Apple Inc.
sustainability = aapl.sustainability # This line retrieves the sustainability scores for Apple Inc.
print(sustainability) # This line prints the sustainability scores for Apple Inc.
recommendations = aapl.recommendations # This line retrieves analyst recommendations for Apple Inc.
print(recommendations) # This line prints the analyst recommendations for Apple Inc.
calendar = aapl.calendar # This line retrieves the upcoming events for Apple Inc.
print(calendar) # This line prints the upcoming events for Apple Inc.
options = aapl.options # This line retrieves the available options expiration dates for Apple Inc.
print(options) # This line prints the available options expiration dates for Apple Inc.
