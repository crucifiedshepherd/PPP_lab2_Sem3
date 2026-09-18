from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from src.data import (
    AFFIRMATIONS,
    BREATHING_EXERCISES,
    MEDITATIONS,
    MOODS,
    RELAXATION_TIPS,
)


def main_menu() -> ReplyKeyboardMarkup:
    """Create the main menu keyboard."""
    keyboard = [
        ["🧘 Медитации"],
        ["🌬 Дыхательные упражнения"],
        ["🌿 Советы по релаксации"],
        ["😊 Трекер настроения"],
        ["💭 Ежедневные аффирмации"],
        ["❓ Помощь"],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the welcome message and show the main menu."""
    await update.message.reply_text(
        "Привет! Я бот для медитации и ментального здоровья. 🧘\n"
        "Выбери нужный раздел в меню.",
        reply_markup=main_menu(),
    )


async def help_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Show available bot commands."""
    await update.message.reply_text(
        "/start — запустить бота\n"
        "/help — показать помощь\n\n"
        "Также можно использовать кнопки меню."
    )


async def handle_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Process messages received from the main menu."""
    message = update.message.text

    if message == "🧘 Медитации":
        keyboard = [
            list(MEDITATIONS.keys()),
            ["⬅️ Назад"],
        ]
        await update.message.reply_text(
            "Выбери медитацию:",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True,
            ),
        )

    elif message in MEDITATIONS:
        await update.message.reply_text(MEDITATIONS[message])

    elif message == "🌬 Дыхательные упражнения":
        keyboard = [
            list(BREATHING_EXERCISES.keys()),
            ["⬅️ Назад"],
        ]
        await update.message.reply_text(
            "Выбери дыхательное упражнение:",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True,
            ),
        )

    elif message in BREATHING_EXERCISES:
        await update.message.reply_text(BREATHING_EXERCISES[message])

    elif message == "🌿 Советы по релаксации":
        await update.message.reply_text(RELAXATION_TIPS)

    elif message == "😊 Трекер настроения":
        keyboard = [
            ["😊 Хорошее", "🙂 Нормальное"],
            ["😐 Нейтральное", "😔 Грустное"],
            ["😣 Тревожное"],
            ["⬅️ Назад"],
        ]
        await update.message.reply_text(
            "Какое у тебя сейчас настроение?",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True,
            ),
        )

    elif message in MOODS:
        await update.message.reply_text(MOODS[message])

    elif message == "💭 Ежедневные аффирмации":
        affirmation = AFFIRMATIONS[0]
        await update.message.reply_text(
            f"Твоя аффирмация на сегодня:\n\n{affirmation}"
        )

    elif message == "⬅️ Назад":
        await update.message.reply_text(
            "Главное меню:",
            reply_markup=main_menu(),
        )

    elif message == "❓ Помощь":
        await help_command(update, context)