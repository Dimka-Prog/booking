from flask import render_template, request, redirect, url_for

import Model.BookingModel as bookingModel
import Model.TablesModel as tables
import Model.UsersModel as users


def booking(date, cache):
    allTime = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
               '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']

    if request.method == "POST":
        users.addGuest(request.form['fio'], request.form['phoneNumber'])
        guestID = users.getGuest(request.form['fio'], request.form['phoneNumber'])
        placeID = tables.getTableLocation(int(request.form['floor']), request.form['window'])
        tableID = tables.getFreeTable(int(request.form['countPlaces']), placeID)

        bookingDate = str(date[-4:]) + "-" + str(date[2:4]) + "-" + str(date[0:2])
        bookingTime = request.form['bookingTime']
        countPlaces = int(request.form['countPlaces'])

        bookingModel.addBooking(tableID, guestID, bookingDate, bookingTime, countPlaces)
        cache.set('booking_true', 'True')
        return redirect(url_for('selectDate'))
    else:
        return render_template(
            'BookingCardTemplate.html',
            allTime=allTime,
            countPlaces=tables.getCountPlaces()
        )
