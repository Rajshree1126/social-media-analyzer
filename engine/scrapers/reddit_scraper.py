import praw
import os
import sys
# Adding parent directory to path so we can import db_connector
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_connector import get_collection
from dotenv import load_dotenv

load_dotenv()

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="SocialMediaAnalyzer v1.0 by /u/your_username"
)

def scrape_subreddit(subreddit_name, limit=10):
    collection = get_collection()
    subreddit = reddit.subreddit(subreddit_name)
    
    print(f"--- Scraping r/{subreddit_name} ---")
    
    for post in subreddit.hot(limit=limit):
        # Formatting data to match our Mongoose Schema
        post_data = {
            "platform": "Reddit",
            "externalId": post.id,
            "content": {
                "text": post.title + " " + post.selftext,
                "media": [post.url] if hasattr(post, 'url') else []
            },
            "metadata": {
                "score": post.score,
                "num_comments": post.num_comments,
                "subreddit": subreddit_name
            },
            "analysis": {
                "sentiment": "Pending",
                "riskLevel": "Low"
            }
        }
        
        try:
            # Upsert (Update if exists, Insert if not) to prevent duplicates
            collection.update_one(
                {"externalId": post.id},
                {"$set": post_data},
                upsert=True
            )
            print(f"✅ Saved: {post.title[:50]}...")
        except Exception as e:
            print(f"❌ Error saving post: {e}")

if __name__ == "__main__":
    scrape_subreddit("technology", limit=5)