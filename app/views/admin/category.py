#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version:
# author:Zhang Zhijun
# time: 2021-03-13
# file: category.py
# function:
# modify:
from flask import Blueprint, render_template, jsonify

from app.forms.category import CategoryForm
from app.models.category import Category

bp_admin_category = Blueprint('admin_category', __name__, url_prefix='/admin', template_folder='../template',
                              static_folder='../static')


@bp_admin_category.route('/category', methods=['GET'])
def category():
    category_form = CategoryForm()
    categories = Category.query.all()
    return render_template('admin/category/category.html', category_form=category_form, categories=categories)

@bp_admin_category.route('/category/list', methods=['GET'])
def get_all_category():
    try:
        categories = Category.query.filter().all()
    except:
        return jsonify(code=12,message='query filed.')
    if categories == None:
        return jsonify(code=12,message='result is none.')
    category_form = CategoryForm()
    categories = Category.query.all()
    return render_template('admin/category/category.html', category_form=category_form, categories=categories)