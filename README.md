# FlowerDelivery Basic

Минимальный Django-проект доставки цветов.

- Без корзины
- Один заказ = один товар
- Каталог товаров + оформление заказа
- Регистрация / логин / логаут
- Уведомление о заказе в Telegram (опционально)

## Стек

- Python 3.11
- Django 5.2.11
- SQLite

## Установка

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt

Переменные окружения

Создай файл .env в корне проекта:

TELEGRAM_BOT_TOKEN=YOUR_TOKEN
TELEGRAM_CHAT_ID=YOUR_CHAT_ID

Если переменные не заданы — проект работает, просто без Telegram-уведомлений.

Запуск
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Открыть:

Каталог: http://127.0.0.1:8000/

Админка: http://127.0.0.1:8000/admin/

Тесты
python manage.py test

### Команды (терминал PyCharm)
```bash
git status