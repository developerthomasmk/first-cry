from flask import request, redirect, session, url_for, render_template, jsonify, flash
from app.home import bp
from app.models import Products as productdb
from app.models import User as logindb
from app import db

@bp.route('/')
def index():
    if 'user_id' in session: 
        return render_template('home.html')
    else:
        return redirect(url_for('login.login'))

@bp.route('/has_session')
def hasSession():
    if 'user_id' in session:
        user = logindb.query.filter_by(id=session['user_id']).first()
        return jsonify({'has_data': True, 'username': user.firstname, 'userid': user.id})
    else:
        return jsonify({'has_data': False})

@bp.route('/get_products')
def getProducts():
    if 'user_id' in session:
        print(session['user_id'])
        userId = session['user_id']
        products = productdb.query.filter(productdb.user_id != userId, productdb.status == 'active').all()
        if len(products) > 0:
            products_dict = [product.to_dict() for product in products]
            response = jsonify({'status':'success','msg': 'success!!', 'data': products_dict})
            print(response)
            return response
        else:
            return jsonify({'status':'failed', 'msg': 'No data found!'})
        
    else:
        return jsonify({'status':'failed', 'msg': 'user not found'})
    
    
@bp.route('/get_products')
def getAdminProducts():
    products = productdb.query.filter(productdb.status != 'active').all()
    if len(products) > 0:
        products_dict = [product.to_dict() for product in products]
        response = jsonify({'status':'success','msg': 'success!!', 'data': products_dict})
        print(response)
        return response
    else:
        return jsonify({'status':'failed', 'msg': 'No data found!'})
    
@bp.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    print(user_id)
    print(user_id)
    print(user_id)
    print(user_id)
    print(user_id)
    print(user_id)
    print(user_id)
    user = db.session.query(logindb).filter_by(id=user_id).first()
    if user is None:
        return 'User nor found!!!'

    db.session.delete(user)
    db.session.commit()
    session.clear()
    return redirect(url_for('login.login'))
    
@bp.route('/login')
def go_to_login():
    return redirect(url_for('login.login'))

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login.login'))

@bp.route('/history')
def go_to_history():
    return redirect(url_for('history.index'))

@bp.route('/sell_product')
def go_to_sell():
    return redirect(url_for('sell_product.addProduct'))