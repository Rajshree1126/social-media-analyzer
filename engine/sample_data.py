from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

db = client.get_default_database()

collection = db["posts"]

sample_posts = [
    {
        "platform": "Twitter",
        "externalId": "001",
        "content": {
            "text": "AI tools are improving productivity massively.",
            "media": []
        },
        "metadata": {
            "likes": 120,
            "shares": 30
        },
        "analysis": {
            "sentiment": "Pending",
            "riskLevel": "Low"
        }
    },

    {
        "platform": "Twitter",
        "externalId": "002",
        "content": {
            "text": "This company is terrible and scams people.",
            "media": []
        },
        "metadata": {
            "likes": 12,
            "shares": 2
        },
        "analysis": {
            "sentiment": "Pending",
            "riskLevel": "High"
        }
    },

    {
        "platform": "Instagram",
        "externalId": "003",
        "content": {
            "text": "Amazing customer service and fast delivery.",
            "media": []
        },
        "metadata": {
            "likes": 400
        },
        "analysis": {
            "sentiment": "Pending",
            "riskLevel": "Low"
        }
    }
]

collection.insert_many(sample_posts)

print("✅ Sample data inserted successfully")