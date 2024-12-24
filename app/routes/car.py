from flask import  Blueprint, render_template,request,redirect,flash,logging,jsonify
from flask import url_for
from flask_login import logout_user
from ..functions import save_pictures
from ..forms import RegistrationForm
from ..forms import LoginForm
from flask_login import login_user
from flask_login import current_user
from flask_login import login_required
import requests
# from .user import get_cookie
from flask_login import current_user

car = Blueprint('car', __name__)


import requests


@car.route('/car', methods=['POST', 'GET'])
@login_required
def car_view():  
#    print("cookies_work", get_cookie())
    print("cookies_from FLASK_LOGIN", request.cookies)
    print("cookies_from FLASK_LOGIN_SESSION", request.cookies.get('session'))


    cars_url = 'https://qauto.forstudy.space/api/cars'
    # cookies=   get_cookie()

    #cookies=   request.cookies.get('session')
    cookies = {'session': request.cookies.get('session')}
    print("new cook", cookies)
    # Відправляємо запит для отримання даних автомобілів з передачею cookie
    cars_response = requests.get(cars_url, headers={'accept': 'application/json'}, cookies = cookies)
    print("Запит", cars_response)

    
    
    # Перевірка статусу відповіді
    if cars_response.status_code == 200:
#        print("Дані з реквесту", cars_response.text)
        cars_data = cars_response.json()  # Отримуємо JSON-відповідь
        cars_all = cars_data.get('data', [])  # Отримуємо список автомобілів
        
        if not cars_all:  # Перевірка, чи список автомобілів порожній
            print("Дані не знайдено")
    else:
        print(f"Не вдалося отримати дані про автомобілі. Статус код: {cars_response.status_code}")
        cars_all = []  # Якщо запит не вдався, створюємо порожній список

    # Передаємо дані у шаблон
    return render_template('car/car.html', cars=cars_all)




@car.route('/add_car', methods=['POST', 'GET'])
@login_required
def add_cars():
    # URL для запросов к API
    cars_brand_url = 'https://qauto.forstudy.space/api/cars/brands'
    cars_model_url = 'https://qauto.forstudy.space/api/cars/models'
    
    # Получаем cookie для авторизации
    
    cookies = get_cookie()

    # Запрос на получение брендов автомобилей
    cars_brand_response = requests.get(cars_brand_url, headers={'accept': 'application/json'}, cookies=cookies)
    
    if cars_brand_response.status_code == 200:
        cars_brands = cars_brand_response.json()  # Получаем ответ в формате JSON
        brand_list = cars_brands.get('data', [])
    else:
        brand_list = []  # Если запрос не удался, создаем пустой список

    # Запрос на получение моделей автомобилей
    cars_models_response = requests.get(cars_model_url, headers={'accept': 'application/json'}, cookies=cookies)
    
    if cars_models_response.status_code == 200:
        cars_models = cars_models_response.json()  # Получаем ответ в формате JSON
        models_list = cars_models.get('data', [])
    else:
        models_list = []  # Если запрос не удался, создаем пустой список
    
    # Отфильтровываем модели, если выбран бренд
    selected_brand_id = request.form.get('car-brand')  # Получаем выбранный бренд из формы
    if selected_brand_id:
        selected_brand_id = int(selected_brand_id)
        # Фильтруем модели по carBrandId
        filtered_models = [model for model in models_list if model['carBrandId'] == selected_brand_id]
    else:
        filtered_models = models_list  # Если бренд не выбран, показываем все модели

    # Передаем данные в шаблон
    return render_template('car/add_car.html', 
                           models_list={'data': filtered_models}, 
                           cars_brands=cars_brands)


  
# Маршрут для обработки кнопки Submit
@car.route('/car/create', methods=['POST'])
def create():
    cars_create_url = 'https://qauto.forstudy.space/api/cars'
    cookies = get_cookie()

    # Получение данных из формы
    car_brand_id = request.form.get('carBrandId')
    car_model_id = request.form.get('carModelId')
    mileage = request.form.get('mileage')

    # Проверка на заполненность полей
    if not (car_brand_id and car_model_id and mileage):
        return "Ошибка: все поля формы должны быть заполнены.", 400

    # Формирование тела запроса
    payload = {
        "carBrandId": int(car_brand_id),
        "carModelId": int(car_model_id),
        "mileage": int(mileage)
    }
    
    print("Отправляем данные на API:", payload)

    try:
        # Отправка POST-запроса
        response = requests.post(
            cars_create_url, 
            json=payload, 
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            cookies=cookies
        )

        # Логируем статус ответа
        print(f"Статус ответа API: {response.status_code}, Тело ответа: {response.text}")

        if response.status_code in [200, 201]:  # Успешный статус
            print("Машина успешно добавлена!")
            return redirect('/car')  # Перенаправление на страницу добавления
        else:
            return f"Ошибка при создании автомобиля: {response.status_code}, {response.text}", 400

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return "Произошла ошибка при соединении с API. Попробуйте позже.", 500

            
