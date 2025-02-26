import os
import pandas as pd
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from app.core.config import MONGO_SERVERLESS_URI, DATABASE_NAME 


def generate_sales_report(event, context):
    # Connect to MongoDB
    client = MongoClient(MONGO_SERVERLESS_URI)
    db = client[DATABASE_NAME]
    collection = db['order']

    orders = collection.find()
    
    # Convert the MongoDB cursor to a list of dictionaries
    orders_data = list(orders)
    
    # If you want to remove the MongoDB-specific `_id` field (which is an ObjectId)
    for order in orders_data:
        order["_id"] = str(order["_id"])  # Convert ObjectId to string

    # Create a DataFrame with the retrieved data
    df = pd.DataFrame(orders_data)
    

    file_directory = f'{os.getcwd()}/serverless/reports'

    if not os.path.isdir(file_directory):
        os.makedirs(file_directory, exist_ok=True)

    csv_file_path = f'{file_directory}/orders_report-{int(datetime.timestamp(datetime.now()))}.csv'

    # Define the CSV file path (in the Lambda /tmp directory)
    
    # Save the DataFrame as a CSV file
    df.to_csv(csv_file_path, index=False)
    
    # Return the response with the file path where the CSV was saved
    return {
        'statusCode': 200,
        'body': f"CSV file generated and saved at {csv_file_path}",
    }
