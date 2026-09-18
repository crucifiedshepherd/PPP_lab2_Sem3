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
    show_breathing,
    show_breathing_exercise,
    show_meditation,
    show_meditations,
    show_relaxation_tips,
    start,
)


def create_application() -> Application:
    """Create and configure the Telegram bot application."""
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
            show_relaxation_tips,
        )
    )
    application.add_handler(
        MessageHandler(
            filters.Regex("^❓ Помощь$"),
            help_command,
        )
    )
    application.add_handler(
        MessageHandler(
            filters.Regex("^⬅️ Назад$"),
            back_to_menu,
        )
    )
    application.add_handler(
        MessageHandler(
            filters.Regex(
                "^(Спокойное дыхание|Дыхание 4-4)$"
            ),
            show_breathing_exercise,
        )
    )
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            show_meditation,
        )
    )

    return application