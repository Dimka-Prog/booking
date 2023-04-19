from flask import Flask
from flask_caching import Cache

import Controller.AuthorizationController as authoriz
import Controller.AdministrationController as admin
import Controller.BookingCardController as card

app = Flask(__name__, template_folder='View/Template')

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 250,
    "SECRET_KEY": '12345'
}
app.config.from_mapping(config)

cache = Cache(app)


# авторизация для пользователя и администратора
@app.route('/', methods=["POST", "GET"])
def login():
    return authoriz.login(cache)


# получение и отображения данных всех бронирований
@app.route('/all_booking', methods=["POST", "GET"])
def allBooking():
    return admin.allBooking(cache)


# карточка для регистрации бронирования
@app.route('/booking/<guestID>', methods=["POST", "GET"])
def booking(guestID):
    return card.booking(guestID, cache)


if __name__ == '__main__':
    app.run(host='85.143.222.44')
