from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# MongoDB Connection
client = MongoClient(os.getenv("MONGO_URI"))

db = client.get_default_database()

collection = db["posts"]

# Toxic / risky keywords
risk_keywords = [
    "scam",
    "fraud",
    "hate",
    "terrible",
    "kill",
    "attack",
    "abuse",
    "fake"
]

posts = collection.find()

for post in posts:

    text = post["content"]["text"].lower()

    risk_level = "Low"

    # Check risky keywords
    for word in risk_keywords:

        if word in text:
            risk_level = "High"
            break

    # Update database
    collection.update_one(
        {"_id": post["_id"]},
        {
            "$set": {
                "analysis.riskLevel": risk_level
            }
        }
    )

    print(f"✅ Updated Post: {post['externalId']} -> {risk_level}")

print("\n🚨 Risk Detection Complete")