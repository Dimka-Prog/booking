from flask import render_template, redirect, request, url_for

import Model.BookingModel as booking


def allBooking(cache):
    if cache.get('login') is None:
        return redirect(url_for('login'))
    else:
        clickButtonEdit = None
        clickButtonDelete = None

        if request.method == "POST":
            if 'buttonEdit' in request.form:
                clickButtonEdit = request.form['buttonEdit']
            elif 'buttonDelete' in request.form:
                clickButtonDelete = request.form['buttonDelete']
                bookingDate = str(request.form['bookingDate'])
                beginTime = str(request.form['beginTime'])
                tableNumber = int(request.form['tableNumber'])

                booking.removeBooking(bookingDate, beginTime, tableNumber)

        return render_template(
            'AdministrationTemplate.html',
            allBooking=booking.getAllBooking(),
            clickButtonEdit=clickButtonEdit,
            clickButtonDelete=clickButtonDelete,
            bookingDates=booking.getDates(),
            bookingBeginTime=booking.getBeginTimes(),
            bookingTableNumbers=booking.getTableNumbers()
        )
