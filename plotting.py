import matplotlib.pyplot as plt
from data_load import get_stock_price

def plot_returns():
    data = get_stock_price()
    plt.figure(figsize=(12,6))
    plt.plot(data.index , data['Close'], label="Stock Price", color='blue')
    plt.plot(data.index, data['SMA_50'], label="50-Day Simple Moving Avg", color='green')
    plt.plot(data.index, data['Upper'], label="Upper Bollinger Band", linestyle='dashed', color='red')
    plt.plot(data.index, data['Lower'], label="Lower Bollinger Band", linestyle='dashed', color='red')
    plt.legend()
    plt.show()
