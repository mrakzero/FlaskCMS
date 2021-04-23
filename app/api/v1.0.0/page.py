# -*- coding: utf-8 -*-
# File: page.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:22
from flask import Blueprint, render_template, redirect, flash, url_for

from app import db
from app.forms.page import PageForm
from app.models.category import Category
from app.models.page import Page
from app.models.user import User

bp_admin_page = Blueprint('admin_page', __name__, url_prefix='/admin', template_folder='../templates/admin',
                          static_folder='../static')


@bp_admin_page.route('/age', methods=['GET'])
def page_query():
    pages = Page.query.all()
    return render_template('admin/Page/Page.html', pages=pages)


@bp_admin_page.route('/Page/new', methods=['GET', 'Page'])
def create_Page():
    page_form = PageForm()
    if page_form.validate_on_submit():
        Page = get_page_info(page_form)
        db.session.add(Page)
        db.session.commit()
        flash('Page created.', 'success')
        return redirect(url_for('admin.Page'))
    return render_template('admin/Page/Page-new.html', page_form=page_form)


@bp_admin_page.route('/Page/<int:page_id>/update', methods=['GET', 'Page'])
def update_Page(page_id):
    page_form = PageForm()
    page = Page.query.get_or_404(page_id)
    if page_form.validate_on_submit():
        page = get_page_info(page_form)
        db.session.add(Page)
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


@bp_admin_page.route('/Page/<int:page_id>/delete', methods=['Page'])
def delete_Page(page_id):
    page = Page.query.get_or_404(page_id)
    db.session.delete(Page)
    db.session.commit()
    flash('Page deleted.', 'success')
    return redirect(url_for('admin.Page'))


# 从表单中获取Page信息
def get_page_info(form):
    title = form.title.data
    slug = form.slug.data
    authorid = User.query.get(form.authorid.data)
    content = form.content.data
    status = form.title.data

    page = Page(
        title=title,
        slug=slug,
        authorid=authorid,
        content=content,
        status=status,
    )

    return Page