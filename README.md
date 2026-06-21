## 🐍 Python Script & Data Pipeline

The raw dataset contained transactional noise, missing variables, and formatting inconsistencies. A Python script (`data_preprocessing.py`) was developed using the **Pandas** and **NumPy** libraries to clean, transform, and extract financial insights prior to visualization.

### 🛠️ Data Challenges Addressed (What the Python Code Fixed)

1. **Handling Missing & Null Values:**
   * Detected and treated missing entries in crucial columns. For instance, missing values in numerical features like `quantity` or `price` were imputed based on logic, ensuring no skewness in the total revenue calculation.

2. **Data Type Correction & Standardization:**
   * Converted the `order_date` column from a generic string text type format into a standardized `datetime64` object. This was essential for establishing accurate time-series analysis in Power BI.
   * Enforced correct numerical constraints on financial metrics such as `total_amount` and `profit_margin`.

3. **Feature Engineering & Financial Calculation:**
   * Formulated the business logic to cross-verify that `total_amount` matches ($quantity \times price$) after factoring in any applied `discount`.
   * Programmatically isolated individual product metrics to isolate and expose categories operating at a negative profit margin (the Grocery issue).

4. **Anomalies and Duplicates Removal:**
   * Identified and dropped duplicate transactional records based on unique `order_id` constraints to prevent overestimating sales figures.
   * Trimmed leading/trailing whitespaces from text categorical columns (`category`, `payment_method`, `region`) to ensure precise group-by aggregation filters.

5. **Exporting Clean Baseline:**
   * Streamlined the final pipeline to output a clean, optimized CSV file (`cleaned_ecommerce_sales.csv`) ready for direct ingestion by Power BI without requiring additional Power Query heavy-lifting.
