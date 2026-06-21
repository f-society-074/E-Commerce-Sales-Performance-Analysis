import pandas as pd

# 1. Load the cleaned data
df = pd.read_csv('cleaned_ecommerce_sales.csv')

# Ensure Python understands the date column correctly
df['order_date'] = pd.to_datetime(df['order_date'])

print("=============================================")
print(" Store Financial and Business Performance Report 📊")
print("=============================================\n")

# 📊 Question 1: General Statistics (Sales, Profit, and Orders)
total_sales = df['total_amount'].sum()
total_profit = df['profit_margin'].sum() # Total Profit
total_orders = df['order_id'].nunique()

print(f"💰 Total Sales (Revenue): ${total_sales:,.2f}")
print(f"📈 Net Profit (Total Profit): ${total_profit:,.2f}")
print(f"📦 Total Number of Successful Orders: {total_orders:,}")
print(f"💵 Average Order Value (AOV): ${df['total_amount'].mean():.2f}\n")


# 📊 Question 2: What are the top-selling and profitable product categories? (Top Categories)
print("--- 🛍️ Product Category Performance (Sales & Profit by Category) ---")
category_analysis = df.groupby('category').agg(
    Total_Sales=('total_amount', 'sum'),
    Total_Profit=('profit_margin', 'sum'),
    Quantity_Sold=('quantity', 'sum')
).sort_values(by='Total_Sales', ascending=False)

print(category_analysis.to_string())
print("\n")


# 📊 Question 3: Impact of Returns on Business (Returns Analysis)
print("--- 🔄 Returns Analysis (Returned Orders) ---")
return_counts = df['returned'].value_counts()
return_rate = (return_counts.get('Yes', 0) / len(df)) * 100
print(f"📉 Number of Returned Orders: {return_counts.get('Yes', 0)} orders")
print(f"🚨 Total Return Rate: {return_rate:.2f}%\n")


# 📊 Question 4: Customer Behavior by Gender (Demographics)
print("--- 👥 Store Sales by Gender (Sales by Gender) ---")
gender_analysis = df.groupby('customer_gender')['total_amount'].sum().sort_values(ascending=False)
print(gender_analysis.to_string())
print("\n")