from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from src.handlers import (
    back_to_menu,
    help_command,
    show_affirmation,
    show_breathing,
    show_meditations,
    show_mood,
    show_relaxation,
    start,
)


def create_application():
    """Создает и настраивает приложение Telegram-бота."""
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(
        MessageHandler(
            filters.Regex("^🧘 Медитации$"),
            show_meditations,
        )
    )
    application.add_handler(
        MessageHandler(
            filters.Regex("^🌬 Дыхательные упражнения$"),
            show_breathing,
        )
    )
    application.add_handler(
        MessageHandler(
            filters.Regex("^🌿 Советы по релаксации$"),
            show_relaxation,
        )
    )
    application.add_handler(
        MessageHandler(
            filters.Regex("^😊 Трекер настроения$"),
            show_mood,
        )
    )
    application.add_handler(
        MessageHandler(
            filters.Regex("^💭 Ежедневные аффирмации$"),
            show_affirmation,
        )
    )
    application.add_handler(
        MessageHandler(
            filters.Regex("^⬅️ Назад$"),
            back_to_menu,
        )
    )

    return application