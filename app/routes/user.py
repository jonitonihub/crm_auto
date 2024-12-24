from datetime import datetime
import requests

from flask import  Blueprint, render_template,request,redirect,flash,logging,jsonify,session
from flask import url_for
from flask_login import logout_user
from ..functions import save_pictures
# from ..extensions import db, bcrypt
from ..models.user import User
from ..forms import RegistrationForm
from ..forms import LoginForm
from flask_login import login_user
from flask_login import current_user
from flask_login import login_required
import requests


user = Blueprint('user', __name__)


# def get_cookie():
#     print(f'Get cookie from User {cookie}')
#     return cookie

@user.route('/user/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()  # Форма, которую вы используете

    if form.validate_on_submit():  # Проверка на отправку формы и ее валидацию
        email = form.login.data  # Получаем email из формы
        password = form.password.data  # Получаем пароль из формы
        remember = form.remember.data  # Получаем remember из формы (булевое значение)

        # Данные для авторизации
        auth_url = 'https://qauto.forstudy.space/api/auth/signin'
        auth_data = {
            "email": email,
            "password": password,
            "remember": remember
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Выполняем POST-запрос для авторизации
        auth_response = requests.post(auth_url, json=auth_data, headers=headers)

        # Проверка успешности авторизации
        if auth_response.status_code == 200:
            flash(f"Вітаємо, {email}. Ми успішно авторизовані.", "success")
            print("Авторизація успішна")
            
            # Получаем данные пользователя из ответа
            user_data = auth_response.json().get('data', {})
            print("Юзер дата", user_data)
            user_id = user_data.get('userId')  # ID пользователя (если есть)
            print("Юзер id", user_id)
            
            # # Сохраняем пользователя и cookies в сессию
            # session['user_data'] = {
            #     'userId': user_id,
            #     'email': email
            # }
            # # global cookie
            # # cookie= auth_response.cookies
            # # print("sessions", cookie)
            
            

            # Создаем объект пользователя
            user = User(id=user_id, email=email)
            print("user", user)

            # Входим в систему с использованием Flask-Login
            login_user(user)

            return redirect('/car')

        else:
            print("Авторизація не вдалася", auth_response.text)
            return "Авторизація не вдалася", 400
        
        
    return render_template('user/login.html', form=form)
            
            



@user.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()  # Осуществляем выход
    flash('Вы успешно вышли из системы', 'success')  # Выводим сообщение
    return redirect('/')
      


@user.route('/profile', methods=['GET', 'POST'])
def profile():
    profile_url = 'https://qauto.forstudy.space/api/users/profile'
    cookies = get_cookie()
    # Відправляємо запит для отримання даних користувача з передачею cookie
    profile_response = requests.get(profile_url, headers={'accept': 'application/json'}, cookies=cookies)
    
    # Перевірка статусу відповіді
    if profile_response.status_code == 200:
        # Отримуємо JSON-відповідь
        profile_data = profile_response.json()
        print("Дані з реквесту профайлу", profile_data)
    else:
        print(f"Не вдалося отримати дані профілю. Статус код: {profile_response.status_code}")
        profile_data = {}

    # Передаємо дані у шаблон
    return render_template('user/profile.html', profile=profile_data)
            



@user.route('/user/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()  # Форма, которую вы используете

    if form.validate_on_submit():  # Проверка на отправку формы и ее валидацию
        name = form.name.data
        lastName = form.lastName.data
        email = form.email.data  # Получаем email из формы
        password = form.password.data  # Получаем пароль из формы
        repeatPassword = form.repeatPassword.data


        # Данные для авторизации
        auth_url = 'https://qauto.forstudy.space/api/auth/signup'
        auth_data = {
            "name" : name,
            "lastName" : lastName,
            "email": email,
            "password": password,
            "repeatPassword": repeatPassword,

        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Выполняем POST-запрос для авторизации
        reg_response = requests.post(auth_url, json=auth_data, headers=headers)

        # Проверка успешности авторизации
        if reg_response.status_code == 201:
            flash(f"Вітаємо, {email}. Ми успішно Зареєструвались.", "success")
            print("Реєстрація успішна")
            
            # Получаем данные пользователя из ответа
            user_data = reg_response.json().get('data', {})
            print("Юзер дата", user_data)
            user_id = user_data.get('userId')  # ID пользователя (если есть)
            print("Юзер id", user_id)
            
            # Сохраняем пользователя и cookies в сессию
            session['user_data'] = {
                'userId': user_id,
                'email': email
            }


            global cookie
            cookie= reg_response.cookies
            print("sessions", cookie)
            
            

            # Создаем объект пользователя
            user = User(id=user_id, email=email)
            print("user", user)

            # Входим в систему с использованием Flask-Login
            login_user(user)

            return redirect('/car')

        else:
            print("Реєстрація не вдалася", reg_response.text)
            return "Реєстрація не вдалася", 400
        
        
    return render_template('user/singin.html', form=form)




@user.route('/', methods=['POST', 'GET'])
def all():
    # posts = Post.query.order_by(Post.date.desc()).all()  # Сортування за спаданням
    return render_template('post/all.html', user=User)