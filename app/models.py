from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    address_line1 = db.Column(db.String(120), nullable=False)
    address_line2 = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False, default=False)
    # products = db.relationship("Product", backref="user")

    def to_dict(self):
        return {
            'userid': self.userid,
            'username': self.username,
            'password': self.password,
            'mobile': self.mobile,
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'address_line1': self.address_line1,
            'address_line2': self.address_line2,
            'is_admin': self.is_admin
        }
    
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoryname = db.Column(db.String(50), unique=True, nullable=False)

    def to_dict(self):
        return{
            'cat_id': self.id,
            'category_name': self.categoryname
        }
    
class Products(db.Model):
    __tablename__ = "products"
    productId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productname = db.Column(db.String(80), nullable=False)
    year_of_purchase = db.Column(db.String(10), nullable=True)
    price = db.Column(db.String(10), nullable=True)
    desc = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('products', lazy=True))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('products', lazy=True))

    def to_dict(self):
        return{
            'productId': self.productId,
            'productname': self.productname,
            'year_of_purchase': self.year_of_purchase,
            'price': self.price,
            'desc': self.desc,
            'status': self.status,
            'image': self.image,
            'user_id': self.user_id,
            'category_id': self.category_id
        }
