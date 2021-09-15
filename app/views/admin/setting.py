# -*- coding: utf-8 -*-
# File: site_resource.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:26
from flask import Blueprint, render_template

from app.models.site import Site
from app.views.admin import bp_admin


@bp_admin.route('/setting', methods=['GET'])
def setting():
    setting = Site.query.all()
    return render_template('admin/site/site.html', posts=posts)
