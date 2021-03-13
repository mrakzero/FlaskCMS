# -*- coding: utf-8 -*-

# File: post.py
# author:Zhang Zhijun
# Date: 2021-03-13
# version: 1.0.0
# Modify:
from flask_restful import Resource, reqparse, fields, abort
from sqlalchemy import String

from app import api

resource_fields = {
    'title': fields.String,
    'slug': fields.String,
    'authorid': fields.Integer,
    'excerpt': fields.String,
    'content': fields.String,
    'categoryid': fields.String,
    'publishtime': fields.DateTime,
    'updatetime': fields.DateTime,
    'tag': fields.List,
    'status': fields.Boolean
}

def abort_if_post_doesnt_exist(post_id):
    if Post.query.filter(id = post_id).first() == None:
        abort(404, message="Post {} doesn't exist".format(post_id))

class PostList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParse()
        self.reqparse.add.argument()
        super(PostList, self).__init__()

    def get_all(self):
        # todo
        pass

    def get_by_author(self, author):
        # todo
        pass

    def get_by_category(self):
        # todo
        pass

    def get_by_tag(self):
        # todo
        pass


class Post(Resource):
    # def __init__(self):
    #     self.reqparser = reqparse.RequestParser()
    #     self.reqparse.add.argument('title',type=String)
    #     args =reqparse.parser_args()
    #     super(PostList, self).__init__()

    def get_post_by_id(self, id):
        pass

    def create_post(self):
        pass

    def update_post(self, id):
        pass

    def delete_post(self, id):
        pass


api.add_resource(PostList, '/api/v1.0.0/posts', endpoint='posts')
api.add_resource(PostList, '/api/v1.0.0/posts/<String:author>', endpoint='get_by_author')
api.add_resource(PostList, '/api/v1.0.0/posts/<String:category>', endpoint='get_by_category')
api.add_resource(PostList, '/api/v1.0.0/posts/<String:tag>', endpoint='get_by_tag')
api.add_resource(Post, '/api/v1.0.0/posts/<int:id>', endpoint='post')
