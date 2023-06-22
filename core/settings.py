"""
Project Settings file
"""
import os


# Mongo configuration
mongo_max_connections = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
mongo_min_connections = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))
db_name = "mydatabase"
mongo_url = f"mongodb://localhost:27017/{db_name}"


API_TOKEN = '6015591015:AAHcPG8iuRvjeV3yvRkACOCkk7u4AcHJo6c'
