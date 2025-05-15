from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
#from sklearn.metrics import mean_absolute_error
from data_load import get_stock_price

def predict_price():
    print("Predicting....")
    data = get_stock_price()
    required_cols = ["SMA_50","EMA_50","RSI","Volatility","Close"]
    if not all(col in data.columns for col in required_cols):
        raise ValueError("Missing one or more required columns in data")

    x = data[["SMA_50" , "EMA_50" , "RSI" , "Volatility"]]
    y = data["Close"]
    x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2 , random_state=42)

    model = RandomForestRegressor(n_estimators=100 , random_state=42)
    model.fit(x_train,y_train)
    predictions = model.predict(x_test)

    return y_test.reset_index(drop=True), predictions
