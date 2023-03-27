from flask import render_template, redirect, url_for
from Model import models


def all_booking():
    if cache.get('login') is None:
        return redirect(url_for('login'))
    else:
        return render_template('all_booking.html', all_booking=models.get_all_booking())