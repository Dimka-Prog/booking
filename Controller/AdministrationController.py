from flask import render_template, redirect, url_for

import Model.BookingModel as booking
import Database.connectDB as db


def all_booking(cache):
    connectDB = db.getConnection()

    if cache.get('login') is None:
        return redirect(url_for('login'))
    else:
        return render_template('all_booking.html', all_booking=booking.get_all_booking(connectDB))
