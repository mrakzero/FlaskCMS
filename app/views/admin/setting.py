# -*- coding: utf-8 -*-
# File: site.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:26
from flask import Blueprint, render_template

from app.models.site import Site

bp_admin_setting = Blueprint('admin_setting', __name__, url_prefix='/admin', template_folder='../templates/admin',
                             static_folder='../static')


@bp_admin_setting.route('/setting', methods=['GET'])
def setting():
    setting = Site.query.all()
    return render_template('admin/site/site.html', posts=posts)
