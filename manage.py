# -*- coding: utf-8 -*-

import os

from app import create_app, db
from flask_migrate import Migrate

from app.models.category import Category
from app.models.comment import Comment
from app.models.page import Page
from app.models.post import Post
from app.models.site import Site
from app.models.tag import Tag
from app.models.user import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post, Category=Category, Page=Page, Tag=Tag, Comment=Comment,
                Site=Site)


if __name__ == '__main__':
    app.run()
