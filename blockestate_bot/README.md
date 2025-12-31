# BlockEstate All-in-One Bot

This is the complete automation system for BlockEstate, integrating Telegram, Twitter, and Website management.

## Features
- **Telegram Bot**: Auto-replies, commands (/price, /website, etc.), anti-spam.
- **Twitter Bot**: Auto-posts marketing messages every 3 hours.
- **Website Manager**: Backend API for website updates and user queries.
- **Scheduler**: Manages background tasks.
- **API**: FastAPI backend for external integrations.

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configuration**
   - Open `utils/config.py` or create a `.env` file.
   - Set your API keys:
     - `TELEGRAM_BOT_TOKEN`
     - `TWITTER_API_KEY`
     - `TWITTER_API_SECRET`
     - `TWITTER_ACCESS_TOKEN`
     - `TWITTER_ACCESS_SECRET`
     - `TWITTER_BEARER_TOKEN`

3. **Run the System**
   ```bash
   python main.py
   ```

## API Endpoints
- `POST /update_home`: Update homepage message.
- `POST /send_announcement`: Post news update.
- `GET /stats`: Get token stats.
- `GET /health`: Health check.

## Folder Structure
- `bots/`: Bot logic (Telegram, Twitter).
- `backend/`: API and Database.
- `utils/`: Config and Scheduler.
- `main.py`: Entry point.
