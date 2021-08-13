from flask import Blueprint, render_template

bp_admin_index = Blueprint('admin_index', __name__, template_folder='../templates/admin/',
                           static_folder='../static')


@bp_admin_index.route('/')
def admin_index():
    return render_template('admin/index.html')
