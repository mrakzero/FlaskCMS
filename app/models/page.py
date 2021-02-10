# -*- coding: utf-8 -*-
import enum

from app import db


class PageStatus(enum.Enum):
    published = 0
    draft = 1


class Page(db.Model):
    __tablename__ = 't_page'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False, index=True)
    slug = db.Column(db.String(64), nullable=False, unique=True)
    authorid = db.Column(db.Integer, db.ForeignKey('t_user.id'))
    content = db.Column(db.Text)
    publishtime = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间')
    updatetime = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), comment='修改时间')
    status = db.Column(db.Enum(PageStatus), default=PageStatus.draft)

    def __repr__(self):
        return '<Page %r>' % self.title
