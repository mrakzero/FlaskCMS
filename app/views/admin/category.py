#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version: 1.0.0
# File: category_resource.py
# Author:Zhang Zhijun
# Time: 2021-03-13
import json

from flask import Blueprint, render_template, jsonify, url_for, current_app
from werkzeug.utils import redirect

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.forms.category_form import CategoryForm
from app.models.category import Category
from app.utils import query_to_dict
from app.views.admin import bp_admin
from app.views.common.category_resource import CategoryResource


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
    # data = CategoryResource.query_categories()

    return render_template('admin/category/category.html')


@bp_admin.route('/category/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    data = CategoryResource.query_category_by_id(category_id)
    return data


@bp_admin.route('/category/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category_form = CategoryForm()
    try:
        category = Category.query.get_or_404(category_id)
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if category is None:
        return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)

    if category_form.validate_on_submit():
        category = get_category_info(category_form)
        db.session.add(category)
        db.session.commit(category)
        return redirect(url_for('bp_admin.get_categories'))

    category_form.title.data = category.title
    category_form.slug.data = category.slug
    category_form.excerpt.data = category.excerpt
    category_form.content.data = category.content
    category_form.categoryid.data = category.categoryid
    category_form.status.data = category.status
    return render_template('admin/category/category-edit.html', category_form=category_form)


@bp_admin.route('/category/<int:category_id>', methods=['Delete'])
def delete_category(category_id):
    try:
        category = Category.query.filter_by(id=category_id).first()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if category is None:
        return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)

    count = Category.query.filter_by(id=category_id).count()
    if (count == 0):
        db.session.delete(category)
        db.session.commit()
    else:
        return jsonify(code=ResponseCode.CATEGORY_ASSOCIATE_WITH_POST,
                       message=ResponseMessage.CATEGORY_ASSOCIATE_WITH_POST)

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
