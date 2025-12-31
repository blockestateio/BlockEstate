import logging
import threading
import uvicorn
from utils.config import config
from backend.database import init_db
from utils.scheduler import start_scheduler
from bots.telegram_bot import run_telegram_bot
from backend.api import app

# Setup Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def run_fastapi():
    """Runs the FastAPI server."""
    uvicorn.run(app, host=config.API_HOST, port=config.API_PORT)

def main():
    logger.info("BlockEstate Automation System Running...")

    # 1. Initialize Database
    init_db()
    logger.info("Database initialized.")

    # 2. Start Scheduler
    start_scheduler()

    # 3. Start FastAPI Server in a separate thread
    # We run FastAPI in a thread so it doesn't block the Telegram bot
    api_thread = threading.Thread(target=run_fastapi, daemon=True)
    api_thread.start()
    logger.info(f"FastAPI server started on port {config.API_PORT}")

    # 4. Start Telegram Bot (Blocking)
    # This must be the last call as it blocks the main thread
    try:
        run_telegram_bot()
    except KeyboardInterrupt:
        logger.info("Stopping BlockEstate Bot...")

if __name__ == "__main__":
    main()
