from flask import Blueprint

bp = Blueprint('home', __name__, static_folder='static', template_folder="template")

from app.home import routes