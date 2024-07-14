from flask import Blueprint

bp = Blueprint('history', __name__, static_folder='static', template_folder="template")

from app.history import routes