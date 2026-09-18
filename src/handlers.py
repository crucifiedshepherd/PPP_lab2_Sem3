from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from src.data import (
    AFFIRMATION,
    BREATHING_EXERCISES,
    MEDITATIONS,
    MOOD_RESPONSES,
    RELAXATION_TIPS,
)


def main_menu():
    """Создает главное меню бота."""
    keyboard = [
        ["🧘 Медитации"],
        ["🌬 Дыхательные упражнения"],
        ["🌿 Советы по релаксации"],
        ["😊 Трекер настроения"],
        ["💭 Ежедневные аффирмации"],
        ["❓ Помощь"],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def meditation_menu():
    """Создает меню выбора медитации."""
    keyboard = [
        ["Медитация на 5 минут"],
        ["Медитация перед сном"],
        ["Медитация для расслабления"],
        ["⬅️ Назад"],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def breathing_menu():
    """Создает меню дыхательных упражнений."""
    keyboard = [
        ["Дыхание 4-4"],
        ["Дыхание для расслабления"],
        ["⬅️ Назад"],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показывает приветствие и главное меню."""
    await update.message.reply_text(
        "Привет! Я бот для медитации и ментального здоровья. 🧘\n"
        "Выбери нужный раздел в меню.",
        reply_markup=main_menu(),
    )


async def help_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """Показывает доступные команды бота."""
    await update.message.reply_text(
        "/start — запустить бота\n"
        "/help — показать помощь\n\n"
        "Также можно использовать кнопки меню.",
        reply_markup=main_menu(),
    )


async def show_meditations(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """Показывает доступные медитации."""
    await update.message.reply_text(
        "Выбери медитацию:",
        reply_markup=meditation_menu(),
    )


async def show_meditation(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """Показывает выбранную медитацию."""
    meditation = MEDITATIONS.get(update.message.text)

    if meditation:
        await update.message.reply_text(
            meditation,
            reply_markup=meditation_menu(),
        )


async def show_breathing(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """Показывает доступные дыхательные упражнения."""
    await update.message.reply_text(
        "Выбери дыхательное упражнение:",
        reply_markup=breathing_menu(),
    )


async def show_breathing_exercise(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """Показывает выбранное дыхательное упражнение."""
    exercise = BREATHING_EXERCISES.get(update.message.text)

    if exercise:
        await update.message.reply_text(
            exercise,
            reply_markup=breathing_menu(),
        )


async def show_relaxation_tips(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """Показывает советы по релаксации."""
    tips = "\n".join(
        f"• {tip}" for tip in RELAXATION_TIPS
    )

    await update.message.reply_text(
        f"Несколько простых советов:\n\n{tips}",
        reply_markup=main_menu(),
    )


async def back_to_menu(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """Возвращает пользователя в главное меню."""
    await update.message.reply_text(
        "Главное меню:",
        reply_markup=main_menu(),
    )