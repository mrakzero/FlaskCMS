# -*- coding: utf-8 -*-
import enum

from app import db


class PageStatus(enum.Enum):
    published = 0
    draft = 1


class Page(db.Model):
    __tablename__ = 't_page'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(64), nullable=False, index=True, comment='页面标题')
    slug = db.Column(db.String(64), nullable=False, unique=True, comment='页面别名')
    authorid = db.Column(db.Integer, db.ForeignKey('t_user.id'), comment='作者ID')
    content = db.Column(db.Text, comment='内容')
    publishtime = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间')
    updatetime = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), comment='修改时间')
    status = db.Column(db.Enum(PageStatus), default=PageStatus.draft, comment='页面状态')

    def __repr__(self):
        return '<Page %r>' % self.title
