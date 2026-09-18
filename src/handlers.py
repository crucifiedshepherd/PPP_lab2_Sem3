from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message after the /start command."""
    await update.message.reply_text(
        "Привет! Я бот для медитации и ментального здоровья. 🧘\n"
        "Используй /help, чтобы посмотреть доступные команды."
    )


async def help_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Show available bot commands."""
    await update.message.reply_text(
        "/start — запустить бота\n"
        "/help — показать доступные команды"
    )