from flask import Flask, render_template, request, redirect, url_for
	
app = Flask(__name__)

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






@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid user'
        else:
            return redirect(url_for('mod1'))
    return render_template('Login.html', error=error)

if( __name__ == '__main__'):
    app.static_folder = 'static'
    app.run(debug = 1)

