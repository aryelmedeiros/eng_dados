# write_to_mongo.py

import pandas as pd
from pymongo import MongoClient

# Load your .csv file into a Pandas DataFrame
df = pd.read_csv('your_data.csv')

# MongoDB connection URI (replace with your MongoDB Atlas connection string)
mongo_uri = "mongodb+srv://<username>:<password>@your-cluster.mongodb.net/test?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(mongo_uri)

# Specify the database and collection
db = client['your_database']
collection = db['your_collection']

# Convert DataFrame to dictionary and insert into MongoDB collection
records = df.to_dict(orient='records')
collection.insert_many(records)

print("Data written to MongoDB Atlas.")