# -*- coding: utf-8 -*-
# File: __init__.py
# Author: Zhangzhijun
# Date: 2021/5/3 12:26
from flask_restful import Api

from app import api
from app.api.v1.category import CategoryResource, CategoryListResource
from app.api.v1.post import PostListResource, PostResource

api = Api()  # restful api


# def init_app(app):
#     api.init_app(app)


def registerResources():
    # Category
    api.add_resource(CategoryListResource, '/categories', endpoint='ep_categories')
    api.add_resource(CategoryResource, '/category', '/category/<int:id>', endpoint='ep_category')

    # Post
    api.add_resource(PostListResource, '/posts', endpoint='ep_posts')
    api.add_resource(PostResource, '/post', '/post/<int:id>', endpoint='ep_post')
    # api.add_resource(PostResource, '/post/title/<String:title>', endpoint='get_post_by_name')
    # api.add_resource(PostResource, '/post/author/<int:atuhrorid>', endpoint='get_post_by_author')
    # api.add_resource(PostResource, '/post/category/<int:categoryid>', endpoint='get_post_by_category')
    # api.add_resource(PostResource, '/post/tag/<String:tag>', endpoint='get_post_by_tag')
