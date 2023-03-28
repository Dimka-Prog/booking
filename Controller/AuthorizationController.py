from flask import render_template, request, redirect, url_for


def login(cache):
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            cache.set('login', 'True')
            return redirect(url_for('all_booking'))
    return render_template('login.html')
