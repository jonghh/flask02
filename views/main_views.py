from flask import Blueprint, render_template

bp = Blueprint('main_views', __name__, url_prefix='/')  # 파일 이름과 동일하게 main_views

@bp.route('/')
def ask():
    return render_template('index.html')
