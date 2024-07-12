from flask import request, render_template, redirect, url_for, flash
from app.login import bp
from app.models import User as logindb

@bp.route('/')
def index():
    return redirect(url_for('login.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        singleUser = logindb.query.filter_by(username=user_name).first()
        print(singleUser)
        if singleUser == None:
            flash("No username assosiated found!!", "danger")
        else:          
            if user_name == "" or password == "":
                flash("Please fill in all fields.")
            elif password == singleUser.password:
                return redirect(url_for('home'))
            else:
                flash("Invalid username or password.", "danger")

    return render_template('login.html')

@bp.route('/register')
def go_to_register():
    return render_template('register.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        conf_password = request.form['confirm_password']
        if password == conf_password:
            record = logindb()


        singleUser = logindb.query.filter_by(username=user_name).first()
        print(singleUser)
        if singleUser == None:
            flash("No username assosiated found!!", "danger")
        else:          
            if user_name == "" or password == "":
                flash("Please fill in all fields.")
            elif password == singleUser.password:
                return redirect(url_for('home'))
            else:
                flash("Invalid username or password.", "danger")

    return render_template('login.html')