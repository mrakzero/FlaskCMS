# -*- coding: utf-8 -*-
import enum

from app import db


class Site(db.Model):
    __tablename__ = 't_site'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True, comment='站点标题')
    keywords = db.Column(db.String(256), comment='关键字')
    description = db.Column(db.String(512), comment='描述')

    def __init__(self, name, keywords, description):
        self.name = name
        self.keywords = keywords
        self.description = description

    def __repr__(self):
        return '<Site %r>' % self.name
