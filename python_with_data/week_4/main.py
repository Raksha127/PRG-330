
from module1_conditional import count_customers_by_gender
from module2_loop import find_popular_category
from module3_functions import calculate_sales_metrics
from module4_report import read_sales_data



file_name = "nepal_retail_sales_dataset.csv"


data = read_sales_data(file_name)



male_count, female_count = count_customers_by_gender(data)



popular_category, category_count = find_popular_category(data)



total_sales, average_sales = calculate_sales_metrics(data)



print("===== NEPAL RETAIL SALES ANALYSIS =====")

print("\nTotal Sales:")
print(f"NPR {total_sales:,.2f}")

print("\nAverage Sales:")
print(f"NPR {average_sales:,.2f}")

print("\nCustomer Gender:")
print(f"Male Customers: {male_count}")
print(f"Female Customers: {female_count}")

print("\nMost Popular Product Category:")
print(f"{popular_category} ({category_count} transactions)")