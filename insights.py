def generate_insights(df):

    insights = []

    top_region = df.groupby("region")["sales"].sum().idxmax()
    insights.append(f"Top region: {top_region}")

    top_product = df.groupby("product")["sales"].sum().idxmax()
    insights.append(f"Best selling product: {top_product}")

    total_sales = df["sales"].sum()
    insights.append(f"Total revenue: {total_sales}")

    avg_sales = df["sales"].mean()
    insights.append(f"Average sales value: {round(avg_sales,2)}")

    return insights