#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version: 1.0.0
# File: category.py
# Author:Zhang Zhijun
# Time: 2021-03-13

from flask import jsonify
from flask_restful import fields, marshal_with, reqparse, Resource

from app.models.category import Category

PARSER_ARGS_STATUS = True

resource_fields = {
    'id': fields.String,
    'name': fields.String,
    'slug': fields.String,
    'parentid': fields.Integer,
    'description': fields.String
}


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


class CategoryResource(Resource):

    @marshal_with(resource_fields)
    def create_category(self):
        # todo
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, trim=True, location='form', help=u'请出入分类名称')
        parser.add_argument('slug', type=str, required=True, trim=True, location='form', help=u'')
        parser.add_argument('parentid', type=int, trim=True, help=u'')
        parser.add_argument('description', type=str, required=True, trim=True, location='form', help='')
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)

    @marshal_with(resource_fields)
    def get_category_by_id(self, category_id):

        try:
            category = Category.query.filter(id=category_id).first()
        except:
            return jsonify(code=12, message='query filed.')
        if category == None:
            return jsonify(code=12, message='result is none.')

        return category

    @marshal_with(resource_fields)
    def get_category_by_name(self, name):
        try:
            category = Category.query.filter(id=name).first()
        except:
            return jsonify(code=12, message='query filed.')
        if category == None:
            return jsonify(code=12, message='result is none.')

        return category

    @marshal_with(resource_fields)
    def get_category_by_slug(self, slug):
        try:
            category = Category.query.filter(id=slug).first()
        except:
            return jsonify(code=12, message='query filed.')
        if category == None:
            return jsonify(code=12, message='result is none.')

        return category

    def update_category(self, id):
        try:
            categories = Category.query.filter(id=id).first()
        except:
            return jsonify(code=12, message='query filed.')
        if categories == None:
            return jsonify(code=12, message='result is none.')

    def delete_category(self, id):
        try:
            categories = Category.query.filter(id=id).first()
        except:
            return jsonify(code=12, message='query filed.')
        if categories == None:
            return jsonify(code=12, message='result is none.')