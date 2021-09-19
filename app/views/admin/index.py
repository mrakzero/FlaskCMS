from flask import render_template

from app.views.admin import bp_admin


@bp_admin.route('/')
def index():
    return render_template('admin/index.html')


@bp_admin.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')
