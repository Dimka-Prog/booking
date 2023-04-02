from flask import render_template, redirect, url_for

import Model.BookingModel as booking


def all_booking(cache):
    if cache.get('login') is None:
        return redirect(url_for('login'))
    else:
        return render_template('AdministrationTemplate.html', all_booking=booking.get_all_booking())
