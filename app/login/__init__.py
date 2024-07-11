from flask import Blueprint

bp = Blueprint('login', __name__, static_folder='static', template_folder="templates")

from app.login import routs