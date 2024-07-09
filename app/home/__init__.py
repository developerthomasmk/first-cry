from flask import Blueprint

bp = Blueprint('home', __name__, template_folder="templates")

from app.home import routes