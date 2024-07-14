from flask import request, render_template, session, redirect, url_for, flash, jsonify
from app.history import bp
from app.models import Products as productdb
from app import db

@bp.route('/')
def index():
    return render_template('history.html')

@bp.route('/get_history')
def getHistory():
    if 'user_id' in session:
        print('UserId:- ',session['user_id'])
        userId = session['user_id']
        products = productdb.query.filter(productdb.user_id == userId).all()
        if len(products) > 0:
            products_dict = [product.to_dict() for product in products]
            response = jsonify({'status':'success','msg': 'success!!', 'data': products_dict})
            print(response)
            return response
        else:
            return jsonify({'status':'failed', 'msg': 'No data found!'})
    else:
        return jsonify({'status':'failed', 'msg': 'user not found'})