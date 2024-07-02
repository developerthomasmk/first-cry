from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import User

app = Flask(__name__)

app.config.from_object('config.Config')

db = SQLAlchemy(app)
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == "" or password == "":
            flash("Please fill in all fields.")
        elif username == "admin" and password == "password":
            flash("Login successful!", "success")
        else:
            flash("Invalid username or password.", "danger")

    return render_template('./login.html')

if __name__ == '__main__':
    app.run(debug=True)
 