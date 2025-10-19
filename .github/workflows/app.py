import os
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# Данные из переменных окружения
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

def send_message(text):
    """Отправляет сообщение в Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': CHAT_ID,
        'text': text
    }
    try:
        response = requests.post(url, data=data)
        print(f"{datetime.now()}: Отправлено - {text}")
        return response.json()
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def morning_job():
    """Задача для утреннего сообщения"""
    send_message("Доброе утро, любимая! ☀️ Пусть твой день будет наполнен улыбками и радостью! 💖")

def night_job():
    """Задача для ночного сообщения"""
    send_message("Спокойной ночи, моя прекрасная! 💫 Пусть тебе снятся самые сладкие сны. 💕")

# Создаем планировщик
scheduler = BlockingScheduler()

# Настраиваем расписание (время UTC!)
# Для Москвы (UTC+3): 8:00 по Москве = 5:00 UTC, 00:00 по Москве = 21:00 UTC
scheduler.add_job(morning_job, 'cron', hour=5, minute=0)   # 8:00 по Москве
scheduler.add_job(night_job, 'cron', hour=21, minute=0)    # 00:00 по Москве

if __name__ == "__main__":
    # Проверяем переменные
    if not BOT_TOKEN or not CHAT_ID:
        print("Ошибка: BOT_TOKEN или CHAT_ID не установлены!")
        exit(1)
    
    print("🤖 Бот запущен!")
    print("Расписание:")
    print("- Утреннее сообщение: 08:00 по Москве (05:00 UTC)")
    print("- Вечернее сообщение: 00:00 по Москве (21:00 UTC)")
    
    # Тестовое сообщение
    send_message("🤖 Бот запущен и готов работать!")
    
    # Запускаем планировщик
    try:
        scheduler.start()
    except KeyboardInterrupt:
        print("Бот остановлен")
