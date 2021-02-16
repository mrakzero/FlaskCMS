# -*- coding: utf-8 -*-
# File: init_project.py
# Author: Zhangzhijun
# Date: 2021/2/16 16:00
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash

from app import db
from app.models.comment import Comment
from app.models.post import Post
from app.models.user import Role, Permission, User

# add default permission
print("add default permission!")
all_rights = Permission('all_rights', '所有权限')

# add default Roles
print("add default roles!")
administrator = Role("administrator", "管理员", "管理员拥有全部权限")
editor = Role("editor", "编辑", "可以对文章、标签、分类、页面、友情链接、评论进行管理")
author = Role("author", "作者", "所发表的文章无需管理员审核即可显示，还可以编辑已通过审核的文章，并且拥有媒体库的使用权限")
contributor = Role("contributor", "投稿者", "可以发表或删除自己的文章，但所发文章需经管理员审核后才能在博客上显示")
subscriber = Role("subscriber", "订阅者", "只允许修改自己的个人资料，例如昵称、联系方式、密码等等")

# add default User
print("add default user!")
admin = User(username='admin', nickname='管理员', password_hash=generate_password_hash('admin.123'), email='admin@flaskcms.com')

# add default Post
print("add default Post!")
# default_post = Post(title='开启FlaskCMS之旅', slug='Beging wiht FlaskCMS', content='这是Flask CMS的第一篇文章！')

# add default Post
print("add default Comment!")
# default_comment = Comment('admin', "这是FlaskCMS的第一条评论！")

db.session.add(all_rights)
db.session.add(administrator)
db.session.add(editor)
db.session.add(author)
db.session.add(contributor)
db.session.add(subscriber)
db.session.add(admin)
# db.session.add(default_post)
db.session.commit()
