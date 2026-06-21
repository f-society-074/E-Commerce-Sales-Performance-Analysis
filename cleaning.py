import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

# 1. Load the data
file_path = 'ecommerce_sales_34500.csv' 
df = pd.read_csv(file_path)

# First look at the data
print("--- First Look ---")
print(f"Number of rows: {df.shape[0]} | Number of columns: {df.shape[1]}")
print(df.head())

# 2. Remove duplicate rows
before_count = df.shape[0]
df.drop_duplicates(inplace=True)
after_count = df.shape[0]
print(f"\n[Done] Removed {before_count - after_count} duplicate rows.")

# 3. Fix order_date column
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
print("[Done] Converted date column to Datetime format.")

# 4. Clean spelling errors in payment_method column
df['payment_method'] = df['payment_method'].str.strip()
typos_dict = {
    'Credit Car': 'Credit Card',
    'Credit Can': 'Credit Card',
    'Debit Car': 'Debit Card'
}
df['payment_method'] = df['payment_method'].replace(typos_dict)
print("[Done] Fixed spelling errors and standardized payment method names.")

# 5. Check for missing values (Null / Missing Values)
print("\n--- Checking for missing values in columns ---")
missing_data = df.isnull().sum()
print(missing_data[missing_data > 0] if missing_data.sum() > 0 else "No missing values found!")

# 6. Save cleaned data to a new file
cleaned_file_path = 'cleaned_ecommerce_sales.csv'
df.to_csv(cleaned_file_path, index=False)
print(f"\n[Success] Data cleaned successfully and saved as: {cleaned_file_path}")
