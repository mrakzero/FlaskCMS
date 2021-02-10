# -*- coding: utf-8 -*-
import enum

from app import db


class Site(db.Model):
    __tablename__ = 't_site'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    keywords = db.Column(db.String(256), comment='keywords')
    description = db.Column(db.String(512), comment='description')

    def __repr__(self):
        return '<Site %r>' % self.name
