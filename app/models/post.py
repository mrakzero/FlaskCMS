# -*- coding: utf-8 -*-
import enum

from app import db


class PostStatus(enum.Enum):
    published = 0
    draft = 1


class Category(db.Model):
    __tablename__ = 't_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    slug = db.Column(db.String(64), nullable=False, unique=True)
    description = db.Column(db.String(256))

    def __repr__(self):
        return '<Category %r>' % self.name


class Post(db.Model):
    __tablename__ = 't_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False, index=True)
    slug = db.Column(db.String(64), nullable=False, unique=True)
    authorid = db.Column(db.Integer, db.ForeignKey('t_user.id'))
    excerpt = db.Column(db.Text)
    content = db.Column(db.Text)
    categoryid = db.Column(db.Integer, db.ForeignKey('t_category.id'))
    publishtime = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间')
    updatetime = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), comment='修改时间')
    tag = db.Column(db.Text)
    status = db.Column(db.Enum(PostStatus), default=PostStatus.draft)

    def __repr__(self):
        return '<Post %r>' % self.title
