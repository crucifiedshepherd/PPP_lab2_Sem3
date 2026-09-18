from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from src.data import BREATHING_EXERCISES, MEDITATIONS, RELAXATION_TIPS


def main_menu() -> ReplyKeyboardMarkup:
    """Create the main bot menu."""
    keyboard = [
        ["🧘 Медитации"],
        ["🌬 Дыхательные упражнения"],
        ["🌿 Советы по релаксации"],
        ["❓ Помощь"],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def meditation_menu() -> ReplyKeyboardMarkup:
    """Create the meditation selection menu."""
    keyboard = [
        ["Медитация на 5 минут"],
        ["Медитация перед сном"],
        ["Медитация для расслабления"],
        ["⬅️ Назад"],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def breathing_menu() -> ReplyKeyboardMarkup:
    """Create the breathing exercises menu."""
    keyboard = [
        ["Спокойное дыхание"],
        ["Дыхание 4-4"],
        ["⬅️ Назад"],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message and show the main menu."""
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
        "Также можно использовать кнопки меню.",
        reply_markup=main_menu(),
    )


async def show_meditations(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Show available meditation exercises."""
    await update.message.reply_text(
        "Выбери медитацию:",
        reply_markup=meditation_menu(),
    )


async def show_meditation(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Send the selected meditation."""
    meditation = MEDITATIONS.get(update.message.text)

    if meditation:
        await update.message.reply_text(
            meditation,
            reply_markup=meditation_menu(),
        )


async def show_breathing(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Show available breathing exercises."""
    await update.message.reply_text(
        "Выбери дыхательное упражнение:",
        reply_markup=breathing_menu(),
    )


async def show_breathing_exercise(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Send the selected breathing exercise."""
    exercise = BREATHING_EXERCISES.get(update.message.text)

    if exercise:
        await update.message.reply_text(
            exercise,
            reply_markup=breathing_menu(),
        )


async def show_relaxation_tips(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Show relaxation tips."""
    tips = "\n".join(
        f"• {tip}" for tip in RELAXATION_TIPS
    )

    await update.message.reply_text(
        f"Несколько простых советов:\n\n{tips}",
        reply_markup=main_menu(),
    )


async def back_to_menu(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Return to the main menu."""
    await update.message.reply_text(
        "Главное меню:",
        reply_markup=main_menu(),
    )