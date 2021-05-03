# -*- coding: utf-8 -*-
# File: resourceList.py
# Author: Zhangzhijun
# Date: 2021/5/3 9:48
from app import api
from app.api.v1.category import CategoryResource, CategoryListResource
from app.api.v1.post import PostsResource, PostResource


def loadResources():
    # Category
    api.add_resource(CategoryResource, '/category', endpoint='category')
    api.add_resource(CategoryListResource, '/categories', endpoint='categories')
    api.add_resource(CategoryResource, '/category/<int:id>', endpoint='category')
    api.add_resource(CategoryResource, '/category/<String:slug>', endpoint='category')

    # Post
    api.add_resource(PostsResource, '/posts', endpoint='get_all_posts')
    api.add_resource(PostResource, '/post/<int:id>', endpoint='get_post_by_id')
    api.add_resource(PostResource, '/post/title/<String:title>', endpoint='get_post_by_name')
    api.add_resource(PostResource, '/post/author/<int:atuhrorid>', endpoint='get_post_by_author')
    api.add_resource(PostResource, '/post/category/<int:categoryid>', endpoint='get_post_by_category')
    api.add_resource(PostResource, '/post/tag/<String:tag>', endpoint='get_post_by_tag')
