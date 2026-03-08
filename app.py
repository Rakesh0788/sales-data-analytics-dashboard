from flask import Flask, render_template, request
import pandas as pd

from ai_analyst import analyze_with_ai
from prediction import predict_sales
from insights import generate_insights

app = Flask(__name__)

df = pd.read_csv("dataset/sales_data.csv")


@app.route("/", methods=["GET", "POST"])
def dashboard():

    region_filter = request.args.get("region")

    filtered_df = df

    if region_filter:
        filtered_df = df[df["region"] == region_filter]

    # SALES BY PRODUCT
    sales_data = filtered_df.groupby("product")["sales"].sum()

    # SALES BY REGION
    region_data = filtered_df.groupby("region")["sales"].sum()

    # MONTHLY SALES (use month names)
    filtered_df["date"] = pd.to_datetime(filtered_df["date"])
    monthly_data = filtered_df.groupby(filtered_df["date"].dt.strftime('%b'))["sales"].sum()

    prediction = predict_sales(filtered_df)

    insights = generate_insights(filtered_df)

    regions = df["region"].unique()

    result = None

    if request.method == "POST":
        question = request.form["question"]
        result = analyze_with_ai(filtered_df, question)

    return render_template(
        "dashboard.html",

        products=sales_data.index.tolist(),
        values=sales_data.values.tolist(),

        region_labels=region_data.index.tolist(),
        region_values=region_data.values.tolist(),

        month_labels=monthly_data.index.tolist(),
        month_values=monthly_data.values.tolist(),

        prediction=prediction,
        insights=insights,
        regions=regions,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)