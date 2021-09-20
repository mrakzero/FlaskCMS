# -*- coding: utf-8 -*-
# File: post_resource.py
# Author: Zhangzhijun
# Date: 2021/2/12 21:22

from flask import jsonify, current_app

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.models.category import Category
from app.models.post import Post
from app.models.tag import Tag
from app.models.user import User
from app.utils import query_to_dict


class PostResource():
    @staticmethod
    def query_posts():
        current_app.logger.debug("Enter get function!")
        try:
            sql = 'SELECT t_post.id AS post_id, t_post.title AS post_title, t_post.slug AS post_slug, ' \
                  't_category.name AS post_category, t_post.excerpt AS post_excerpt, ' \
                  't_post.updatetime AS post_updatetime, t_post.publishtime AS post_publishtime,' \
                  't_post.status AS post_status, t_user.username AS post_author ' \
                  'FROM t_post, t_category, t_user WHERE t_post.categoryid = t_category.id AND t_post.authorid = t_user.id ' \
                  'ORDER BY t_post.publishtime DESC'
            posts = db.session.execute(sql)
            posts = list(posts)
            # posts = db.session.query(Post.id, Post.title, Post.slug, Category.name, Post.excerpt,
            #                          Post.updatetime, User.username) \
            #     .filter(Post.categoryid == Category.id) \
            #     .filter(Post.authorid == User.id) \
            #     .all() \
            #     .order_by(Post.publishtime.desc())

        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if posts is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        current_app.logger.debug("posts: %s", posts)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, posts=query_to_dict(posts))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    @staticmethod
    def query_post_by_id(post_id):
        try:
            post = db.session.query(Post.id, Post.title, Post.slug, Category.name, Post.excerpt,
                                    Post.updatetime, User.username, Post.content) \
                .filter(Post.id == post_id) \
                .filter(Post.categoryid == Category.id) \
                .filter(Post.authorid == User.id) \
                .first()

        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if post is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, post=query_to_dict(post))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    # get post by post name
    @staticmethod
    def query_post_by_title(title):
        try:
            post = db.session.query(Post.id, Post.title, Post.slug, Category.name, Post.excerpt,
                                    Post.updatetime, User.username, Post.content) \
                .filter(Post.title == title) \
                .filter(Post.categoryid == Category.id) \
                .filter(Post.authorid == User.id) \
                .all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if post is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, post=query_to_dict(post))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    # get posts by author
    @staticmethod
    def query_post_by_author(author):
        try:
            user = User.query.filter(User.username == author).first()
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
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, posts=query_to_dict(posts))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    # get posts by category
    @staticmethod
    def query_posts_by_category(category_name):
        try:
            category = Category.query.filter_by(name=category_name).first()
            posts = db.session.query(Post.id, Post.title, Post.slug, Category.name, Post.excerpt,
                                     Post.updatetime, User.username, Post.content) \
                .filter(Post.categoryid == category.id) \
                .filter(Post.authorid == User.id) \
                .all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if posts is None:
            return jsonify(code=ResponseCode.POST_NOT_EXIST, message=ResponseMessage.POST_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, posts=query_to_dict(posts))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    # get posts by tag
    @staticmethod
    def query_posts_by_tag(tag_name):
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
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, posts=query_to_dict(posts))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)
