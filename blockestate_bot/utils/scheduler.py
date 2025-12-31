from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from bots.twitter_bot import twitter_bot
from backend.database import SessionLocal, Log
from datetime import datetime, timedelta
from utils.config import config
import logging

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def scheduled_twitter_post():
    logger.info("Running scheduled Twitter post...")
    twitter_bot.post_to_twitter()

def scheduled_telegram_announcement():
    logger.info("Running scheduled Telegram announcement...")
    # Logic to send announcement to Telegram channel would go here
    # For now, we just log it as per requirements
    pass

def daily_log_cleanup():
    logger.info("Running daily log cleanup...")
    db = SessionLocal()
    try:
        # Delete logs older than 7 days
        cutoff_date = datetime.utcnow() - timedelta(days=7)
        deleted_count = db.query(Log).filter(Log.timestamp < cutoff_date).delete()
        db.commit()
        logger.info(f"Deleted {deleted_count} old logs.")
    except Exception as e:
        logger.error(f"Error cleaning logs: {e}")
    finally:
        db.close()

def start_scheduler():
    # Schedule Twitter Post
    scheduler.add_job(
        scheduled_twitter_post,
        trigger=IntervalTrigger(hours=config.TWITTER_POST_INTERVAL_HOURS),
        id='twitter_post',
        name='Post to Twitter every X hours',
        replace_existing=True
    )

    # Schedule Telegram Announcement
    scheduler.add_job(
        scheduled_telegram_announcement,
        trigger=IntervalTrigger(hours=config.TELEGRAM_ANNOUNCEMENT_INTERVAL_HOURS),
        id='telegram_announcement',
        name='Send Telegram announcement every X hours',
        replace_existing=True
    )

    # Schedule Daily Log Cleanup
    scheduler.add_job(
        daily_log_cleanup,
        trigger=IntervalTrigger(days=1),
        id='log_cleanup',
        name='Clean up old logs daily',
        replace_existing=True
    )

    scheduler.start()
    logger.info("Scheduler started...")
