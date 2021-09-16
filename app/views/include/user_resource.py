# -*- coding: utf-8 -*-
# File: user_resource.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:26
from flask import Blueprint, flash, redirect, url_for, render_template, jsonify, current_app
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_restful import fields, reqparse, Resource
from werkzeug.security import generate_password_hash

from app import db, login_manager
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.models.user import User, Role
from app.utils import query_to_dict


class UserResource():
    def register(self, user):

        if (User.query.filter_by(username=user.username() > 0)):
            return jsonify(code=ResponseCode.USER_ALREADY_EXIST, message=ResponseMessage.USER_ALREADY_EXIST)

        u = User(
            username=user.username,
            nickname=user.nickname,
            password_hash=generate_password_hash(user.password),
            email=user.email
        )
        db.session.add(u)
        db.session.commit()
        flash('Post created.', 'success')
        data = dict(code=ResponseCode.CREATE_CATEGORY_SUCCESS, message=ResponseMessage.CREATE_CATEGORY_SUCCESS)
        return jsonify(data)

    def login(self, user):

        username = user.username,
        password = user.password,

        user = User.query.first()
        # 验证用户名和密码是否一致
        if username == user.username and user.validate_password(password):
            login_user(user)  # 登入用户
            data = dict(code=ResponseCode.LOGIN_SUCCESS, message=ResponseMessage.LOGIN_SUCCESS)
            return jsonify(data)
        else:
            data = dict(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)
            return jsonify(data)

    @login_required
    def logout(self):
        logout_user()  # 登出用户
        data = dict(code=ResponseCode.LOGOUT_SUCCESS, message=ResponseMessage.LOGOUT_SUCCESS)
        return jsonify(data)

    def get_users(self):
        try:
            users = db.session.query(User.id, User.username, User.nickname, Role.code, User.email, User.registertime,
                                     User.status) \
                .filter(User.roleid == Role.id) \
                .all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if users is None:
            return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)

        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(users))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    def get_user_by_name(self, username):
        try:
            user = db.session.query(User.id, User.username, User.nickname, Role.code, User.email, User.registertime,
                                    User.status) \
                .filter(User.username == username) \
                .filter(User.roleid == Role.id) \
                .first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if user is None:
            return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(user))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    @login_required
    def update_user(self, user):

        try:
            u = User.query.filter_by(username=user.username).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if u is None:
            return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)

        u.username = user.username,
        u.nickname = user.nickname,
        u.email = user.email

        db.session.commit()
        data = dict(code=ResponseCode.UPDATE_USER_SUCCESS, message=ResponseMessage.UPDATE_USER_SUCCESS)
        return jsonify(data)

    @login_required
    def delete_user(self, username):
        try:
            user = User.query.filter_by(username=username).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if user is None:
            return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)

        db.session.delete(user)
        db.session.commit()
        flash('Category deleted.', 'success')

        date = dict(code=ResponseCode.DELETE_USER_SUCCESS, message=ResponseMessage.DELETE_USER_SUCCESS)
        return jsonify(date)
