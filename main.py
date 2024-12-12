import asyncio
import aiohttp
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
AIRPORTS_API_KEY = os.getenv("AIRPORTS_API_KEY")
MOUNTAIN_API_KEY = os.getenv("MOUNTAIN_API_KEY")

# Проверка обязательных переменных окружения
if not BOT_TOKEN or not AIRPORTS_API_KEY or not MOUNTAIN_API_KEY:
    raise ValueError("Убедитесь, что BOT_TOKEN, AIRPORTS_API_KEY и MOUNTAIN_API_KEY заданы в файле .env")

# Инициализация бота
bot = Bot(token=BOT_TOKEN)


# Функция для получения данных об аэропортах
async def fetch_airport_data(search_query):
    url = "https://airports.p.rapidapi.com/v1/airports"
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": AIRPORTS_API_KEY,
        "X-RapidAPI-Host": "airports.p.rapidapi.com"
    }
    payload = {"search": search_query}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=payload) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Ошибка API аэропортов: {response.status} - {await response.text()}")
                    return None
    except aiohttp.ClientError as e:
        print(f"Ошибка подключения к API аэропортов: {e}")
        return None


# Функция для получения данных о горах
async def fetch_mountain_data(mountain_name):
    url = f"https://mountain-api1.p.rapidapi.com/api/mountains?name={mountain_name}"
    headers = {
        "X-RapidAPI-Key": MOUNTAIN_API_KEY,
        "X-RapidAPI-Host": "mountain-api1.p.rapidapi.com"
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"API Response: {data}")  # Логируем ответ API
                    return data
                else:
                    print(f"Ошибка API гор: {response.status} - {await response.text()}")
                    return None
    except aiohttp.ClientError as e:
        print(f"Ошибка подключения к API гор: {e}")
        return None



# Обработчик команды для поиска аэропорта
async def airport_handler(message: Message):
    search_query = message.text.replace("/airport", "").strip()
    if not search_query:
        await message.answer("✈️ Пожалуйста, укажите название аэропорта после команды /airport.")
        return

    data = await fetch_airport_data(search_query)
    if not data or not isinstance(data, list):
        await message.answer("✈️Аэропорты не найдены. Попробуйте уточнить запрос.")
        return

    response = []
    for airport in data:
        info = (
            f"\u2708\ufe0f <b>Название:</b> {airport.get('name', 'Неизвестно')}\n"
            f"<b>Код IATA:</b> {airport.get('iata', 'Не указано')}\n"
            f"<b>Город:</b> {airport.get('city', 'Неизвестно')}\n"
            f"<b>Страна:</b> {airport.get('country', 'Неизвестно')}\n"
            f"<b>Часовой пояс:</b> {airport.get('tz', 'Не указано')}\n"
            f"<b>Широта:</b> {airport.get('lat', 'Не указано')}\n"
            f"<b>Долгота:</b> {airport.get('lon', 'Не указано')}\n"
        )
        response.append(info)

    await message.answer("\n\n".join(response), parse_mode="HTML")


# Обработчик команды /start
async def start_handler(message: Message):
    await message.answer("Привет! Используйте команду /airport для поиска аэропорта или /mountain для поиска горы.")


# Обработчик команды для поиска горы
async def mountain_handler(message: Message):
    mountain_name = message.text.replace("/mountain", "").strip()
    if not mountain_name:
        await message.answer("🏔️ Пожалуйста, укажите название горы после команды /mountain.")
        return

    data = await fetch_mountain_data(mountain_name)
    if not data:
        await message.answer("❌ Гора не найдена. Попробуйте уточнить запрос.")
        return

    # Если API возвращает только один объект, обработка изменена:
    response = (
        f"⛰️ <b>Название:</b> {data.get('name', 'Неизвестно')}\n"
        f"<b>Местоположение:</b> {data.get('location', 'Не указано')}\n"
        f"<b>Высота:</b> {data.get('altitude', 'Не указано')}\n"
        f"<b>Первая экспедиция:</b> {data.get('first_climbed_date', 'Неизвестно')} "
        f"({data.get('first_climber', 'Неизвестно')})\n"
    )
    photo_url = data.get("mountain_img", None)

    if photo_url:
        await message.answer_photo(photo=photo_url, caption=response, parse_mode="HTML")
    else:
        await message.answer(response, parse_mode="HTML")



# Главная функция
async def main():
    dp = Dispatcher()

    # Регистрация обработчиков
    dp.message.register(start_handler, Command("start"))
    dp.message.register(airport_handler, Command("airport"))
    dp.message.register(mountain_handler, Command("mountain"))

    await dp.start_polling(bot)


# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())









