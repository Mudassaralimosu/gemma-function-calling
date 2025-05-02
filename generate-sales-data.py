import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate sample data
np.random.seed(42)
num_records = 1000

products = ["Wireless Headphones", "Smartphone", "Laptop", "Tablet", 
            "Smart Watch", "Bluetooth Speaker", "Monitor", "Keyboard", "Mouse", "External SSD"]
regions = ["North", "South", "East", "West"]

data = {
    "order_id": range(1001, 1001 + num_records),
    "product_name": np.random.choice(products, num_records),
    "quantity": np.random.randint(1, 11, num_records),
    "unit_price": np.round(np.random.uniform(50, 1500, num_records), 2),
    "customer_age": np.random.randint(18, 70, num_records),
    "region": np.random.choice(regions, num_records),
    "purchase_date": pd.date_range(start="2024-01-01", periods=num_records).strftime('%Y-%m-%d')
}

# Calculate revenue
df = pd.DataFrame(data)
df["revenue"] = df["quantity"] * df["unit_price"]

# Save to CSV
df.to_csv("sales_data.csv", index=False, 
          columns=["order_id", "product_name", "quantity", "revenue", 
                   "customer_age", "region", "purchase_date"])
print("Generated sales_data.csv with 1000 records")