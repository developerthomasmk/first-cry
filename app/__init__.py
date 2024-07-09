from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from app.login import bp as login_bp
        from app.home import bp as home_bp

        app.register_blueprint(login_bp, url_prefix='/login')
        app.register_blueprint(home_bp)

        db.create_all()

    return app
