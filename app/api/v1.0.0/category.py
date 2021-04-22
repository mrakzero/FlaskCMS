#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version: 1.0.0
# File: category.py
# Author:Zhang Zhijun
# Time: 2021-03-13
from importlib.resources import Resource

from flask import jsonify
from flask_restful import fields, marshal_with

from app import api
from app.models.category import Category


class Categoty(Resource):
    resource_fields = {
        'id': fields.String,
        'name': fields.String,
        'slug': fields.String,
        'parentid': fields.Integer,
        'description': fields.String
    }

    def create_category(self):
        # todo
        pass

    def get_all_categories(self):
        try:
            categories = Category.query.filter().all()
        except:
            return jsonify(code=12, message='query filed.')
        if categories == None:
            return jsonify(code=12, message='result is none.')

    @marshal_with(resource_fields)
    def get_category_by_id(self, id):
        try:
            category = Category.query.filter(id=id).first()
        except:
            return jsonify(code=12, message='query filed.')
        if category == None:
            return jsonify(code=12, message='result is none.')

        return jsonify(code=0, message='query sueess.')

    @marshal_with(resource_fields)
    def get_category_by_name(self, name):
        pass
        # todo

    @marshal_with(resource_fields)
    def get_category_by_slug(self, slug):
        pass
        # todo

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


api.add_resource(Category, '/category/', endpoint='create_category')
api.add_resource(Category, '/categories/', endpoint='get_all_categories')
api.add_resource(Category, '/category/<int:id>/', endpoint='get_category_by_id')
api.add_resource(Category, '/category/<String:name>/', endpoint='create_category')
api.add_resource(Category, '/category/', endpoint='update_category')
api.add_resource(Category, '/category/<int:id>', endpoint='delete_category')
