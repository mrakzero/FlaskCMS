# -*- coding: utf-8 -*-
# File: page_resource.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:22
from flask import flash, jsonify, current_app

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.models.page import Page
from app.models.user import User
from app.utils import query_to_dict


class PageResource():
    def get_pages(self):
        try:
            pages = db.session.query(Page.id, Page.title, Page.slug, User.username, Page.publishtime) \
                .filter(Page.authorid == User.id) \
                .all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if pages is None:
            return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)
        current_app.logger.debug("posts: %s", pages)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(pages))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    def get_page_by_id(self, page_id):
        try:
            p = db.session.query(Page.id, Page.title, Page.slug, User.username, Page.excerpt,
                                 Page.updatetime) \
                .filter(Page.id == page_id) \
                .filter(Page.authorid == User.id) \
                .first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)

        if p is None:
            return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)
        current_app.logger.debug("page: %s", p)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(p))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    def create_page(self, page):
        current_app.logger.debug("Enter page function")
        current_app.logger.debug("page: %s", page)

        db.session.add(page)
        db.session.commit()
        flash('Post created.', 'success')

        data = dict(code=ResponseCode.CREATE_PAGE_SUCCESS, message=ResponseMessage.CREATE_PAGE_SUCCESS)
        return jsonify(data)

    def put(self, page):

        try:
            p = Page.query.filter_by(id=page.id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if p is None:
            return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)

        db.session.commit()
        data = dict(code=ResponseCode.UPDATE_PAGE_SUCCESS, message=ResponseMessage.UPDATE_PAGE_SUCCESS)
        return jsonify(data)

    def delete(self, page_id):
        current_app.logger.debug("Enter delete function")

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
    def get_page_by_title(self, title):
        try:
            pages = db.session.query(Page.id, Page.title, Page.slug, User.username, Page.excerpt,
                                     Page.updatetime) \
                .filter(Page.title == title) \
                .filter(Page.authorid == User.id) \
                .all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if pages is None:
            return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)
        current_app.logger.debug("posts: %s", pages)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(pages))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    # get Pages by author

    def get_page_by_author(self, author):
        try:
            author = User.query.filter_by(username=author).first()
            pages = db.session.query(Page.id, Page.title, Page.slug, User.username, Page.excerpt,
                                     Page.updatetime) \
                .filter(Page.authorid == author.id) \
                .all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if pages is None:
            return jsonify(code=ResponseCode.PAGE_NOT_EXIST, message=ResponseMessage.PAGE_NOT_EXIST)
        current_app.logger.debug("posts: %s", pages)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(pages))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)
