from sqlalchemy.orm import Session
from backend.database import Query, Announcement, Log, SessionLocal
from datetime import datetime

class WebsiteManager:
    def __init__(self):
        self.db: Session = SessionLocal()

    def update_homepage_message(self, text: str):
        """
        Updates the homepage message. 
        In a real scenario, this might update a CMS or a file.
        Here we log it as an action.
        """
        self.log_action("INFO", f"Homepage message updated: {text}")
        return {"status": "success", "message": "Homepage message updated"}

    def save_user_query(self, name: str, email: str, message: str):
        """
        Saves a user query from the website to the database.
        """
        new_query = Query(name=name, email=email, message=message)
        self.db.add(new_query)
        self.db.commit()
        self.log_action("INFO", f"New user query saved from {email}")
        return {"status": "success", "message": "Query saved"}

    def fetch_token_stats(self):
        """
        Fetches token stats. 
        Placeholder for real blockchain data fetching.
        """
        stats = {
            "price": 1.25,
            "market_cap": 5000000,
            "holders": 1200,
            "volume_24h": 150000
        }
        return stats

    def post_news_update(self, title: str, content: str):
        """
        Posts a news update to the database.
        """
        new_announcement = Announcement(title=title, content=content)
        self.db.add(new_announcement)
        self.db.commit()
        self.log_action("INFO", f"News update posted: {title}")
        return {"status": "success", "message": "News update posted"}

    def log_action(self, level: str, message: str):
        """
        Logs an action to the database.
        """
        new_log = Log(level=level, message=message)
        self.db.add(new_log)
        self.db.commit()

    def __del__(self):
        self.db.close()

website_manager = WebsiteManager()
