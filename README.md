# Airport and Mountain Information Bot

## Описание

Этот проект представляет собой бота Telegram, который предоставляет информацию об аэропортах и горах. Бот использует API для получения данных и предоставляет пользователям возможность искать информацию с помощью команд.

## Установка

1. **Клонируйте репозиторий**:
  
   git clone <URL-репозитория>
   cd <название-папки>
   

2. **Создайте виртуальное окружение и активируйте его**:
   
   python -m venv venv
   source venv/bin/activate  # для Linux/MacOS
   venv\Scripts\activate  # для Windows
  

3. **Установите зависимости**:
  
   pip install -r requirements.txt
 

4. **Создайте файл `.env` для хранения переменных окружения**:
   В корневом каталоге создайте файл `.env` и добавьте следующие переменные:
  
   BOT_TOKEN=<Ваш_токен_бота_Telegram>
   AIRPORTS_API_KEY=<Ваш_API_ключ_для_аэропортов>
   MOUNTAIN_API_KEY=<Ваш_API_ключ_для_гор>
 

## Использование

1. **Запустите бота**:
  
   python bot.py


2. **Используйте команды в Telegram**:
   - `/start` — приветственное сообщение и инструкция.
   - `/airport <название>` — поиск информации об аэропортах по названию.
   - `/mountain <название>` — поиск информации о горах по названию.

## Основные функции

- **fetch_airport_data**: Асинхронная функция для получения данных об аэропортах с помощью API. 
- **fetch_mountain_data**: Асинхронная функция для получения данных о горах с помощью API.
- **start_handler**: Обработчик команды `/start`.
- **airport_handler**: Обработчик команды `/airport` для поиска информации об аэропортах.
- **mountain_handler**: Обработчик команды `/mountain` для поиска информации о горах.

## Примечания

- Убедитесь, что у вас есть действительные API ключи и токен бота.
- В случае ошибок подключения или проблем с API проверьте правильность указанных ключей и токена в файле `.env`.

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности


смотрите в файле `LICENSE`.


Этот README файл предоставляет общее описание проекта, инструкции по установке, использованию и основные функции кода. Не забудьте заменить `<URL-репозитория>` и `<название-папки>` на актуальные значения при необходимости.



# Airport and Mountain Information Bot

This is a Telegram bot that allows users to search for information about airports and mountains. It uses the Aiogram library for handling Telegram bot interactions and the RapidAPI service for fetching data about airports and mountains.

## Features

- **Airport Search**: Users can get detailed information about airports, including name, IATA code, city, country, timezone, latitude, and longitude.
- **Mountain Search**: Users can retrieve information about mountains, including name, location, altitude, first climbed date, and first climber. If available, a mountain image is also displayed.

## Setup

1. Clone the repository:
 
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
  

2. Create a `.env` file in the root directory and add your API keys:

   BOT_TOKEN=your_telegram_bot_token
   AIRPORTS_API_KEY=your_airports_api_key
   MOUNTAIN_API_KEY=your_mountain_api_key
 

3. Install the required Python packages:
   
   pip install -r requirements.txt


## Usage

1. Start the bot:
  
   python main.py


2. In Telegram, start a chat with your bot and use the following commands:
   - `/start`: Welcome message with instructions.
   - `/airport <name>`: Search for an airport by name.
   - `/mountain <name>`: Search for a mountain by name.

## Dependencies

- Python 3.x
- Aiogram
- Aiohttp
- Python-dotenv

## Contributing

Feel free to open issues or submit pull requests if you would like to contribute to this project.

## License

This project is licensed under the MIT License.









