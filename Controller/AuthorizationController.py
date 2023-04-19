from flask import render_template, request, redirect, url_for, flash

import Model.UsersModel as users


def login(cache):
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']

        if 'authorization' in request.form:
            if users.getAuthStaff(login, password):
                cache.set('admin', 'True')
                return redirect(url_for('allBooking'))

            if users.getAuthGuest(login, password):
                cache.set('user', 'True')
                return redirect(url_for('booking', guestID=users.getAuthGuest(login, password)[0]))
            else:
                flash(f"Пользователь с логином '{login}' еще не зарегистрирован!", category='error')
        elif 'registration' in request.form:
            if users.getAuthGuest(login, password):
                flash(f"Пользователь с логином '{login}' уже зарегистрирован!", category='error')
            else:
                users.addGuest(login, password)
                flash(f"Пользователь с логином '{login}' зарегистрирован.", category='success')

    return render_template('AuthorizationTemplate.html')
