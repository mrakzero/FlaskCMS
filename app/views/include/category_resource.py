#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version: 1.0.0
# File: category_resource.py
# Author:Zhang Zhijun
# Time: 2021-03-13

from flask import jsonify, request, flash, current_app

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
    category = Category.query.get_or_404(category_id, description=desc)
    return category


class CategoryResource():

    def get_categories(self):
        # page_num = request.args.get('page_num', 1)
        # per_page = request.args.get('per_page', 10)
        #
        # try:
        #     page_num = int(page_num)
        #     per_page = int(per_page)
        # except ValueError:
        #     return {'message': 'Make sure page_num and per_page are integers.'}, 400
        # if per_page > 10:
        #     per_page = 10
        #
        # paginate = Category.page(page_num, per_page)

        try:
            categories = Category.query.filter().all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if categories is None:
            return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)
        current_app.logger.debug("categories: %s", categories)

        return categories

    def get_category_by_id(self, category_id):
        try:
            category = Category.query.filter_by(id=category_id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if category is None:
            return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(category))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    def create_category(self, category):
        # todo

        if (Category.query.filter_by(slug=category.slug).count() > 0) or (
                Category.query.filter_by(name=category.name).count() > 0):
            return jsonify(code=ResponseCode.CATEGORY_ALREADY_EXIST, message=ResponseMessage.CATEGORY_ALREADY_EXIST)

        c = Category(
            name=category.name,
            slug=category.slug,
            description=category.description
        )
        db.session.add(c)
        db.session.commit()

        flash('Post created.', 'success')
        data = dict(code=ResponseCode.CREATE_CATEGORY_SUCCESS, message=ResponseMessage.CREATE_CATEGORY_SUCCESS)
        return jsonify(data)

    def update_category(self, category):

        try:
            c = Category.query.filter_by(id=category.id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if category is None:
            return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)

        c.name = category.name
        c.slug = category.slug
        c.id = category.parentid
        c.description = category.description

        db.session.commit()

        flash('Post created.', 'success')
        date = dict(code=ResponseCode.UPDATE_CATEGORY_SUCCESS, message=ResponseMessage.UPDATE_CATEGORY_SUCCESS)
        return jsonify(date)

    def delete_category(self, category_id):
        """
        delete specificated post.
        paras: post_id
        """
        try:
            c = Category.query.filter_by(id=category_id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if c is None:
            return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)

        db.session.delete(c)
        db.session.commit()
        flash('Category deleted.', 'success')

        # 未分类文章处理方法
        # TODO

        date = dict(code=ResponseCode.DELETE_CATEGORY_SUCCESS, message=ResponseMessage.DELETE_CATEGORY_SUCCESS)
        return jsonify(date)
