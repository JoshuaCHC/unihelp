from flask import Flask, render_template, request, redirect, url_for
from app import app

@app.route("/")
def homePage():
    return render_template('HomePage.html')

@app.route('/about')
def about():
    return render_template('About.html')


@app.route('/rankings')
def rankings():
    return render_template('Rankings.html')	

@app.route('/login/module1/content')
def mod1():
    return render_template('Module1.html')

@app.route('/login/module2/content')
def mod2():
    return render_template('Module2.html')

@app.route('/login/module3/content')
def mod3():
    return render_template('Module3.html')

@app.route('/login/module1/quiz')
def quiz1():
    return render_template('Module1_quiz.html')

@app.route('/login/module2/quiz')
def quiz2():
    return render_template('Module2_quiz.html')

@app.route('/login/module3/quiz')
def quiz3():
    return render_template('Module3_quiz.html')

@app.route('/login/modules')
def home_mod():
    return render_template('home_mod.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid user'
        else:
            return redirect(url_for('home_mod'))
    return render_template('Login.html', error=error)

@app.route('/modules')
def modules():
    return render_template('Modules.html')