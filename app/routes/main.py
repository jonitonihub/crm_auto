# from flask import  Blueprint, render_template

# main = Blueprint('main', __name__)


# @main.route('/index')
# @main.route('/')
# def index():
#     return render_template('main/index.html')








# Імпорт класу Blueprint і функції render_template з Flask

# Створення блупринта 'main' для головних маршрутів додатка.
# 'main' - це ім'я блупринта, яке буде використовуватися для його ідентифікації
# __name__ - використовується для налаштування шляху до шаблонів, що пов’язані з цим блупринтом

# Маршрут для головної сторінки
# @main.route('/index') – створює маршрут, доступний за URL /index
# @main.route('/') – створює альтернативний маршрут для цього ж представлення, доступний за кореневою адресою (/)

"""
Відображає головну сторінку додатка, використовуючи шаблон main/index.html.

Повертає:
- Відрендерений HTML шаблон 'main/index.html'.
"""

# render_template викликає шаблон із директорії шаблонів (templates).
# У цьому випадку він шукає файл main/index.html і відображає його в браузері.
