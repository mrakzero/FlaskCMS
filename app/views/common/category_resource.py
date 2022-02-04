#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version: 1.0.0
# File: category_resource.py
# Author:Zhang Zhijun
# Time: 2021-03-13

from flask import current_app

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.models.category import Category
from app.utils import query_to_dict


def abort_if_not_exist(category_id):
    """
    操作之前需要保证操作的分类存在，否则返回 404
    :param category_id:
    :return:
    """
    desc = 'The category {} not exist.'.format(category_id)
    category = Category.query.query_or_404(category_id, description=desc)
    return category


class CategoryResource():

    @staticmethod
    def query_categories():
        # page_num = request.args.get('page_num', 1)
        # per_page = request.args.get('per_page', 10)
        #
        # try:
        #     page_num = int(page_num)
        #     per_page = int(per_page)
        # except ValueError:
        #     return {'message': 'Make sure page_num and per_page are integers.'}, 400
        # if per_page > 10:
        #     per_page = 10d
        #
        # paginate = Category.page(page_num, per_page)

        try:
            categories = Category.query.filter().all()
        except:
            return dict(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if categories is None:
            return dict(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, categories=query_to_dict(categories))
        current_app.logger.debug("data: %s", data)

        return data

    @staticmethod
    def query_category_by_id(category_id):
        try:
            category = Category.query.filter_by(id=category_id).first()
        except:
            return dict(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if category is None:
            return dict(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(category))
        current_app.logger.debug("data: %s", data)
        return data

    @staticmethod
    def query_category_by_title(category_title):
        try:
            category = Category.query.filter_by(id=category_title).first()
        except:
            return dict(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if category is None:
            return dict(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(category))
        current_app.logger.debug("data: %s", data)
        return data
