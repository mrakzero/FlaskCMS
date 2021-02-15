# -*- coding: utf-8 -*-
import enum

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class UserStatus(enum.Enum):
    normal = 0
    frozen = 1


class User(db.Model, UserMixin):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, comment='用户id')
    username = db.Column(db.String(64), unique=True, index=True, comment='登录名')
    nickname = db.Column(db.String(64), nullable=False, unique=True, comment='用户昵称')
    password_hash = db.Column(db.String(256), nullable=False, comment='密码')
    email = db.Column(db.String(128), nullable=False, unique=True, comment='邮件')
    roleid = db.Column(db.Integer, db.ForeignKey('t_role.id'), comment='角色ID')
    role = db.relationship('Role', backref=db.backref('t_user', lazy='dynamic'))
    registertime = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间')
    status = db.Column(db.Enum(UserStatus), default=UserStatus.normal, comment='用户状态')

    def __init__(self, username, nickname, password, email):
        self.username = username
        self.nickname = nickname
        self.password = password
        self.email = email

    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 返回布尔值

    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 't_role'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, comment='角色ID')
    name = db.Column(db.String(64), unique=True, index=True, comment='角色名称')
    description = db.Column(db.String(256), comment='角色描述')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Role %r>' % self.name
