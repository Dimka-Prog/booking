from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
from pytz import timezone
from dateutil.parser import parse

import copy
import Model.BookingModel as bookingModel
import Model.TablesModel as tables
import Model.UsersModel as users


# функция получения ближайшего свободного времени для резервирования столика
def getFreeDate():
    result_close = []
    var_result = {}
    date = bookingModel.getDateTime()
    for d in date:
        temp_data = d[0]
        # temp_time = d[1][:2]
        data_temp = []
        for j in date:
            if j[0] == temp_data:
                data_temp.append(j[1])
        var_result[temp_data] = data_temp

    allTime = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
               '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']

    for value in var_result.items():
        var_sett = copy.copy(allTime)
        for i in range(len(value[1])):
            if value[1][i] in var_sett:
                index = var_sett.index(value[1][i])
                if abs(index - len(value[1])) < 5:
                    del var_sett[index:index + 6]
                else:
                    del var_sett[index:]
        flag = False
        k = 0
        for i in range(len(var_sett) - 1):
            if abs(int(var_sett[i][:2]) - int(var_sett[i + 1][:2])) == 1:
                k += 1
            else:
                k = 0
        if k >= 5:
            flag = True
        if not flag:
            result_close.append(value[0])
    return result_close


def booking():
    allTime = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
               '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']

    temp_data = getFreeDate()
    data = {'date': temp_data}

    if request.method == "POST":
        bookingDate = parse(request.form['date']).date()
        beginBookingTime = request.form['beginBookingTime']
        endBookingTime = request.form['endBookingTime']
        countPlaces = int(request.form['countPlaces'])

        users.addGuest(request.form['fio'], request.form['phoneNumber'])
        guestID = users.getGuest(request.form['fio'], request.form['phoneNumber'])
        placeID = tables.getTableLocation(int(request.form['floor']), request.form['window'])
        tableID = tables.getFreeTable(
            int(request.form['countPlaces']),
            placeID,
            bookingDate,
            beginBookingTime,
            endBookingTime
        )

        if tableID is None:
            if request.form['window'] == 'yes':
                flash(f'''
                    На время с {beginBookingTime} до {endBookingTime} нет свободного столика на {countPlaces} человек(а) у окна! 
                    Пожалуйста, выберите другое время или расположение столика.
                    ''', category='error')
            elif request.form['window'] == 'no':
                flash(f'''
                    На время с {beginBookingTime} до {endBookingTime} нет свободного столика на {countPlaces} человек(а) не у окна!
                    Пожалуйста, выберите другое время или расположение столика.
                    ''', category='error')
        else:
            bookingModel.addBooking(tableID, guestID, bookingDate, beginBookingTime, endBookingTime, countPlaces)
            flash(f'''Бронь на {bookingDate} с {beginBookingTime} до {endBookingTime} успешно создана!
                      Ваш столик под номером {bookingModel.getBookingTable(tableID)}.''', category='success')

    return render_template(
        'BookingCardTemplate.html',
        data=data,
        currentDate=datetime.now(timezone('Asia/Vladivostok')).strftime('%d.%m.%Y'),
        allTime=allTime,
        countPlaces=tables.getCountPlaces()
    )
