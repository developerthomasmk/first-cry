from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    mobile = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(20), unique=True, nullable=False)
    lastname = db.Column(db.String(50), unique=True, nullable=False)
    address_line1 = db.Column(db.String(120), unique=True, nullable=False)
    address_line2 = db.Column(db.String(120), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean(), unique=True, nullable=False)
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
    
class Products(db.Model):
    __tablename__ = "products"
    productId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productname = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(10), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('products', lazy=True))