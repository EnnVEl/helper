# Telegram bot

Бот присылает по команде `/game` сообщение с кнопками-ссылками.

## Локальный запуск

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env           # впиши свой токен в .env
export BOT_TOKEN=$(grep BOT_TOKEN .env | cut -d= -f2)   # или используй python-dotenv
python bot.py
