# -*- coding: utf-8 -*-
# File: index.py
# Author: Zhangzhijun
# Date: 2021/2/12 18:33
from flask import render_template

from app.views.cms import bp_cms


@bp_cms.route('/')
@bp_cms.route('/index')
def cms_index():
    return render_template('cms/index.html')
