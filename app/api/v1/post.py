# -*- coding: utf-8 -*-
# File: post.py
# Author: Zhangzhijun
# Date: 2021/2/12 21:22


from flask import flash, redirect, url_for, jsonify, current_app
from flask_restful import fields, Resource, reqparse, marshal_with

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.models.post import Post
from app.utils import serialize

PARSER_ARGS_STATUS = True

# 声明各字段数据类型用来序列化
resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'slug': fields.String,
    'author': fields.Nested({
        'username': fields.String
    }),
    'excerpt': fields.String,
    'content': fields.String,
    'category': fields.Nested({
        'name': fields.String
    }),
    'image': fields.String,
    'publishtime': fields.DateTime,
    'updatetime': fields.DateTime,
    'counter': fields.Integer,
    'tag': fields.List(fields.Nested({
        'id': fields.Integer,
        'name': fields.String
    })),
    'status': fields.Boolean,
    'comment': fields.List(fields.Nested({
        'id': fields.Integer,
        'nickname': fields.String,
        'content': fields.String,
        'date': fields.DateTime
    }))
}

# 获取浏览器传递的请求参数
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请出入分类名称')
parser.add_argument('slug', type=str, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'')
parser.add_argument('authorid', type=int, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请出入分类名称')
parser.add_argument('categoryid', type=int, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请出入分类名称')
parser.add_argument('excerpt', type=str, trim=True, location=[u'json', u'form', u'args', u'values'], help=u'')
parser.add_argument('content', type=str, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help='')
parser.add_argument('image', type=str, required=False, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'')
# parser.add_argument('tag', type=int, trim=False, location=[u'json', u'form', u'args', u'values'], help=u'')
parser.add_argument('status', type=bool, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help='')


class PostListResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self):
        try:
            posts = Post.query.filter().all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if posts is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        current_app.logger.debug("posts: %s", posts)

        return posts


class PostResource(Resource):

    def get(self, id):
        try:
            post = Post.query.filter_by(id=id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if post is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(post))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    def post(self):
        current_app.logger.debug("Enter post function")
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)
        current_app.logger.debug("args: %s", args)

        post = Post(
            title=args.title,
            slug=args.slug,
            authorid=args.authorid,
            excerpt=args.excerpt,
            content=args.content,
            categoryid=args.categoryid,
            status=args.status
        )
        current_app.logger.debug("post: %s", post)
        db.session.add(post)
        db.session.commit()

        flash('Post created.', 'success')
        data = dict(code=ResponseCode.CREATE_POST_SUCCESS, message=ResponseMessage.CREATE_POST_SUCCESS)
        return jsonify(data)

    def put(self, post_id):
        post = Post.query.get_or_404(post_id)

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', 'success')
        return redirect(url_for('admin.post'))


# get post by post name
class PostTitleResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, title):
        try:
            post = Post.query.filter_by(title=title).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if post is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(post))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)


# get posts by author id
class PostAuthorResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, authorid):
        try:
            post = Post.query.filter_by(authorid=authorid).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if post is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(post))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)


# get posts by category id
class PostCategoryResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, categoryid):
        try:
            post = Post.query.filter_by(categoryid=categoryid).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if post is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(post))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

# class PostTagResource(Resource):
#     @marshal_with(resource_fields, envelope='resource')
#     def get(self, tag):
#         try:
#             post = Post.query.filter_by(tag=tag).first()
#         except:
#             return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
#         if post is None:
#             return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
#         data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(post))
#         current_app.logger.debug("data: %s", data)
#         return jsonify(data)
