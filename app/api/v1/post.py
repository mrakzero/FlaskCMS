# -*- coding: utf-8 -*-
# File: post.py
# Author: Zhangzhijun
# Date: 2021/2/12 21:22


from flask import flash, redirect, url_for, jsonify, current_app
from flask_restful import fields, Resource, reqparse, marshal_with

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.models.category import Category
from app.models.post import Post, t_post_tag
from app.models.tag import Tag
from app.models.user import User
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
                    help=u'请输入分类名称')
parser.add_argument('slug', type=str, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'')
parser.add_argument('authorid', type=int, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入分类名称')
parser.add_argument('categoryid', type=int, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入分类名称')
parser.add_argument('excerpt', type=str, trim=True, location=[u'json', u'form', u'args', u'values'], help=u'')
parser.add_argument('content', type=str, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help='')
parser.add_argument('image', type=str, required=False, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'')
# parser.add_argument('tag', type=int, trim=False, location=[u'json', u'form', u'args', u'values'], help=u'')
parser.add_argument('status', type=bool, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help='')


class PostListResource(Resource):
    # @marshal_with(resource_fields, envelope='resource')
    def get(self):
        current_app.logger.debug("Enter get function!")
        try:
            # posts = Post.query.filter().all()
            # posts = Post.query.join(Category, (Category.id == Post.categoryid)) \
            #     .join(User, (User.id == Post.authorid)) \
            #     .with_entitles(Post.id, Post.title, Post.slug, User.username, Category.name, Post.excerpt,
            #                    Post.publishtime) \
            #     .all()
            posts = Post.query.join(Category, (Category.id == Post.categoryid)) \
                .join(User, (User.id == Post.authorid)) \
                .all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if posts is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)

        post_dict = [lambda: post for post in posts]
        current_app.logger.debug("posts: %s", serialize(post_dict))

        return post_dict


class PostResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, id):
        try:
            # post = Post.query.filter_by(id=id).first()
            # post = db.session.query(Post.id, Post.title, Post.slug, User.username, Category.name, Post.excerpt,
            #                         Post.publishtime) \
            #     .filter(Post.id==id) \
            #     .filter(Post.categoryid == Category.id) \
            #     .filter(Post.authorid == User.id)
            post = Post.query.join(Category, (Category.id == Post.categoryid)) \
                .join(User, (User.id == Post.authorid)) \
                .filter(Post.id == id) \
                .all()
            current_app.logger.debug("post: %s", post)
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if post is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        current_app.logger.debug("post: %s", post)
        # data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(post))
        # current_app.logger.debug("data: %s", data)
        return post

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
        current_app.logger.debug("Enter put function")
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)
        current_app.logger.debug("args: %s", args)

        try:
            post = Post.query.filter_by(id=post_id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if post is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)

        post.title = args.title,
        post.slug = args.slug,
        post.excerpt = args.excerpt,
        post.content = args.content,
        post.categoryid = args.categoryid,
        post.status = args.status
        db.session.commit()
        data = dict(code=ResponseCode.UPDATE_POST_SUCCESS, message=ResponseMessage.UPDATE_POST_SUCCESS)
        return jsonify(data)

    def delete(self, post_id):
        try:
            post = Post.query.filter_by(id=post_id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if post is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)

        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', 'success')
        data = dict(code=ResponseCode.DELETE_POST_SUCCESS, message=ResponseMessage.DELETE_POST_SUCCESS)
        return jsonify(data)


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


# get posts by category
class PostCategoryResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, category_name):
        try:
            category = Category.query.filter_by(name=category_name).first()
            posts = Post.query.filter_by(categoryid=category.id).all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if posts is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(posts))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)


# get posts by tag
class PostTagResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, tag_name):
        # todo
        try:
            # 多对多关系中获取对象,只能用get(id)方法,不能通过filter或者filter_by来获取
            tag = Tag.query.get(tag_name)
            # post = db.session.query(Post.id, Post.title, Post.slug, User.username, Category.name, Post.excerpt,
            #                         Post.publishtime) \
            #     .filter(Post.id==id) \
            #     .filter(Post.categoryid == Category.id) \
            #     .filter(Post.authorid == User.id)

            # post_id_list = db.session.query(t_post_tag.postid).filter(t_post_tag.tagid == tag.id)
            # post = Post.query.filter_by(tag=tag).first()
            posts = Post.tag.all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if posts is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(posts))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)
