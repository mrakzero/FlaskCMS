# -*- coding: utf-8 -*-
# File: user.py
# Author: Zhangzhijun
# Date: 2021/2/12 22:43
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, PasswordField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length

from app.models.user import User, Role


class UserForm(FlaskForm):
    username = StringField(u'用户名',
                           validators=[Length(min=1, max=64, message='账号长度为1~64位'), DataRequired(message='用户名不能为空')])
    nickname = StringField(u'昵称',
                           validators=[Length(min=1, max=64, message='昵称长度为1~64位'), DataRequired(message='用户别名不能为空')])
    password = PasswordField(u'密码',
                             validators=[Length(min=8, max=256, message='密码长度为8~16位'), DataRequired(message='密码不能为空')])
    email = TextAreaField(u'邮箱',
                          validators=[Length(min=8, max=128, message='邮箱长度为8~128位'), DataRequired(message='邮箱不能为空')])
    roleid = SelectField(u'角色', validators=[DataRequired()])
    status = IntegerField(u'用户状态', validators=[DataRequired()])
    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.roleid.choices = [(role.id, role.name)
                               for role in Role.query.order_by(Role.name).all()]


class RegisterForm(FlaskForm):
    username = StringField(u'用户名',
                           validators=[Length(min=1, max=64, message='账号长度为1~64位'), DataRequired(message='用户名不能为空')])
    nickname = StringField(u'昵称',
                           validators=[Length(min=1, max=64, message='昵称长度为1~64位'), DataRequired(message='用户别名不能为空')])
    password = PasswordField(u'密码',
                             validators=[Length(min=8, max=256, message='密码长度为8~16位'), DataRequired(message='密码不能为空')])
    email = TextAreaField(u'邮箱',
                          validators=[Length(min=8, max=128, message='邮箱长度为8~128位'), DataRequired(message='邮箱不能为空')])
    submit = SubmitField(u'注册')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)


class LoginForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField(u'记住我')
    submit = SubmitField(u'登录')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
