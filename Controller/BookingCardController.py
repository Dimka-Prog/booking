from flask import render_template, request, redirect, url_for

import Database.connectDB as db
import Model.BookingModel as bookingModel
import Model.TablesModel as tables
import Model.UsersModel as users


def booking(date, cache):
    connectDB = db.getConnection()

    var_date = str(date[-4:]) + "-" + str(date[2:4]) + "-" + str(date[0:2])
    setting = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
               '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    block_time = bookingModel.get_block_time(connectDB, var_date)
    for i in range(len(block_time)):
        if block_time[i][0] in setting:
            index = setting.index(block_time[i][0])

    if request.method == "POST":
        guest_id = users.insert_guest(connectDB, request.form['fio'], request.form['number_phone'])
        place_id = tables.get_place(connectDB, request.form['system_kat'], request.form['dva'])
        desk_id = tables.select_desk(connectDB, int(request.form['desc_amount']), place_id)
        var_date = str(date[-4:]) + "-" + str(date[2:4]) + "-" + str(date[0:2])
        time = request.form['time']
        amount = int(request.form['desc_amount'])
        bookingModel.insert_booking(connectDB, desk_id, guest_id, var_date, time, amount)
        cache.set('booking_true', 'True')
        return redirect(url_for('select_date'))
    else:
        return render_template('BookingCardTemplate.html', time=setting)
