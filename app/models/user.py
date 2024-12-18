from ..extensions import db, loginManager
from datetime import datetime
from flask_login import UserMixin
from .post import Post
from flask import session




class User(UserMixin):
    def __init__(self, id, email):
        self.id = id
        self.email = email

    def __repr__(self):
        return f'<User {self.email}>'




@loginManager.user_loader
def load_user(user_id):
    user_data = session.get('user_data')
    if user_data:
        # Используйте правильные имена параметров (id и email)
        return User(id=user_data['userId'], email=user_data['email'])
    return None







