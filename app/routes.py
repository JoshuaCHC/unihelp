from flask import Flask, render_template, request, redirect, url_for, flash
from app import app,db
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from flask_login import login_required, logout_user, current_user, login_user
from app.models import User
@app.route("/")
def homePage():
    return render_template('HomePage.html')

@app.route('/about')
def about():
    return render_template('About.html')


@app.route('/rankings')
def rankings():
    return render_template('Rankings.html')	
@login_required
@app.route('/login/module1')
def mod1():
    return render_template('Module1.html')
@login_required
@app.route('/login/module2')
def mod2():
    return render_template('Module2.html')
@login_required
@app.route('/login/module3')
def mod3():
    return render_template('Module3.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = []
    if current_user.is_authenticated:
        return redirect(url_for('mod1'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        bool = True
        if user is None: 
            print('No user')
            bool = False
            error.append('Invalid username')
            return render_template('login.html', form=form, errors= error)

        if not user.check_password(form.password.data):
            print(form.password.data)
            error.append('Invalid password')
            return render_template('login.html', form=form, errors= error)

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '' or next_page == '/':
            next_page = url_for('homePage')
        return redirect(url_for('mod1'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homePage'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = []
    err = False
    print('trying reg')
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        print('Form is good?')
        if(User.query.filter_by(username=form.username.data).first() != None):
            #Could try use regex to suggest new ones.
            error.append('Username is taken, please try another.')
            err = True
        if(User.query.filter_by(email=form.email.data).first() != None):
            #Suggest forgot password?
            error.append('There is already an account with that email address.')
            err = True
        if(err):
            return render_template('registerform.html', title='Register', form=form, errors = error)

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('homePage'))
    return render_template('registerform.html', title='Register', form=form)

@login_required
@app.route('/modules')
def modules():
    return render_template('Modules.html')