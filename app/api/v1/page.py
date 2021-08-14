# -*- coding: utf-8 -*-
# File: page.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:22
from flask import Blueprint, render_template, redirect, flash, url_for, jsonify, current_app
from flask_restful import fields, reqparse, Resource, marshal_with

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.forms.page import PageForm
from app.models.category import Category
from app.models.page import Page
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
    'content': fields.String,
    'publishtime': fields.DateTime,
    'updatetime': fields.DateTime,
    'status': fields.Boolean

}

# 获取浏览器传递的请求参数
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入页面标题')
parser.add_argument('slug', type=str, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入页面别名')
parser.add_argument('authorid', type=int, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入作者')
parser.add_argument('content', type=str, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入页面内容')
parser.add_argument('status', type=bool, required=True, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请选择发布状态')


class PageListResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self):
        try:
            pages = Page.query.join(User, (User.id == Page.authorid)) \
                .with_entitles(Page.id, Page.title, Page.slug, User.username, Page.publishtime) \
                .all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if pages is None:
            return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)
        current_app.logger.debug("pages: %s", pages)

        return pages


class PageResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, id):
        try:
            # Page = Page.query.filter_by(id=id).first()
            # Page = db.session.query(Page.id, Page.title, Page.slug, User.username, Category.name, Page.excerpt,
            #                         Page.publishtime) \
            #     .filter(Page.id==id) \
            #     .filter(Page.categoryid == Category.id) \
            #     .filter(Page.authorid == User.id)
            page = Page.query.join(User, (User.id == Page.authorid)) \
                .filter(Page.id == id) \
                .all()

        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)

        if Page is None:
            return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)
        current_app.logger.debug("Page: %s", page)
        # data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(Page))
        # current_app.logger.debug("data: %s", data)
        return page

    def post(self):
        current_app.logger.debug("Enter post function")
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)
        current_app.logger.debug("args: %s", args)

        page = Page(
            title=args.title,
            slug=args.slug,
            authorid=args.authorid,
            content=args.content,
            status=args.status
        )
        current_app.logger.debug("page: %s", page)
        db.session.add(page)
        db.session.commit()

        flash('page created.', 'success')
        data = dict(code=ResponseCode.CREATE_Page_SUCCESS, message=ResponseMessage.CREATE_Page_SUCCESS)
        return jsonify(data)

    def put(self, page_id):
        current_app.logger.debug("Enter put function")
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)
        current_app.logger.debug("args: %s", args)

        try:
            page = Page.query.filter_by(id=page_id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if page is None:
            return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)

        page.title = args.title,
        page.slug = args.slug,
        page.content = args.content,
        page.status = args.status
        db.session.commit()
        data = dict(code=ResponseCode.UPDATE_PAGE_SUCCESS, message=ResponseMessage.UPDATE_PAGE_SUCCESS)
        return jsonify(data)

    def delete(self, page_id):
        current_app.logger.debug("Enter delete function")
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)
        current_app.logger.debug("args: %s", args)

        try:
            page = Page.query.filter_by(id=page_id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if page is None:
            return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)
        db.session.delete(page)
        db.session.commit()
        flash('page deleted.', 'success')
        data = dict(code=ResponseCode.DELETE_PAGE_SUCCESS, message=ResponseMessage.DELETE_PAGE_SUCCESS)
        return jsonify(data)


# get Page by Page name
class PageTitleResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, title):
        try:
            page = Page.query.filter_by(title=title).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if page is None:
            return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(page))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)


# get Pages by author id
class PageAuthorResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, author):
        try:
            author = User.query.filter_by(username=author)
            page = Page.query.filter_by(authorid=author.id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if page is None:
            return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(page))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)
