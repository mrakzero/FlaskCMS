# -*- coding: utf-8 -*-
import enum

from app import db


class UserStatus(enum.Enum):
    normal = 0
    frozen = 1


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
