from flask import render_template, redirect, jsonify
from app.admin import bp
from app.models import Products as productdb

@bp.route('/')
def adminHome():
    return render_template('admin_home.html')

@bp.route('/api/getProducts')
def getAllProducts():
    products = productdb.query.all()
    if len(products) > 0:
        products_dict = [product.to_dict() for product in products]
        response = jsonify({'status':'success','msg': 'success!!', 'data': products_dict})
        print(response)
        return response
    else:
        return jsonify({'status':'failed', 'msg': 'No data found!'})