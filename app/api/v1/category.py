#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version: 1.0.0
# File: category.py
# Author:Zhang Zhijun
# Time: 2021-03-13

from flask import jsonify, request, flash, current_app
from flask_restful import fields, marshal_with, reqparse, Resource

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.models.category import Category
from app.utils import serialize

PARSER_ARGS_STATUS = True

resource_fields = {
    'id': fields.String,
    'name': fields.String,
    'slug': fields.String,
    'parentid': fields.Integer,
    'description': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, required=False, trim=True, location=[u'json', u'form', u'args', u'values'])
parser.add_argument('name', type=str, required=False, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入分类名称')
parser.add_argument('slug', type=str, required=False, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入分类别名')
parser.add_argument('parentid', type=int, trim=False, location=[u'json', u'form', u'args', u'values'], help=u'')
parser.add_argument('description', type=str, required=False, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入分类描述')


def abort_if_not_exist(category_id):
    """
    操作之前需要保证操作的分类存在，否则返回 404
    :param category_id:
    :return:
    """
    desc = 'The category {} not exist.'.format(category_id)
    category = Category.query.get_or_404(category_id, description=desc)
    return category


class CategoryListResource(Resource):
    # https://github.com/frankRose1/flask-blog-restful-api/blob/master/resources/posts.py

    @marshal_with(resource_fields)
    def get(self):
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


class CategoryResource(Resource):

    def get(self, id):
        try:
            category = Category.query.filter_by(id=id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if category is None:
            return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(category))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    def post(self):
        # todo

        args = parser.parse_args(strict=PARSER_ARGS_STATUS)

        if (Category.query.filter_by(slug=args.slug).count() > 0) or (
                Category.query.filter_by(name=args.name).count() > 0):
            return jsonify(code=ResponseCode.CATEGORY_ALREADY_EXIST, message=ResponseMessage.CATEGORY_ALREADY_EXIST)

        category = Category(
            name=args.name,
            slug=args.slug,
            description=args.description
        )
        db.session.add(category)
        db.session.commit()

        flash('Post created.', 'success')
        data = dict(code=ResponseCode.CREATE_CATEGORY_SUCCESS, message=ResponseMessage.CREATE_CATEGORY_SUCCESS)
        return jsonify(data)

    def put(self, id):
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)
        try:
            category = Category.query.filter_by(id=id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if category is None:
            return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)

        category.name = args.name
        category.slug = args.slug
        category.id = args.parentid
        category.description = args.description

        db.session.commit()

        flash('Post created.', 'success')
        date = dict(code=ResponseCode.UPDATE_CATEGORY_SUCCESS, message=ResponseMessage.UPDATE_CATEGORY_SUCCESS)
        return jsonify(date)

    def delete(self, id):
        """
        delete specificated post.
        paras: post_id
        """
        try:
            category = Category.query.filter_by(id=id).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if category is None:
            return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)

        db.session.delete(category)
        db.session.commit()
        flash('Category deleted.', 'success')

        # 未分类文章处理方法
        # TODO

        date = dict(code=ResponseCode.DELETE_CATEGORY_SUCCESS, message=ResponseMessage.DELETE_CATEGORY_SUCCESS)
        return jsonify(date)


def get_category_info(args):
    category = Category
    category.id = args.id
    category.name = args.name
    category.slug = args.slug
    category.parentid = args.parentid
    category.description = args.description

    return category
