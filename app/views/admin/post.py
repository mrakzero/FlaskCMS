# -*- coding: utf-8 -*-
# File: post.py
# Author: Zhangzhijun
# Date: 2021/2/12 21:22
from flask import Blueprint, request, flash, redirect, url_for, render_template

from app import db
from app.forms.post import PostForm
from app.models.post import Category, Post
from app.models.user import User

bp_admin_post = Blueprint('admin_post', __name__, url_prefix='/admin', template_folder='../templates/admin',
                          static_folder='../static')


@bp_admin_post.route('/post', methods=['GET'])
def post_query():
    pass


@bp_admin_post.route('/post/new', methods=['GET', 'POST'])
def post_new():
    form = PostForm()
    if form.validate_on_submit():
        post = get_post_info(form)
        db.session.add(post)
        db.session.commit()
        flash('Post created.', 'success')
        return redirect(url_for('admin.post'))
    return render_template('admin/post_new.html', form=form)


@bp_admin_post.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
def post_update(post_id):
    form = PostForm()
    post = Post.query.get_or_404(post_id)
    if form.validate_on_submit():
        post = get_post_info(form)
        db.session.add(post)
        db.session.commit()
        flash('Post updated.', 'success')
        return redirect(url_for('admin.post'))
    form.title.data = post.title
    form.content.data = post.content
    form.categoryid.data = post.categoryid
    return render_template('admin/post_edit.html', form=form)


@bp_admin_post.route('/post/<int:post_id>/delete', methods=['POST'])
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted.', 'success')
    return redirect(url_for('admin.post'))


# 从表单中获取post信息
def get_post_info(form):
    title = form.title.data
    slug = form.slug.data
    authorid = User.query.get(form.authorid.data)
    excerpt = form.excerpt.data
    content = form.content.data
    categoryid = Category.query.get(form.categoryid.data)
    status = form.title.data
    tag = form.title.data

    post = Post(
        title=title,
        slug=slug,
        authorid=authorid,
        excerpt=excerpt,
        content=content,
        categoryid=categoryid,
        status=status,
        tag=tag,
    )

    return post
