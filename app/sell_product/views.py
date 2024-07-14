from flask import request, render_template, session, redirect, url_for, flash, jsonify, current_app
from app.sell_product import bp
from app.models import Products as productDb
from werkzeug.utils import secure_filename
import os
from app.models import Products as productdb
from app import db

# app = create_app()
@bp.route('/', methods=['GET', 'POST'])
def addProduct():
    if request.method == 'POST':
        if 'user_id' in session:
            product_name = request.form['product-name']
            category = request.form['category']
            yop = request.form['year-of-purchase']
            price = request.form['price']
            desc = request.form['description']
            product_images = request.files.getlist('product-images')
            fileName = ''
            for image in product_images:
                if image.filename != '':
                    filename = secure_filename(image.filename)
                    fileName = filename
                    image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                    
            product = productdb(productname=product_name,
                                year_of_purchase=yop,
                                price=price,
                                desc=desc,
                                status='inProgress',
                                image=fileName,
                                user_id=session['user_id'],
                                category_id='1'
                                )
                
            try:
                db.session.add(product)
                db.session.commit()
                flash('Product added successfully!', 'success')
                # return redirect(url_for('sell_product.go_to_home'))
            except Exception as e:
                db.session.rollback()
                flash('Product not added!', 'failed')
            finally:
                db.session.close()
        else:
            print('User not logged in....')
    else:
        flash('Please fill all the required fields and add at least one image.', 'error')

    return render_template('add_request.html')

@bp.route('/home')
def go_to_home():
    return redirect(url_for('home.index'))