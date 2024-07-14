from flask import Blueprint

bp = Blueprint('admin', __name__, static_folder='static', template_folder='template')

from app.admin import routes