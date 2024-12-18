from flask import Flask
from .extensions import db, migrate, loginManager
from .config import Config
from .routes.user import user
from .routes.post import post
from .routes.car import car
# from .routes.main import main
from datetime import datetime
# from dotenv import load_dotenv



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # app.register_blueprint(main)
    app.register_blueprint(user)
    app.register_blueprint(post)
    app.register_blueprint(car)
    
    db.init_app(app)
    migrate.init_app(app, db)
    loginManager.init_app(app)
    
    # LOGIN MANAGER
    loginManager.login_view = "user.login"
    loginManager.login_message = "Ви неможете получить доступ к странице"
    

    with app.app_context():
        db.create_all()  # Исправлен отступ

    return app


# Коментарі:

# Імпорти:
# - `from flask import Flask`: Імпорт Flask для створення додатка.
# - `from .extensions import db`: Імпорт об’єкта бази даних (SQLAlchemy) із модуля `extensions`.
# - `from .config import Config`: Імпорт класу конфігурації.
# - `from .routes.user import user`: Імпорт блупринта для маршрутів, пов’язаних із користувачами.
# - `from .routes.post import post`: Імпорт блупринта для маршрутів постів.
# - `from .routes.main import main`: Імпорт блупринта для головних маршрутів.

# Функція `create_app`:
# - `def create_app(config_class=Config)`: Створює і налаштовує додаток Flask, використовуючи переданий клас конфігурації. За замовчуванням використовує клас `Config`.

# Ініціалізація додатка:
# - `app = Flask(__name__)`: Ініціалізація об’єкта додатка.
# - `app.config.from_object(config_class)`: Завантаження конфігурації з переданого класу конфігурації.

# Реєстрація блупринтів:
# - `app.register_blueprint(main)`: Підключення блупринта для основних маршрутів.
# - `app.register_blueprint(user)`: Підключення блупринта для маршрутів, пов'язаних із користувачами.
# - `app.register_blueprint(post)`: Підключення блупринта для маршрутів, пов'язаних із постами.

# Ініціалізація бази даних:
# - `db.init_app(app)`: Підключення бази даних до додатка.

# Створення таблиць у базі даних:
# - `with app.app_context(): db.create_all()`: У контексті додатка створюються всі таблиці, якщо вони ще не існують.

# Повернення об'єкта додатка:
# - `return app`: Повертає налаштований об'єкт додатка для подальшого використання або запуску.


