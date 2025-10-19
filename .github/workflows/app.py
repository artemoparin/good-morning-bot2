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
