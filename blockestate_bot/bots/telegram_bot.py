import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from utils.config import config
from bots.auto_messages import (
    TELEGRAM_WELCOME_MESSAGE,
    TELEGRAM_PRICE_MESSAGE,
    TELEGRAM_WEBSITE_MESSAGE,
    TELEGRAM_WHITEPAPER_MESSAGE
)

# Setup Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(TELEGRAM_WELCOME_MESSAGE)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(TELEGRAM_WELCOME_MESSAGE)

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(TELEGRAM_PRICE_MESSAGE)

async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(TELEGRAM_WEBSITE_MESSAGE)

async def whitepaper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(TELEGRAM_WHITEPAPER_MESSAGE)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Auto-reply to messages and basic anti-spam (placeholder logic).
    """
    text = update.message.text
    user = update.effective_user
    
    # Basic Anti-Spam: Ignore messages with links from non-admins (simplified)
    if "http" in text or "www" in text:
        # In a real bot, check if user is admin. For now, just log.
        logger.info(f"Link detected from {user.first_name}: {text}")
        # await update.message.delete() # Uncomment to enable deletion
        return

    # Auto-reply template
    response = "Thank you for contacting BlockEstate.\nA team member will reach out soon."
    await update.message.reply_text(response)

def run_telegram_bot():
    if not config.TELEGRAM_BOT_TOKEN or config.TELEGRAM_BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN":
        logger.warning("Telegram Bot Token not set. Skipping Telegram Bot startup.")
        return

    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('price', price))
    application.add_handler(CommandHandler('website', website))
    application.add_handler(CommandHandler('whitepaper', whitepaper))
    
    # Handle text messages
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    logger.info("Starting Telegram Bot...")
    application.run_polling()
