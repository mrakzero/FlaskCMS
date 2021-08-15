# -*- coding: utf-8 -*-
import datetime
import enum

from flask_login import UserMixin
from sqlalchemy import text
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class UserStatus(enum.Enum):
    normal = 0
    frozen = 1


t_role_permission = db.Table('t_role_permission',
                             db.Column('id', db.Integer, autoincrement=True, primary_key=True),
                             db.Column('roleid', db.Integer, db.ForeignKey('t_role.id'), index=True),
                             db.Column('permissionid', db.Integer, db.ForeignKey('t_permission.id'), index=True)
                             )


class Permission(db.Model):
    __tablename__ = 't_permission'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(21), unique=True)
    description = db.Column(db.String(64), nullable=True)
    role = db.relationship('Role', secondary='t_role_permission', backref=db.backref('t_role'), lazy='dynamic')

    def __init__(self, **kwargs):
        super(Permission, self).__init__(**kwargs)

    def set_default_permission(self):
        # todo
        pass

    def __repr__(self):
        return '<Permission %r>' % self.name


class Role(db.Model):
    __tablename__ = 't_role'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, comment='角色ID')
    code = db.Column(db.String(64), unique=True, index=True, comment='角色代码')
    name = db.Column(db.String(64), unique=True, comment='角色名称')
    description = db.Column(db.String(256), comment='角色描述')
    user = db.relationship('User', backref=db.backref('t_role'), lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model, UserMixin):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, comment='用户id')
    username = db.Column(db.String(64), unique=True, index=True, comment='登录名')
    nickname = db.Column(db.String(64), nullable=False, unique=True, comment='用户昵称')
    password_hash = db.Column(db.String(256), nullable=False, comment='密码')
    email = db.Column(db.String(128), nullable=False, unique=True, comment='邮件')
    roleid = db.Column(db.Integer, db.ForeignKey('t_role.id'), comment='角色ID')
    registertime = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间')
    status = db.Column(db.Boolean, server_default=text('1'), comment='用户状态')
    post = db.relationship('Post', backref=db.backref('t_user'), lazy='dynamic')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def set_password(self, password):
        """用来设置密码的方法，接受密码作为参数,将生成的密码保持到对应字段"""
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        """用于验证密码的方法，接受密码作为参数, 返回布尔值"""
        return check_password_hash(self.password_hash, password)

    def set_role(self):
        """为用户设置角色,默认为user"""
        if self.role is None:
            role = Role.query.filter_by(code='subscriber').first()
            self.role = role
            db.session.commit()

    @property
    def get_status(self):
        return self.status

    def __repr__(self):
        return '<User %r>' % self.username
