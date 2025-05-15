from prediction import predict_price
from plotting import plot_returns
from compare import plot_compare

def print_preds():
    actual,predicted = predict_price()
    print("\n\t\t-Predicted VS Actual Prices")
    for i in range(min(10,len(actual))):
        print(f"Actual:{actual[i]:.2f}  |  Predicted:{predicted[i]:.2f}")

def show_menu():
    while True:
        print("\nStock Price Prediction Menu")
        print("1. Visualise Stock History along with SMA and Bollinger bands")
        print("2. Compare Actual and Predicted Price")
        print("3. Print Predicted vs Actual price values")
        print("4. Exit")
        cho = input("Enter Your Choice (1-4): ")
        if cho=='1':
            plot_returns()
        elif cho=='2':
            plot_compare()
        elif cho=='3':
            print_preds()
        elif cho=='4':
            print("Exiting..")
            break;
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    show_menu()