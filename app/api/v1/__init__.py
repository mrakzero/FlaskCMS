# -*- coding: utf-8 -*-
# File: __init__.py
# Author: Zhangzhijun
# Date: 2021/5/3 12:26
from flask_restful import Api

from app import api
from app.api.v1.category import CategoryResource, CategoryListResource
from app.api.v1.post import PostListResource, PostResource, PostAuthorResource, PostCategoryResource, \
    PostTitleResource
from app.api.v1.user import UserListResource, UserRegisterResource, UserLoginResource, UserlogoutResource, UserResource

api = Api()  # restful api


# def init_app(app):
#     api.init_app(app)


def registerResources():
    # User Resource
    api.add_resource(UserRegisterResource, '/register', endpoint='ep_user_register')
    api.add_resource(UserLoginResource, '/login', endpoint='ep_user_login')
    api.add_resource(UserlogoutResource, '/logout', endpoint='ep_user_logout')
    api.add_resource(UserListResource, '/users', endpoint='ep_users')
    api.add_resource(UserResource, '/user', '/user/<int:id>', endpoint='ep_user')

    # Category Resouce
    api.add_resource(CategoryListResource, '/categories', endpoint='ep_categories')
    api.add_resource(CategoryResource, '/category', '/category/<int:id>', endpoint='ep_category')

    # Post Resource
    api.add_resource(PostListResource, '/posts', endpoint='ep_posts')
    api.add_resource(PostResource, '/post', '/post/<int:id>', endpoint='ep_post')
    api.add_resource(PostTitleResource, '/post/title/<string:title>', endpoint='ep_get_post_by_name')
    api.add_resource(PostAuthorResource, '/post/author/<string:atuhror>', endpoint='get_post_by_author')
    api.add_resource(PostCategoryResource, '/post/category/<string:category>', endpoint='get_post_by_category')
    # api.add_resource(PostResource, '/post/tag/<String:tag>', endpoint='get_post_by_tag')
