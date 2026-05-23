from pymongo import MongoClient
from dotenv import load_dotenv
from textblob import TextBlob
import os

load_dotenv()

# MongoDB Connection
client = MongoClient(os.getenv("MONGO_URI"))

db = client.get_default_database()

collection = db["posts"]

# Fetch all posts
posts = collection.find()

for post in posts:

    text = post["content"]["text"]

    # Sentiment Analysis
    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    # Determine sentiment
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Update MongoDB
    collection.update_one(
        {"_id": post["_id"]},
        {
            "$set": {
                "analysis.sentiment": sentiment
            }
        }
    )

    print(f"✅ Updated Post: {post['externalId']} -> {sentiment}")

print("\n🎉 Sentiment Analysis Complete")