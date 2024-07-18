from flask import render_template, redirect, jsonify
from app.admin import bp
from app.models import Products as productdb
from app import db

@bp.route('/')
def adminHome():
    return render_template('admin_home.html')

@bp.route('/api/getProducts')
def getAllProducts():
    products = productdb.query.filter_by(status='inProgress').all()
    if len(products) > 0:
        products_dict = [product.to_dict() for product in products]
        response = jsonify({'status':'success','msg': 'success!!', 'data': products_dict})
        print(response)
        return response
    else:
        return jsonify({'status':'failed', 'msg': 'No data found!'})
    
@bp.route('/api/changeStatus/<int:product_id>/<string:status>/<int:price>', methods = ['GET', 'PUT', 'POST'])
def acceptProduct(product_id, status, price):
    product = productdb.query.get(product_id)
    if product is None:
        return jsonify({'status':'failed', 'msg': 'No data found!'})
    else:
        product.status = status
        product.price = str(price)
        db.session.commit()
        
        response = jsonify({'status':'success','msg': 'success!!'})
        print(response)
        return response
         
    
@bp.route('/api/changeStatus/<int:product_id>/<string:status>', methods = ['GET', 'PUT', 'POST'])
def rejectProduct(product_id, status, price):
    product = productdb.query.get(product_id)
    product.status = status
    
@bp.route('/home')
def go_to_home():
    pass