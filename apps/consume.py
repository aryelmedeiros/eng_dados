# consume_and_process.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("MongoDBSpark").getOrCreate()

# MongoDB connection URI (replace with your MongoDB Atlas connection string)
mongo_uri = "mongodb+srv://<username>:<password>@your-cluster.mongodb.net/test?retryWrites=true&w=majority"

# Read data from MongoDB collection into a DataFrame
df = spark.read.format("mongo").option("uri", mongo_uri).load()

# Perform your data processing using PySpark DataFrame operations
processed_df = df.select(col("your_column").alias("new_column"))

# Specify the HDFS output path
hdfs_output_path = "hdfs:///user/spark/output_data"

# Write the processed DataFrame to HDFS in CSV format
processed_df.write.mode("overwrite").csv(hdfs_output_path)

print("Data processed and saved to HDFS.")