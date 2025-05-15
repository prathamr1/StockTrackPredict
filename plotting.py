import matplotlib.pyplot as plt
from main import data
plt.figure(figsize=(10,5))
plt.plot(data.index , data['Close'], label="Stock Price", color='black')
plt.plot(data.index, data['SMA_50'], label="50-Day Simple Moving Avg", color='red')
plt.legend()
plt.show()
