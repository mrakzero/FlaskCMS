# -*- coding: utf-8 -*-
# File: post_resource.py
# Author: Zhangzhijun
# Date: 2021/2/12 21:22

from flask import flash, redirect, url_for, render_template, make_response, jsonify, current_app

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.forms.post_form import PostForm
from app.models.post import Category, Post
from app.models.user import User
from app.utils import query_to_dict
from app.views.admin import bp_admin


@bp_admin.route('/post', methods=['GET', 'POST'])
def create_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post = get_post_info(post_form)

        db.session.add(post)
        db.session.commit()
        flash('Post created.', 'success')
        return redirect(url_for('admin.post'))
    return render_template('admin/post/post-new.html', post_form=post_form)


@bp_admin.route('/posts', methods=['GET'])
def get_posts():
    try:
        posts = db.session.query(Post.id, Post.title, Post.slug, Category.name, Post.excerpt,
                                 Post.updatetime, User.username) \
            .filter(Post.categoryid == Category.id) \
            .filter(Post.authorid == User.id) \
            .all()
        # .order_by('Post.publishtime')  # 降序 ‘-Post.publishtime’
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if posts is None:
        return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
    current_app.logger.debug("posts: %s", posts)
    data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(posts))
    current_app.logger.debug("data: %s", data)

    return render_template('admin/post/post.html', posts=data)


@bp_admin.route('/post/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id):
    try:
        posts = db.session.query(Post.id, Post.title, Post.slug, Category.name, Post.excerpt,
                                 Post.updatetime, User.username, Post.content) \
            .filter(Post.title == post_id) \
            .filter(Post.categoryid == Category.id) \
            .filter(Post.authorid == User.id) \
            .all()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if posts is None:
        return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
    data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(posts))
    current_app.logger.debug("data: %s", data)
    return jsonify(data)


@bp_admin.route('/post/<string:post_title>', methods=['GET'])
def get_post_by_title(post_title):
    try:
        posts = db.session.query(Post.id, Post.title, Post.slug, Category.name, Post.excerpt,
                                 Post.updatetime, User.username, Post.content) \
            .filter(Post.title == post_title) \
            .filter(Post.categoryid == Category.id) \
            .filter(Post.authorid == User.id) \
            .all()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if posts is None:
        return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
    data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(posts))
    current_app.logger.debug("data: %s", data)
    return jsonify(data)


@bp_admin.route('/post/<string:post_author>', methods=['GET'])
def get_post_by_author(post_author):
    try:
        user = User.query.filter(User.username == post_author).first()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if user is None:
        return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)
    try:
        posts = db.session.query(Post.id, Post.title, Post.slug, Category.name, Post.excerpt,
                                 Post.updatetime, User.username, Post.content) \
            .filter(Post.authorid == user.id) \
            .filter(Post.categoryid == Category.id) \
            .all()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if posts is None:
        return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
    data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(posts))
    current_app.logger.debug("data: %s", data)
    return jsonify(data)


@bp_admin.route('/post/<int:post_id>', methods=['PUT'])
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


@bp_admin.route('/post/<int:post_id>', methods=['DELETE'])
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
# @bp_admin.route('/upload/', methods=['POST'])
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
