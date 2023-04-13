import pandas_datareader as pdr

from datetime import datetime 
 
start_date = datetime(2021,1,1) 
end_date = datetime(2021,1,5)
 
df = pdr.DataReader('AAPL', 'yahoo', start_date, end_date)
print(df)