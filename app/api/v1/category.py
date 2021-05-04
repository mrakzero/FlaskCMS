#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version: 1.0.0
# File: category.py
# Author:Zhang Zhijun
# Time: 2021-03-13

from flask import jsonify, request, flash, current_app
from flask_restful import fields, marshal_with, reqparse, Resource

from app import db
from app.errors.errorcode import ResponseCode
from app.models.category import Category

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
            return jsonify(code=12, message='query filed.')
        if categories is None:
            return jsonify(code=12, message='result is none.')

        return categories


class CategoryResource(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        try:
            category = Category.query.filter_by(id=id).first()
        except:
            return jsonify(code=12, message='query filed.')
        if category is None:
            return jsonify(code=12, message='result is none.')
        return category

    @marshal_with(resource_fields)
    def post(self):
        # todo

        args = parser.parse_args(strict=PARSER_ARGS_STATUS)

        if (Category.query.filter_by(slug=args.slug).count() > 0) or (
                Category.query.filter_by(name=args.name).count() > 0):
            return jsonify(code=11, message='category already exist.')

        category = Category(
            name=args.name,
            slug=args.slug,
            description=args.description
        )
        db.session.add(category)
        db.session.commit()

        flash('Post created.', 'success')
        # date = ResponseCode.SUCCESS
        # return jsonify(ResponseCode.SUCCESS())
        return category

    def put(self, id):
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)
        try:
            category = Category.query.filter_by(id=id).first()
        except:
            return jsonify(code=12, message='query filed.')
        if category is None:
            return jsonify(code=12, message='result is none.')

        category.name = args.name
        category.slug = args.slug
        category.id = args.parentid
        category.description = args.description

        db.session.commit()

        flash('Post created.', 'success')
        date = ResponseCode.SUCCESS
        return jsonify(ResponseCode.SUCCESS())

    def delete(self, id):
        """
        delete specificated post.
        paras: post_id
        """
        try:
            category = Category.query.filter_by(id=id).first()
        except:
            return jsonify(code=12, message='query filed.')
        if category == None:
            return jsonify(code=12, message='result is none.')

        db.session.delete(category)
        db.session.commit()
        flash('Post deleted.', 'success')

        # 未分类文章处理方法
        # TODO

        return jsonify(ResponseCode.SUCCESS())


def get_category_info(args):
    category = Category
    category.id = args.id
    category.name = args.name
    category.slug = args.slug
    category.parentid = args.parentid
    category.description = args.description

    return category
