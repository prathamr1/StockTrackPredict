import yfinance as yf
import pandas as pd


def get_stock_price():
    stock = yf.Ticker(input("Enter the stock symbol : "))
    per=input("Enter the period of Stock Price 1mo,2mo,3mo... : ")
    data = stock.history(period=per)
    data.ffill(inplace=True)  # forward filling missing data
    data.index = pd.to_datetime(data.index)  # formatting date and time
    data = data.astype(float)

    data['SMA_50'] = data['Close'].rolling(window=50).mean()  # calc simple moving avg
    data["EMA_50"] = data['Close'].ewm(span=50, adjust=False).mean()  # calc exponential moving avg
    data["Volatility"] = data["Close"].pct_change().rolling(window=10).std()  # returns standard deviation
    data['Upper'] = data['SMA_50'] + (data['Close'].rolling(50).std() * 2)
    data['Lower'] = data['SMA_50'] - (data['Close'].rolling(50).std() * 2)

    # Finding RSI to identify overbought and oversold situations
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 9)).rolling(window=14).mean()
    rs = gain / loss
    data["RSI"] = 100 - (100 / (1 + rs))

    return data

