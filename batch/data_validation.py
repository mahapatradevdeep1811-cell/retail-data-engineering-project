import pandas as pd

print("Loading sales data...")

df = pd.read_csv('../data/orders.csv')

print(df)

print("Running Data Quality Checks...")

# Null Check
null_check = df.isnull().sum()

print("\nNull Values:")
print(null_check)

# Duplicate Check
duplicate_check = df.duplicated().sum()

print("\nDuplicate Records:")
print(duplicate_check)

# Negative Quantity Check
negative_quantity = df[df['quantity'] < 0]

print("\nNegative Quantity Records:")
print(negative_quantity)

if duplicate_check == 0 and negative_quantity.empty:
    print("\nData Validation Passed")
else:
    print("\nData Validation Failed")