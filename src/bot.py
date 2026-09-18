from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import BOT_TOKEN
from src.handlers import handle_message, help_command, start


def create_application() -> Application:
    """Create and configure the Telegram bot application."""
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    return application