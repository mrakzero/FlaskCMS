# -*- coding: utf-8 -*-
# File: post.py
# Author: Zhangzhijun
# Date: 2021/2/12 21:22


from flask import flash, redirect, url_for, jsonify
from flask_restful import fields, Resource, reqparse, marshal_with

from app import db
from app.errors.errorcode import ResponseCode, ErrorCode
from app.forms.post import PostForm
from app.models.post import Post

PARSER_ARGS_STATUS = True

# 声明各字段数据类型用来序列化
resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'slug': fields.String,
    'authorid': fields.Integer,
    'excerpt': fields.String,
    'content': fields.String,
    'categoryid': fields.Integer,
    'image': fields.String,
    'publishtime': fields.DateTime,
    'updatetime': fields.DateTime,
    'counter': fields.Integer,
    'tag': fields.List(fields.Nested({
        'id': fields.Integer,
        'name': fields.String
    })),
    'status': fields.Boolean,
    'comment': fields.List(fields.Integer)
}

# 获取浏览器传递的请求参数
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, trim=True, location='form', help=u'请出入分类名称')
parser.add_argument('slug', type=str, required=True, trim=True, location='form', help=u'')
parser.add_argument('authorid', type=str, required=True, trim=True, location='form', help=u'请出入分类名称')
parser.add_argument('categoryid', type=str, required=True, trim=True, location='form', help=u'请出入分类名称')
parser.add_argument('excerpt', type=int, trim=True, help=u'')
parser.add_argument('content', type=str, required=True, trim=True, location='form', help='')
parser.add_argument('image', type=str, required=True, trim=True, location='form', help=u'')
parser.add_argument('tag', type=int, trim=True, help=u'')
parser.add_argument('status', type=str, required=True, trim=True, location='form', help='')


class PostsResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self):
        posts = Post.query.all()

        data = {
            'status': ErrorCode.SUCCESS,
            'msg': '获取成功',
            'data': posts
        }

        return data


class PostResource(Resource):

    def get_post_by_title(self, title):
        return Post.get_by_title(title)

    def get_posts_by_author(self, authorid):
        return Post.get_by_authror()

    def create_post(self):
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)

        title = args.title
        slug = args.slug
        authorid = args.authorid
        excerpt = args.excerpt
        content = args.content
        categoryid = args.categoryid
        status = args.title
        tag = args.title

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

        db.session.add(post)
        db.session.commit()

        flash('Post created.', 'success')
        date = dict(ResponseCode.SUCCESS)
        return jsonify(date)

    def update_post(post_id):
        post_form = PostForm()
        post = Post.query.get_or_404(post_id)

    def delete_post(post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', 'success')
        return redirect(url_for('admin.post'))
