import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config['UPLOAD_FOLDER'] = 'app/uploads/images'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    with app.app_context():
        from app.login import bp as login_bp
        from app.home import bp as home_bp
        from app.history import bp as history_bp
        # from app.sell_product import bp as sell_bp

        app.register_blueprint(login_bp, url_prefix='/login')
        app.register_blueprint(home_bp, url_prefix='/home')
        app.register_blueprint(history_bp, url_prefix='/history')
        # app.register_blueprint(sell_bp, url_prefix='/sell_product')

        db.create_all()
        
        @app.route('/uploads/images/<path:filename>')
        def download_file(filename):
            return send_from_directory('uploads/images', filename)

    return app
