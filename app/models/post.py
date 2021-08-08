# -*- coding: utf-8 -*-
import enum

from flask_login import current_user

from app import db
from app.models.category import Category
from app.models.user import User

t_post_tag = db.Table('t_post_tag',
                      db.Column('id', db.Integer, autoincrement=True, primary_key=True),
                      db.Column('tagid', db.Integer, db.ForeignKey('t_tag.id'), primary_key=True),
                      db.Column('postid', db.Integer, db.ForeignKey('t_post.id'), primary_key=True)
                      )


# t_post_comment = db.Table('t_post_comment',
#                           db.Column('id', db.Integer, autoincrement=True, primary_key=True),
#                           db.Column('commentid', db.Integer, db.ForeignKey('t_comment.id'), primary_key=True),
#                           db.Column('postid', db.Integer, db.ForeignKey('t_post.id'), primary_key=True)
#                           )


class Post(db.Model):
    __tablename__ = 't_post'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(64), nullable=False, index=True, comment='文章标题')
    slug = db.Column(db.String(64), nullable=False, unique=True, comment='标题别名')
    authorid = db.Column(db.Integer, db.ForeignKey('t_user.id'), comment='作者ID')
    excerpt = db.Column(db.Text, comment='摘要')
    content = db.Column(db.Text, comment='内容')
    categoryid = db.Column(db.Integer, db.ForeignKey('t_category.id'), comment='分类ID')
    image = db.Column(db.String(500), nullable=True, comment='图片')
    publishtime = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间')
    updatetime = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), comment='修改时间')
    counter = db.Column(db.Integer, comment='阅读计数')
    tag = db.relationship('Tag', secondary=t_post_tag, backref=db.backref('t_post'), lazy='dynamic')
    status = db.Column(db.Boolean, default=True, comment='文章状态')
    comment = db.relationship('Comment', backref=db.backref('t_post'), lazy='dynamic')

    def __init__(self, **kwargs):
        super(Post, self).__init__(**kwargs)

    def set_category(self):
        """使劲儿中文章默认分类为未分类"""
        if self.categoryid is None:
            category = Category.query.filter_by(name='未分类').first()
            self.categoryid = category.id
            db.session.commit()

    def set_author(self):
        """设置文章作者"""
        if current_user.id() is None:
            author = User.query.filter_by(username='admin').first()
            self.authorid = author.id
            db.session.commit()

    def set_excerpt(self):
        """设置文章摘要默认为文章前500个字符"""
        if self.excerpt is None:
            excerpt = self.content[:500].strip()
            self.excerpt = excerpt
            db.session.commit()

    @staticmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @staticmethod
    def get_by_title(cls, title):
        return cls.query.fiflter_by(title=title).first()

    @staticmethod
    def get_by_category(cls, categoryid):
        return cls.query.filter_by(categoryid=categoryid)

    @staticmethod
    def get_by_authror(cls, authroid):
        return cls.query.filter_by(authorid=authroid)

    @staticmethod
    def get_by_tag(cls, tagid):
        return cls.query.filter_by(tagid=tagid)

    @staticmethod
    def page(page_num, per_page):
        return Post.query.paginate(page_num, per_page, False)

    @staticmethod
    def get_by_category(category):
        return Post.query.filter_by(category=category)

    def verify_post_author(self, user_id):
        if user_id == self.author_id:
            return True
        else:
            return False

    def __repr__(self):
        return '<Post %r>' % self.title
