# -*- coding: utf-8 -*-
# File: index.py
# Author: Zhangzhijun
# Date: 2021/2/12 18:33
from flask import Blueprint, render_template

bp_cms_index = Blueprint('cms_index', __name__,  template_folder='../templates/cms', static_folder='../static')


@bp_cms_index.route('/')
@bp_cms_index.route('/index')
def cms_index():
    return render_template('cms/index.html')