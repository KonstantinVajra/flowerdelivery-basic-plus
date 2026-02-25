# FlowerDelivery Basic+

Улучшенная (UI/UX) версия проекта **FlowerDelivery Basic** без изменения бизнес-логики:
- **без корзины**
- **заказ = один товар**
- **без статусов/пользователя в Order**
- Telegram-уведомления работают

## Стек
- Python 3.11
- Django 5.2.11
- SQLite
- python-dotenv
- requests

## Функциональность
- Каталог товаров: `/`
- Оформление заказа: `/order/<product_id>/`
- Страница успеха: `/order/success/`
- Регистрация: `/register/`
- Вход: `/accounts/login/`
- Выход: POST `/accounts/logout/`
- Django messages (успешный заказ)

## ENV
Создай файл `.env` в корне проекта:

```env
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...

.env не должен попадать в git.

Установка и запуск
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Открыть: http://127.0.0.1:8000/

Тесты
python manage.py test
Примечания

Проект предназначен для учебного/демо сценария.

UI улучшен, но архитектура и модель данных уровня Basic сохранены.


---

## Проверка (кратко)

1) `README.md` обновлён  
2) Команды в README запускаются  
3) Git diff показывает только README

Команды:
```bash
git diff