def analyze_with_ai(df, question):

    question = question.lower()

    if "top product" in question:
        product = df.groupby("product")["sales"].sum().idxmax()
        return f"Top selling product is {product}"

    elif "best region" in question:
        region = df.groupby("region")["sales"].sum().idxmax()
        return f"Best performing region is {region}"

    elif "total sales" in question:
        total = df["sales"].sum()
        return f"Total sales is {total}"

    elif "average sales" in question:
        avg = df["sales"].mean()
        return f"Average sales value is {round(avg,2)}"

    else:
        return "I couldn't understand the question."