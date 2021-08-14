# -*- coding: utf-8 -*-
# File: user.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:26
from flask import Blueprint, flash, redirect, url_for, render_template, jsonify, current_app
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_restful import fields, reqparse, Resource
from werkzeug.security import generate_password_hash

from app import db, login_manager
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.models.user import User
from app.utils import serialize

PARSER_ARGS_STATUS = True

resource_fields = {
    'id': fields.String,
    'username': fields.String,
    'nickname': fields.String,
    'email': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, required=False, trim=True, location=[u'json', u'form', u'args', u'values'])
parser.add_argument('username', type=str, required=False, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入用户名')
parser.add_argument('nickname', type=str, required=False, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入昵称')
parser.add_argument('password', type=int, trim=False, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入密码')
parser.add_argument('email', type=str, required=False, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入邮箱号')


class UserRegisterResource(Resource):
    def post(self):
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)

        if (User.query.filter_by(username=args.username() > 0)):
            return jsonify(code=ResponseCode.USER_ALREADY_EXIST, message=ResponseMessage.USER_ALREADY_EXIST)

        user = User(
            username=args.username,
            nickname=args.nickname,
            password_hash=generate_password_hash(args.password),
            email=args.email
        )
        db.session.add(user)
        db.session.commit()
        flash('Post created.', 'success')
        data = dict(code=ResponseCode.CREATE_CATEGORY_SUCCESS, message=ResponseMessage.CREATE_CATEGORY_SUCCESS)
        return jsonify(data)


class UserLoginResource(Resource):
    def post(self):
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)
        username = args.username,
        password = args.password,

        user = User.query.first()
        # 验证用户名和密码是否一致
        if username == user.username and user.validate_password(password):
            login_user(user)  # 登入用户
            data = dict(code=ResponseCode.LOGIN_SUCCESS, message=ResponseMessage.LOGIN_SUCCESS)
            return jsonify(data)
        else:
            data = dict(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)
            return jsonify(data)


class UserlogoutResource(Resource):
    @login_required
    def get(self):
        logout_user()  # 登出用户
        data = dict(code=ResponseCode.LOGOUT_SUCCESS, message=ResponseMessage.LOGOUT_SUCCESS)
        return jsonify(data)


class UserListResource(Resource):
    def get(self):
        try:
            users = User.query.all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if users is None:
            return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)

        # data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(users))
        # current_app.logger.debug("data: %s", data)
        # return jsonify(data)
        return users


class UserResource(Resource):
    def get(self, username):
        try:
            user = User.query.filter_by(username=username).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if user is None:
            return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)
        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(user))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    @login_required
    def put(self, username):
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)

        try:
            user = User.query.filter_by(username=username).first()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if user is None:
            return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)

        user.username = args.username,
        user.nickname = args.nickname,
        user.email = args.email

        db.session.commit()
        data = dict(code=ResponseCode.UPDATE_USER_SUCCESS, message=ResponseMessage.UPDATE_USER_SUCCESS)
        return jsonify(data)

    @login_required
    def delete(self, username):
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
