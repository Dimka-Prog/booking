from flask import render_template, request, redirect, url_for
from datetime import datetime
from pytz import timezone
from dateutil.parser import parse

import copy
import Model.BookingModel as booking


# функция получения ближайшего свободного времени для резервирования столика
def getFreeDate():
    result_close = []
    var_result = {}
    date = booking.getDateTime()
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


def selectDate(cache):
    temp_data = getFreeDate()
    data = {'date': temp_data}

    if request.method == "POST":
        if 'selectDateButton' in request.form:
            date = parse(request.form['date']).date()
            return redirect(url_for('booking', date=date))
        elif 'allBookingButton' in request.form:
            return redirect(url_for('allBooking'))
    else:
        cache.clear()
        return render_template(
            'CalendarTemplate.html',
            data=data,
            currentDate=datetime.now(timezone('Asia/Vladivostok')).strftime('%d.%m.%Y'),
            settings=cache.get('booking_true')
        )
