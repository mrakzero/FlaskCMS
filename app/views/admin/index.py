from flask import Blueprint, render_template

from app.views.admin import bp_admin


@bp_admin.route('/')
def admin_index():
    return render_template('admin/index.html')
