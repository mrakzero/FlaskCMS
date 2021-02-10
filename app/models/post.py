# -*- coding: utf-8 -*-
import enum

from app import db

tags = db.Table('t_post_tag',
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
    category = db.relationship('Category', backref=db.backref('t_post', lazy='dynamic'))
    publishtime = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间')
    updatetime = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), comment='修改时间')
    counter = db.Column(db.Integer, comment='阅读计数')
    tag = db.relationship('Tag', secondary=tags, backref=db.backref('t_post', lazy='dynamic'))
    status = db.Column(db.Enum(PostStatus), default=PostStatus.draft, comment='文章状态')

    def __repr__(self):
        return '<Post %r>' % self.title


class Tag(db.Model):
    __tablename__ = 't_tag'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True, comment='标签名')

    def __repr__(self):
        return '<Tag %r>' % self.name
