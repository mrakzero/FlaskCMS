# -*- coding: utf-8 -*-
# File: post.py
# Author: Zhangzhijun
# Date: 2021/2/12 21:22
import os
from datetime import datetime
from random import random

from flask import Blueprint, request, flash, redirect, url_for, render_template, make_response

from app import db
from app.forms.post import PostForm
from app.models.post import Category, Post
from app.models.user import User

bp_admin_post = Blueprint('admin_post', __name__, url_prefix='/admin', template_folder='../templates/admin',
                          static_folder='../static')


@bp_admin_post.route('/post', methods=['GET'])
def post_query():
    posts = Post.query.all()
    return render_template('admin/post/post.html', posts=posts)


@bp_admin_post.route('/post/new', methods=['GET', 'POST'])
def create_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post = get_post_info(post_form)
        db.session.add(post)
        db.session.commit()
        flash('Post created.', 'success')
        return redirect(url_for('admin.post'))
    return render_template('admin/post/post-new.html', post_form=post_form)


@bp_admin_post.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
def update_post(post_id):
    post_form = PostForm()
    post = Post.query.get_or_404(post_id)
    if post_form.validate_on_submit():
        post = get_post_info(post_form)
        db.session.add(post)
        db.session.commit()
        flash('Post updated.', 'success')
        return redirect(url_for('admin.post'))
    post_form.title.data = post.title
    post_form.slug.data = post.slug
    post_form.excerpt.data = post.excerpt
    post_form.content.data = post.content
    post_form.categoryid.data = post.categoryid
    post_form.status.data = post.status
    return render_template('admin/post/post-edit.html', post_form=post_form)


@bp_admin_post.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
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

# def gen_rnd_filename():
#     filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#     return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))
#
#
# @bp_admin_post.route('/upload/', methods=['POST'])
# def ckupload():
#     """CKEditor file upload"""
#     error = ''
#     url = ''
#     callback = request.args.get("CKEditorFuncNum")
#     if request.method == 'POST' and 'upload' in request.files:
#         fileobj = request.files['upload']
#         fname, fext = os.path.splitext(fileobj.filename)
#         rnd_name = '%s%s' % (gen_rnd_filename(), fext)
#         filepath = os.path.join(app.static_folder, 'upload', rnd_name)
#         # 检查路径是否存在，不存在则创建
#         dirname = os.path.dirname(filepath)
#         if not os.path.exists(dirname):
#             try:
#                 os.makedirs(dirname)
#             except:
#                 error = 'ERROR_CREATE_DIR'
#         elif not os.access(dirname, os.W_OK):
#             error = 'ERROR_DIR_NOT_WRITEABLE'
#         if not error:
#             fileobj.save(filepath)
#             url = url_for('static', filename='%s/%s' % ('upload', rnd_name))
#     else:
#         error = 'post error'
#     res = """<script type="text/javascript">
#   window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
# </script>""" % (callback, url, error)
#     response = make_response(res)
#     response.headers["Content-Type"] = "text/html"
#     return response
