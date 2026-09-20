def calculate_sales_metrics(data):
    sales = []

    for row in data:
        sales.append(float(row["Sales_NPR"]))

    total_sales = sum(sales)
    average_sales = total_sales / len(sales)

    return total_sales, average_sales