#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version:
# author:Zhang Zhijun
# time: 2021-03-13
# file: category.py
# function:
# modify:
from flask import Blueprint

bp_admin_category = Blueprint('admin_category',__name__, url_prefix='/admin', template_folder='../template',static_folder='../static')

@bp_admin_category.route('/category',methods=['GET'])
def category():
    category_form = CategoryForm()