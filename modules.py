from flask import Flask, render_template, request, redirect, url_for
	
app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template('Modules.html')

@app.route('/Module1')
def about():
    return render_template('Module1.html')


@app.route('/Module2')
def rankings():
    return render_template('Module2.html')

@app.route('/Module3')
def rankings():
    return render_template('Module3.html')