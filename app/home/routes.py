from flask import request, redirect, url_for, render_template
from app.home import bp

@bp.route('/')
def index():
    return render_template(url_for('home.html'))