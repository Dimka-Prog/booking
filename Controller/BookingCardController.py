from flask import render_template, request, redirect
from Model import models


def booking(date):
    var_date = str(date[-4:]) + "-" + str(date[2:4]) + "-" + str(date[0:2])
    setting = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
               '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    block_time = models.get_block_time(var_date)
    for i in range(len(block_time)):
        if block_time[i][0] in setting:
            index = setting.index(block_time[i][0])

    if request.method == "POST":
        try:

            guest_id = models.insert_guest(request.form['fio'], request.form['number_phone'])
            place_id = models.get_place(request.form['system_kat'], request.form['dva'])
            desk_id = models.select_desk(request.form['desc_amount'], place_id)
            print(desk_id)
            var_date = str(date[-4:]) + "-" + str(date[2:4]) + "-" + str(date[0:2])
            time = request.form['time']
            amount = request.form['desc_amount']
            models.insert_booking(desk_id, guest_id, var_date, time, amount)
            cache.set('booking_true', 'True')
            return redirect('/')
        except TypeError:
            print('Ошибка типа данных')
    else:
        return render_template('librarian.html', time=setting)