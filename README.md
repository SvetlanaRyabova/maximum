# Автотесты "Страница авторизации ВТБ Онлайн"

Установка:
1. Версия python от 3.9
2. Установить виртуальное окружение
python3 -m venv venv
3. Активировать виртуально окружение
source venv/bin/activate
4. Установить библиотеки
pip install -r requirements.txt

Запуск тестов в Chrome:
- pytest

Запуск тестов в Firefox:
- pytest --browser="firefox" 