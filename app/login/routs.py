from flask import request, render_template, session, redirect, url_for, flash, jsonify
from app.login import bp
from app.models import User as logindb
from app import db

# @bp.route('/')
# def index():
#     return redirect(url_for('login'))

@bp.route('/', methods=['GET', 'POST'])
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
                session['user_id'] = singleUser.id
                return redirect(url_for('home'))
            else:
                flash("Invalid username or password.", "danger")

    return render_template('login.html')

# @bp.route('/register')
# def go_to_register():
#     return redirect(url_for('login.register'))

@bp.route('/api/add_user', methods=['POST'])
def addUser():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        mobile = request.form['mobile']
        address_line1 = request.form['address_line1']
        address_line2 = request.form['address_line2']
        user_name = request.form['username']
        password = request.form['password']
        conf_password = request.form['confirm_password']
        if password == conf_password:
            record = logindb(username=user_name, 
                             password=password, 
                             mobile=mobile, 
                             email=email, 
                             firstname=firstname, 
                             lastname=lastname, 
                             address_line1=address_line1, 
                             address_line2=address_line2, 
                             is_admin=False
                             )
            
            try:
                db.session.add(record)
                db.session.commit()
                return jsonify({'success': True, 'username': user_name}), 200
            except Exception as e:
                db.session.rollback()
                return jsonify({'success': False, 'error': str(e)}), 500
            finally:
                db.session.close()


@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/home')
def go_to_home():
    return redirect(url_for('home.index'))