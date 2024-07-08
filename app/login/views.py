from flask import request, render_template, redirect, url_for, flash
from app.login import bp
from app.login.models import User as logindb

@bp.route('/')
def index():
    return redirect(url_for('login.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        singleUser = logindb.query.filter_by(username=user_name).first()
        print(singleUser.username)

        if user_name == "" or password == "":
            flash("Please fill in all fields.")
        elif password == singleUser.password:
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password.", "danger")

    return render_template('login.html')