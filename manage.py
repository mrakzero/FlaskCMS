# -*- coding: utf-8 -*-

import os

from mako.parsetree import Tag

from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app.models.page import Page
from app.models.post import Post, Category
from app.models.site import Site
from app.models.user import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post, Category=Category, Page=Page, Tag=Tag, Site=Site)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
