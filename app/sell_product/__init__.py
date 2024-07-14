from flask import Blueprint

bp = Blueprint('sell_product', __name__, static_folder='static', template_folder="template")

from app.sell_product import views