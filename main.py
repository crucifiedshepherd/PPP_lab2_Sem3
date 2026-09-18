from src.bot import create_application


def main() -> None:
    """Запуск Telegram бота"""
    application = create_application()
    application.run_polling()


if __name__ == "__main__":
    main()