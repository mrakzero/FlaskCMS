# -*- coding: utf-8 -*-
# File: post_resource.py
# Author: Zhangzhijun
# Date: 2021/2/12 21:22

from flask import flash, redirect, url_for, render_template, jsonify

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.forms.post_form import PostForm
from app.models.post import Category, Post
from app.models.user import User
from app.views.admin import bp_admin
from app.views.common.post_resource import PostResource


@bp_admin.route('/post', methods=['GET', 'POST'])
def create_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post = get_post_info(post_form)

        db.session.add(post)
        db.session.commit()
        return redirect(url_for('bp_admin.get_posts'))
    return render_template('admin/post/post-new.html', post_form=post_form)


@bp_admin.route('/posts', methods=['GET'])
def get_posts():
    data = PostResource.query_posts()
    return data


@bp_admin.route('/post/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id):
    data = PostResource.query_post_by_id(post_id)
    return data


@bp_admin.route('/post/<string:post_title>', methods=['GET'])
def get_post_by_title(post_title):
    data = PostResource.query_post_by_title(post_title)
    return data


@bp_admin.route('/post/<string:post_author>', methods=['GET'])
def get_post_by_author(post_author):
    data = PostResource.query_post_by_author(post_author)
    return data


@bp_admin.route('/post/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post_form = PostForm()

    try:
        post = Post.query.filter_by(id=post_id).first()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if post is None:
        return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)

    if post_form.validate_on_submit():
        post = get_post_info(post_form)
        db.session.add(post)
        db.session.commit()
        flash('Post updated.', 'success')
        return redirect(url_for('bp_admin.get_posts'))
    post_form.title.data = post.title
    post_form.slug.data = post.slug
    post_form.excerpt.data = post.excerpt
    post_form.content.data = post.content
    post_form.categoryid.data = post.categoryid
    post_form.status.data = post.status
    return render_template('admin/post/post-edit.html', post_form=post_form)


@bp_admin.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        post = Post.query.filter_by(id=post_id).first()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if post is None:
        return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('admin.post'))


# 从表单中获取post信息
def get_post_info(form):
    post = Post()
    post.title = form.title.data
    post.slug = form.slug.data
    post.authorid = User.query.get(form.authorid.data)
    post.excerpt = form.excerpt.data
    post.content = form.content.data
    post.categoryid = Category.query.get(form.categoryid.data)
    post.status = form.title.data
    post.tag = form.title.data

    return post
