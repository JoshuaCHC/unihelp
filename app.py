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

@app.route('/login')
def login():
    return render_template('Login.html')

if( __name__ == '__main__'):
    app.run()

