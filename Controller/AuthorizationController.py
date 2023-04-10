from flask import render_template, request, redirect, url_for


def login(cache):
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        if login == 'admin' and password == 'admin':
            cache.set('login', 'True')
            return redirect(url_for('allBooking'))

    return render_template('AuthorizationTemplate.html')
