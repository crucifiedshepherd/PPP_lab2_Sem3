from telegram.ext import Application, CommandHandler

from config import BOT_TOKEN
from src.handlers import help_command, start


def create_application() -> Application:
    """Создание и конфигурация ТГ-бота"""
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    return application