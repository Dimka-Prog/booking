from flask import Flask
from flask_caching import Cache

import Controller.CalendarController as calendar
import Controller.AuthorizationController as authoriz
import Controller.AdministrationController as admin
import Controller.BookingCardController as card

app = Flask(__name__, template_folder='View/Template')

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 150,
    "SECRET_KEY": '12345'
}
app.config.from_mapping(config)

cache = Cache(app)


# получения данных для отображения календаря резервированных дат
@app.route('/', methods=["POST", "GET"])
def select_date():
    return calendar.select_date(cache)


# авторизация для пользователя и администратора
@app.route('/login', methods=["POST", "GET"])
def login():
    return authoriz.login(cache)


# получение и отображения данных всех бронирований
@app.route('/all_booking', methods=["POST", "GET"])
def all_booking():
    return admin.all_booking(cache)


# регистрации бронирования
@app.route('/booking/<date>', methods=["POST", "GET"])
def booking(date):
    return card.booking(date, cache)


if __name__ == '__main__':
    app.run(host='85.143.222.44')
