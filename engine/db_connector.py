import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_collection():
    client = MongoClient(os.getenv("MONGO_URI"))
    # 'SocialAnalyzer' is the DB name, 'posts' is the collection
    db = client['SocialAnalyzer']
    return db['posts']