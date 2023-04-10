from flask import render_template, redirect, url_for

import Model.BookingModel as booking


def allBooking(cache):
    if cache.get('login') is None:
        return redirect(url_for('login'))
    else:
        return render_template('AdministrationTemplate.html', allBooking=booking.getAllBooking())
