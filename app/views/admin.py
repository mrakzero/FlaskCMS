from flask import Blueprint, render_template

bp_admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='../templates')


@bp_admin.route('/')
def admin():
    return render_template('index.html')
