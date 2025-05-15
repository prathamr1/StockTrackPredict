import pandas as pd
import requests as rq
import yfinance as yf
import numpy as np

stock = yf.Ticker(input("Enter the stock symbol : "))
data = stock.history(period='1mo')

data.ffill(inplace=True)#forward filling missing data
data.index = pd.to_datetime(data.index) #formatting date and time
data = data.astype(float)

data['SMA_50'] = data['Close'].rolling(window=50).mean() #calc simple moving avg
data["EMA_50"] = data['Close'].ewm(span=50, adjust=False).mean() #calc exponential moving avg
data["Volatility"] = data["Close"].pct_change().rolling(window=10).std() #returns standard deviation
data['Upper'] = data['SMA_50'] + (data['Close'].rolling(50).std()*2)
data['Lower'] = data['SMA_50'] - (data['Close'].rolling(50).std()*2)
#Finding RSI to identify overbought and oversold situations
delta = data['Close'].diff()
gain = (delta.where(delta > 0,0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0,9)).rolling(window=14).mean()
rs=gain/loss
data["RSI"] = 100-(100/(1+rs))

corr_mat= data.corr()
corr_mat['Close'].sort_values(ascending=False)
print(data)
