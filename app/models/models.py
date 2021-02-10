# -*- coding: utf-8 -*-
import enum

from app import db


class UserStatus(enum.Enum):
    normal = 0
    frozen = 1


class PostStatus(enum.Enum):
    published = 0
    draft = 1


class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, comment='用户id')
    login = db.Column(db.String(64), unique=True, index=True)
    nickname = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('t_role.id'))
    registertime = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间')
    status = db.Column(db.Enum(UserStatus), default=UserStatus.normal)

    def __repr__(self):
        return '<User %r>' % self.login


class Role(db.Model):
    __tablename__ = 't_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    description = db.Column(db.String(256))

    def __repr__(self):
        return '<Role %r>' % self.name


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


class Page(db.Model):
    __tablename__ = 't_page'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False, index=True)
    slug = db.Column(db.String(64), nullable=False, unique=True)
    authorid = db.Column(db.Integer, db.ForeignKey('t_user.id'))
    content = db.Column(db.Text)
    publishtime = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间')
    updatetime = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), comment='修改时间')
    status = db.Column(db.Enum(PostStatus), default=PostStatus.draft)

    def __repr__(self):
        return '<Page %r>' % self.title


class Tag(db.Model):
    __tablename__ = 't_tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)

    def __repr__(self):
        return '<Tag %r>' % self.name


class Site(db.Model):
    __tablename__ = 't_site'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    keywords = db.Column(db.String(256), comment='keywords')
    description = db.Column(db.String(512), comment='description')

    def __repr__(self):
        return '<Site %r>' % self.name
