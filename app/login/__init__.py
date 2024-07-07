from flask import Blueprint

bp = Blueprint('login', _name_, template_folder="templates")

from app.login import views