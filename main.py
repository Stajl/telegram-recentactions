#!/usr/bin/env python3

import os
from decouple import config
from telethon import TelegramClient
from telethon.tl.types import PeerChannel
import json
import asyncio
from datetime import datetime
import base64

# Завантажуємо API-креденшали
api_id = config('API_ID', default=None, cast=int)
api_hash = config('API_HASH', default=None)
group_id = config('GROUP_CHAT_ID', default=None, cast=str)

if not api_id or not api_hash or not group_id:
    raise ValueError("API_ID, API_HASH або GROUP_CHAT_ID не задано у .env")

# Функція для серіалізації нестандартних типів
def serialize_special(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Конвертуємо datetime у строку ISO-8601
    if isinstance(obj, bytes):
        return base64.b64encode(obj).decode('utf-8')  # Конвертуємо bytes у base64
    raise TypeError(f"Type {type(obj)} not serializable")

# Основна асинхронна функція
async def main():
    # Ініціалізація клієнта
    client = TelegramClient('session_name', api_id, api_hash)

    print("Запуск Telegram клієнта...")
    await client.start()
    print("Клієнт успішно підключено!")

    print("Отримання даних групи...")
    try:
        group = await client.get_entity(PeerChannel(int(group_id)))
        print(f"Група знайдена: {group.title}")
    except Exception as e:
        print(f"Помилка отримання групи: {e}")
        return

    # Логування дій адміністраторів
    data = []
    print("Завантаження дій адміністраторів...")
    try:
        async for event in client.iter_admin_log(group):
            if event.deleted_message:
                event_data = event.old.to_dict()
                data.append(event_data)
                if event.old.media:
                    await client.download_media(event.old.media, str(event.old.id))
    except Exception as e:
        print(f"Помилка під час логування: {e}")
        return

    # Збереження до JSON
    print("Збереження до файлу dump.json...")
    try:
        with open("dump.json", "w") as file:
            json.dump(data, file, indent=4, default=serialize_special)
        print("Дані успішно збережені!")
    except Exception as e:
        print(f"Помилка збереження файлу: {e}")

# Виконуємо асинхронну функцію
if __name__ == "__main__":
    asyncio.run(main())
