# -*- coding: utf-8 -*-
# File: dashboard.py
# Author: Zhangzhijun
# Date: 2021/2/12 18:33
from flask import Blueprint, render_template

bp_cms_index = Blueprint('cm_index', __name__,  template_folder='../templates/cms', static_folder='../static')


@bp_cms_index.route('/')
@bp_cms_index.route('/index')
def cm_index():
    return render_template('cms/index.html')