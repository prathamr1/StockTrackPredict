import matplotlib.pyplot as plt
from prediction import predict_price

def plot_compare():
    actual,predicted = predict_price()

    plt.figure(figsize=(10,6))
    plt.plot(actual, label='Actual Price', color='blue')
    plt.plot(predicted, label='Predicted Price', color='orange')
    plt.title("Actual VS Predicted Prices")
    plt.xlabel("Samples")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.show()