import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Токен берём из переменной окружения (на GitHub — из Secrets)
TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("Не задан BOT_TOKEN в переменных окружения")


async def game_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение с кнопками-ссылками по команде /game."""

    # --- НАСТРОЙКА ССЫЛОК ---
    # Формат: ("Текст кнопки", "Ссылка")
    buttons_data = [
        ("Правила", "https://example.com/rules"),
        ("Донат", "https://example.com/donate"),
        ("Новости", "https://example.com/news"),
        ("Поддержка", "https://example.com/support"),
    ]
    # -------------------------

    keyboard = [[InlineKeyboardButton(text, url=url)] for text, url in buttons_data]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text="Выберите нужный раздел:",
        reply_markup=reply_markup,
    )


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Отправь /game, чтобы увидеть меню.")


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("game", game_command))

    print("Бот запущен.")
    application.run_polling()


if __name__ == "__main__":
    main()
