from flask import Flask, render_template, request, redirect, url_for, flash
from app import app
from app.forms import LoginForm

@app.route("/")
def homePage():
    return render_template('HomePage.html')

@app.route('/about')
def about():
    return render_template('About.html')


@app.route('/rankings')
def rankings():
    return render_template('Rankings.html')	
@app.route('/login/module1')
def mod1():
    return render_template('Module1.html')

@app.route('/login/module2')
def mod2():
    return render_template('Module2.html')

@app.route('/login/module3')
def mod3():
    return render_template('Module3.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('homePage'))
    return render_template('login.html', title='Sign In', form=form)
# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     error = ''
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid user'
#         else:
#             return redirect(url_for('mod1'))
#     return render_template('Login.html', error=error)

@app.route('/modules')
def modules():
    return render_template('Modules.html')