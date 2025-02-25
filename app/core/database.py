from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.core.config import DATABASE_NAME, MONGO_URI


uri = MONGO_URI


#Create a new client and connect to the server

client = MongoClient(uri, server_api = ServerApi('1'))

db = client[DATABASE_NAME]
