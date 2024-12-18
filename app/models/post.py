from datetime import datetime
from ..extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(250))
    teacher = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))

    student = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    
  
      
# class Post(db.Model): # створює пусту таблицю
#     # 'id' - це унікальний ідентифікатор кожного поста.
#     # Він є первинним ключем таблиці, що означає, що кожен запис у таблиці буде мати унікальне значення в цьому стовпці.
#     id = db.Column(db.Integer, primary_key=True)

#     # 'subject' - це текстове поле, в якому зберігається тема або заголовок поста.
#     # В даному випадку максимальна довжина рядка обмежена 250 символами.
#     subject = db.Column(db.String(250))
