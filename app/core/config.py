from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from .env
MONGO_URI = os.getenv("MONGO_DB_CONNECTION_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME", "mydatabase")