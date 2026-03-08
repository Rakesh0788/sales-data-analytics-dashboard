import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_sales(df):

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month

    X = df[["month"]]
    y = df["sales"]

    model = LinearRegression()
    model.fit(X,y)

    next_month = [[12]]

    prediction = model.predict(next_month)

    return round(prediction[0],2)