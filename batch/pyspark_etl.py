from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

os.environ["PYSPARK_SUBMIT_ARGS"] = "--conf spark.driver.extraJavaOptions=--add-opens=java.base/sun.nio.ch=ALL-UNNAMED pyspark-shell"

print("Starting Spark Session...")

spark = SparkSession.builder \
    .appName("RetailETL") \
    .master("local[*]") \
    .config("spark.sql.warehouse.dir", "file:///C:/tmp") \
    .getOrCreate()

print("Reading CSV Files...")

customers = spark.read.csv(
    "../data/customers.csv",
    header=True,
    inferSchema=True
)

products = spark.read.csv(
    "../data/products.csv",
    header=True,
    inferSchema=True
)

orders = spark.read.csv(
    "../data/orders.csv",
    header=True,
    inferSchema=True
)

print("Joining DataFrames...")

joined_df = orders.join(customers, "customer_id") \
                  .join(products, "product_id")

print("Calculating Revenue...")

final_df = joined_df.withColumn(
    "total_amount",
    col("quantity") * col("price")
)

print("Showing Final Data...")

final_df.show()

print("PySpark ETL Completed Successfully")

spark.stop()