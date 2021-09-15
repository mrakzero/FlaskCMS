#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version: 1.0.0
# File: category_resource.py
# Author:Zhang Zhijun
# Time: 2021-03-13


from flask import Blueprint, render_template, jsonify

from app.forms.category_form import CategoryForm
from app.models.category import Category
from app.views.admin import bp_admin


@bp_admin.route('/category', methods=['GET'])
def category():
    category_form = CategoryForm()
    categories = Category.query.all()
    return render_template('admin/category/category.html', category_form=category_form, categories=categories)


@bp_admin.route('/categories', methods=['GET'])
def get_all_category():
    try:
        categories = Category.query.filter().all()
    except:
        return jsonify(code=12, message='query filed.')
    if categories == None:
        return jsonify(code=12, message='result is none.')


@bp_admin.route('/category/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    try:
        category = Category.query.filter(id=category_id).first()
    except:
        return jsonify(code=12, message='query filed.')
    if category == None:
        return jsonify(code=12, message='result is none.')

    return jsonify(code=0, message='query sueess.')


@bp_admin.route('/category/create', methods=['GET,POST'])
def create_category():
    try:
        categories = Category.query.filter().all()
    except:
        return jsonify(code=12, message='query filed.')
    if categories == None:
        return jsonify(code=12, message='result is none.')


@bp_admin.route('/category/<int:category_id>/update', methods=['GET', 'PUT'])
def update_category(category_id):
    try:
        categories = Category.query.filter(id=category_id).first()
    except:
        return jsonify(code=12, message='query filed.')
    if categories == None:
        return jsonify(code=12, message='result is none.')


@bp_admin.route('/category/<int:category_id>/delete', methods=['Delete'])
def delete_category(category_id):
    try:
        categories = Category.query.filter(id=category_id).first()
    except:
        return jsonify(code=12, message='query filed.')
    if categories == None:
        return jsonify(code=12, message='result is none.')


def objects_to_json():
    # todo
    pass
