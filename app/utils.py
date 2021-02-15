# -*- coding: utf-8 -*-
# File: utils.py
# Author: Zhangzhijun
# Date: 2021/2/15 11:41
from werkzeug.security import generate_password_hash

from app import db
from app.models.post import Category, Post
from app.models.user import Role, User


def add_default_data():
    # 实例化ROM对象
    # 添加默认角色
    administrator = Role("管理员", "管理员拥有全部权限")
    editor = Role("编辑", "可以对文章、标签、分类、页面、友情链接、评论进行管理")
    author = Role("作者", "所发表的文章无需管理员审核即可显示，还可以编辑已通过审核的文章，并且拥有媒体库的使用权限")
    contributor = Role("投稿者", "可以发表或删除自己的文章，但所发文章需经管理员审核后才能在博客上显示")
    subscriber = Role("订阅者", "只允许修改自己的个人资料，例如昵称、联系方式、密码等等")
    if Role.query.filter_by(name='管理员') or Role.query.filter_by(name='编辑') or Role.query.filter_by(
            name='作者') or Role.query.filter_by(name='投稿者') or Role.query.filter_by(name='订阅者'):
        pass
    else:
        db.session.add(administrator)
        db.session.add(editor)
        db.session.add(author)
        db.session.add(contributor)
        db.session.add(subscriber)

    # 添加默认管理员
    admin = User('admin', 'administrator', 'admin.123', 'admin@flaskcms.com')
    if User.query.filter_by(username='admin'):
        pass
    else:
        db.session.add(admin)

    # 添加默认文章分类
    default_category = Category('未分类', '文章默认分类')
    if Category.query.filter_by(name='未分类'):
        pass
    else:
        db.session.add(default_category)

    # 添加默认文章
    default_post = Post('欢迎使用FlaskCMS', 'welcome_to_use_flaskcms', '1', '欢迎使用FlaskCMS', '欢迎使用FlaskCMS', '1', '1',
                        'FlaskCMS')
    if Post.query.filter_by(title='欢迎使用FlaskCMS'):
        pass
    else:
        db.session.add(default_post)

    db.session.commit()


@staticmethod
def generate_user_password_hash(password):
    if password == '':
        return 0
    else:
        return generate_password_hash(password)
