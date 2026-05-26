import pandas as pd
from sqlalchemy import create_engine
import logging

logging.basicConfig(
    filename='logs/etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Reading CSV files...")

customers = pd.read_csv('data/customers.csv')
products = pd.read_csv('data/products.csv')
orders = pd.read_csv('data/orders.csv')

print("Customers Data:")
print(customers)

print("Products Data:")
print(products)

print("Orders Data:")
print(orders)

logging.info("Merging datasets...")

merged = orders.merge(customers, on='customer_id')
merged = merged.merge(products, on='product_id')

logging.info("Calculating total amount...")

merged['total_amount'] = merged['quantity'] * merged['price']

logging.info("Connecting to PostgreSQL...")
print(merged)

print("Connecting to PostgreSQL...")

engine = create_engine(
    'postgresql://postgres:Devdeep6200@localhost:5432/retail_dw'
)

print("Loading data into PostgreSQL...")

merged.to_sql(
    'sales_data',
    engine,
    if_exists='replace',
    index=False
)

logging.info("ETL Pipeline Completed Successfully")