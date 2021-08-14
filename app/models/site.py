# -*- coding: utf-8 -*-
import enum

from app import db


class Site(db.Model):
    __tablename__ = 't_site'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    site_name = db.Column(db.String(64), nullable=False, index=True, comment='网站名称')
    domain = db.Column(db.String(128), nullable=False, comment='网站域名')
    keywords = db.Column(db.String(256), comment='META关键字')
    description = db.Column(db.String(512), comment='MWTA描述')


    def __init__(self, **kwargs):
        super(Site, self).__init__(**kwargs)
        
    def __repr__(self):
        return '<Site %r>' % self.name
