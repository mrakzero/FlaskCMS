# -*- coding: utf-8 -*-
import enum

from app import db

t_post_tag = db.Table('t_post_tag',
                      db.Column('tagid', db.Integer, db.ForeignKey('t_tag.id')),
                      db.Column('postid', db.Integer, db.ForeignKey('t_post.id'))
                      )


class PostStatus(enum.Enum):
    published = 0
    draft = 1


class Category(db.Model):
    __tablename__ = 't_category'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True, comment='分类名称')
    slug = db.Column(db.String(64), nullable=False, unique=True, comment='分类别名')
    description = db.Column(db.String(256), comment='分类描述')
    post = db.relationship('Post', backref=db.backref('t_category', lazy='dynamic'))

    def __repr__(self):
        return '<Category %r>' % self.name


class Post(db.Model):
    __tablename__ = 't_post'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(64), nullable=False, index=True, comment='文章标题')
    slug = db.Column(db.String(64), nullable=False, unique=True, comment='标题别名')
    authorid = db.Column(db.Integer, db.ForeignKey('t_user.id'), comment='作者ID')
    excerpt = db.Column(db.Text, comment='摘要')
    content = db.Column(db.Text, comment='内容')
    categoryid = db.Column(db.Integer, db.ForeignKey('t_category.id'), comment='分类ID')
    publishtime = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间')
    updatetime = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), comment='修改时间')
    counter = db.Column(db.Integer, comment='阅读计数')
    tag = db.relationship('Tag', secondary=t_post_tag, backref=db.backref('t_post', lazy='dynamic'))
    status = db.Column(db.Enum(PostStatus), default=PostStatus.draft, comment='文章状态')
    comment = db.relationship('Comment', backref='Post', lazy='dynamic')

    def __init__(self, title, slug, authorid, excerpt, content, categoryid, status, tag):
        self.title = title
        self.slug = slug
        self.authorid = authorid
        self.excerpt = excerpt
        self.content = content
        self.categoryid = categoryid
        self.status = status
        self.tag = tag

    def __repr__(self):
        return '<Post %r>' % self.title


class Tag(db.Model):
    __tablename__ = 't_tag'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True, comment='标签名')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag %r>' % self.name
