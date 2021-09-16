#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version: 1.0.0
# File: category_resource.py
# Author:Zhang Zhijun
# Time: 2021-03-13


from flask import Blueprint, render_template, jsonify, url_for, current_app
from werkzeug.utils import redirect

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.forms.category_form import CategoryForm
from app.models.category import Category
from app.utils import query_to_dict
from app.views.admin import bp_admin


@bp_admin.route('/category', methods=['GET', 'POST'])
def create_category():
    category_form = CategoryForm()
    if category_form.validate_on_submit():
        category = get_category_info(category_form)

        if (Category.query.filter_by(slug=category.slug).count() > 0) or (
                Category.query.filter_by(name=category.name).count() > 0):
            return jsonify(code=ResponseCode.CATEGORY_ALREADY_EXIST, message=ResponseMessage.CATEGORY_ALREADY_EXIST)

        db.session.add(category)
        db.session.commit()
        return redirect(url_for('bp_admin.get_categories'))

    return render_template('admin/category/category-new.html', category_form=category_form)


@bp_admin.route('/categories', methods=['GET'])
def get_categories():
    try:
        categories = Category.query.filter().all()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if categories is None:
        return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)
    current_app.logger.debug("categories: %s", categories)

    return categories


@bp_admin.route('/category/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    try:
        category = Category.query.filter_by(id=category_id).first()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if category is None:
        return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)
    data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(category))
    current_app.logger.debug("data: %s", data)
    return jsonify(data)


@bp_admin.route('/category/<int:category_id>', methods=['GET', 'PUT'])
def update_category(category_id):
    category_form = CategoryForm()
    if category_form.validate_on_submit():
        category = get_category_info(category_form)
        try:
            c = Category.query.filter_by(id=category.id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if c is None:
            return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)

    db.session.commit()
    date = dict(code=ResponseCode.UPDATE_CATEGORY_SUCCESS, message=ResponseMessage.UPDATE_CATEGORY_SUCCESS)
    return jsonify(date)


@bp_admin.route('/category/<int:category_id>', methods=['Delete'])
def delete_category(category_id):
    try:
        c = Category.query.filter_by(id=category_id).first()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if c is None:
        return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)

    db.session.delete(c)
    db.session.commit()

    # 未分类文章处理方法
    # TODO

    date = dict(code=ResponseCode.DELETE_CATEGORY_SUCCESS, message=ResponseMessage.DELETE_CATEGORY_SUCCESS)
    return jsonify(date)


def get_category_info(form):
    category = Category()
    category.name = form.name.data
    category.slug = form.slug.data
    category.parentid = form.parentid.data
    category.post = form.post.data
    category.description = form.description.data

    return category
