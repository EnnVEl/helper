import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Включаем логирование, чтобы видеть ошибки
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def game_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение с кнопками-ссылками по команде /game."""
    
    # --- НАСТРОЙКА ВАШИХ ССЫЛОК И ТЕКСТА ---
    # Формат: ("Текст кнопки", "Ссылка")
    # Можно добавить сколько угодно слов/кнопок
    buttons_data = [
        ("Правила", "https://example.com/rules"),
        ("Донат", "https://example.com/donate"),
        ("Новости", "https://example.com/news"),
        ("Поддержка", "https://example.com/support")
    ]
    # ---------------------------------------

    # Создаем список кнопок. 
    # В данном случае каждая кнопка будет в отдельном ряду (одна под другой).
    keyboard = []
    for text, url in buttons_data:
        keyboard.append([InlineKeyboardButton(text, url=url)])

    # Обертка для отправки
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Текст сообщения, которое придет вместе с кнопками
    message_text = "Выберите нужный раздел:"

    # Отправляем сообщение в тот чат, где была вызвана команда (личка или группа)
    await update.message.reply_text(
        text=message_text,
        reply_markup=reply_markup
    )

def main() -> None:
    # Создаем приложение с вашим токеном
    application = Application.builder().token("ВАШ_ТОКЕН_ЗДЕСЬ").build()

    # Регистрируем команду /game
    application.add_handler(CommandHandler("game", game_command))

    # Запускаем бота
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    application.run_polling()

if __name__ == "__main__":
    main()
