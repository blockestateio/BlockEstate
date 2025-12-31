import tweepy
import random
import logging
from utils.config import config
from bots.auto_messages import MARKETING_MESSAGES, VIRAL_POSTS

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TwitterBot:
    def __init__(self):
        try:
            self.client = tweepy.Client(
                bearer_token=config.TWITTER_BEARER_TOKEN,
                consumer_key=config.TWITTER_API_KEY,
                consumer_secret=config.TWITTER_API_SECRET,
                access_token=config.TWITTER_ACCESS_TOKEN,
                access_token_secret=config.TWITTER_ACCESS_SECRET
            )
            logger.info("Twitter Client Initialized")
        except Exception as e:
            logger.error(f"Failed to initialize Twitter Client: {e}")
            self.client = None

    def post_to_twitter(self):
        """
        Posts a random marketing message to Twitter.
        """
        if not self.client:
            logger.warning("Twitter client not initialized. Skipping post.")
            return

        # Combine standard marketing messages with viral posts for variety
        all_messages = MARKETING_MESSAGES + VIRAL_POSTS
        message = random.choice(all_messages)
        try:
            response = self.client.create_tweet(text=message)
            logger.info(f"Tweet posted successfully: {message}")
            return response
        except Exception as e:
            logger.error(f"Failed to post tweet: {e}")

twitter_bot = TwitterBot()
