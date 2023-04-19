import pandas_datareader as pdr
import datetime

start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime(2021, 12, 31)

# Use DataReader function from pandas_datareader to download the historical stock prices
aapl_stock_prices = pdr.DataReader('AAPL', data_source='yahoo', start=start_date, end=end_date)

# Print the first 5 rows of the dataframe
print(aapl_stock_prices.head())
