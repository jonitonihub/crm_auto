from flask import Flask
from .routes.user import user
from .routes.car import car
from datetime import datetime
from flask import Blueprint
from .config import Config
from flask_login import LoginManager
from .extensions import loginManager




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(user)
    app.register_blueprint(car)  
    loginManager.init_app(app)
    
    # LOGIN MANAGER
    loginManager.login_view = "user.login"
    loginManager.login_message = "Ви неможете получить доступ к странице"
   

    return app