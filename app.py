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
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if not username or not password or not confirm_password:
            flash("Please fill in all fields.", "warning")
        elif password != confirm_password:
            flash("Passwords do not match.", "danger")
        else:
            # Check if the user already exists
            user = User.query.filter_by(username=username).first()
            if user:
                flash("Username already exists.", "danger")
            else:
                new_user = User(username=username, password=password)
                db.session.add(new_user)
                db.session.commit()
                flash("Registration successful! You can now log in.", "success")
                return redirect(url_for('login'))
                
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
 