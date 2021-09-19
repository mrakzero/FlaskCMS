# -*- coding: utf-8 -*-
# File: page_resource.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:22
from flask import render_template, redirect, flash, url_for, jsonify

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.forms.page_form import PageForm
from app.models.category import Category
from app.models.page import Page
from app.models.user import User
from app.views.admin import bp_admin
from app.views.include.page_resource import PageResource


@bp_admin.route('/page', methods=['GET', 'Post'])
def create_page():
    page_form = PageForm()
    if page_form.validate_on_submit():
        Page = get_page_info(page_form)
        db.session.add(Page)
        db.session.commit()
        flash('Page created.', 'success')
        return redirect(url_for('admin.Page'))
    return render_template('admin/Page/Page-new.html', page_form=page_form)


@bp_admin.route('/pages', methods=['GET'])
def get_pages():
    data = PageResource.query_pages()
    return render_template('admin/page/page.html', data=data)


@bp_admin.route('/page/<int:page_id>', methods=['GET'])
def get_page_by_id(page_id):
    data = PageResource.query_page_by_id()
    return data


@bp_admin.route('/page/<string:page_title>', methods=['GET'])
def get_page_by_title(page_title):
    data = PageResource.query_page_by_title()
    return data


@bp_admin.route('/page/<string:page_author>', methods=['GET'])
def get_page_by_author(page_author):
    data = PageResource.query_page_by_title()
    return data


@bp_admin.route('/page/<int:page_id>', methods=['GET', 'PUT'])
def update_page(page_id):
    page_form = PageForm()
    try:
        page = Page.query.filter_by(id=page_id).first()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if page is None:
        return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)

    if page_form.validate_on_submit():
        page = get_page_info(page_form)
        db.session.add(page)
        db.session.commit()
        flash('Page updated.', 'success')
        return redirect(url_for('admin.Page'))
    page_form.title.data = Page.title
    page_form.slug.data = Page.slug
    page_form.excerpt.data = Page.excerpt
    page_form.content.data = Page.content
    page_form.categoryid.data = Page.categoryid
    page_form.status.data = Page.status
    return render_template('admin/Page/Page-edit.html', page_form=page_form)


@bp_admin.route('/page/<int:page_id>', methods=['DELETE'])
def delete_page(page_id):
    try:
        page = Page.query.filter_by(id=page_id).first()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if page is None:
        return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)
    db.session.delete(page)
    db.session.commit()
    return redirect(url_for('bp_admin.get_pages'))


# 从表单中获取Page信息
def get_page_info(form):
    page = Page()
    page.title = form.title.data
    page.slug = form.slug.data
    page.authorid = User.query.get(form.authorid.data)
    page.content = form.content.data
    page.status = form.title.data

    return page
