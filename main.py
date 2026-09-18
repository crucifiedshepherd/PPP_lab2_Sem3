import logging

from src.bot import create_application


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def main():
    """Запускает Telegram-бота."""
    logger.info("Запуск Telegram-бота")

    application = create_application()
    application.run_polling()


if __name__ == "__main__":
    main()