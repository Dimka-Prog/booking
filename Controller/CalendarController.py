from flask import render_template, request, redirect, url_for
from Model import models

import copy


# функция получения ближайшего свободного времени для резервирования столика
def get_close_date():
    result_close = []
    var_result = {}
    date = models.get_date_time_booking()
    for d in date:
        temp_data = d[0]
        temp_time = d[1][:2]
        data_temp = []
        for j in date:
            if j[0] == temp_data:
                data_temp.append(j[1])
        var_result[temp_data] = data_temp

    setting = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
               '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    for value in var_result.items():
        var_sett = copy.copy(setting)
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


def select_date():
    # подключение к бд
    temp_data = get_close_date()
    data = {'date': temp_data}
    # обработчик нажатия на кнопку
    if request.method == "POST":
        if 'entrance' in request.form:
            date = request.form['val']
            date = date.replace('.', '')
            return redirect(url_for('booking', date=date))
        elif 'all_booking' in request.form:
            return redirect(url_for('all_booking'))
    else:
        cache.clear()
        return render_template('main.html', data=data, settings=cache.get('booking_true'))