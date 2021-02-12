# -*- coding: utf-8 -*-
# File: user.py
# Author: Zhangzhijun
# Date: 2021/2/12 22:43
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length

from app.models.user import User, Role


class UserForm(FlaskForm):
    login = StringField('标题', validators=[Length(min=1, max=64, message='账号长度为1~64位'), DataRequired(message='用户名不能为空')])
    nickname = StringField('别名',
                           validators=[Length(min=1, max=64, message='昵称长度为1~64位'), DataRequired(message='用户别名不能为空')])
    password = PasswordField('作者', validators=[Length(min=8, max=256, message='密码长度为8~16位'), DataRequired(message='密码不能为空')])
    email = TextAreaField('摘要', validators=[Length(min=8, max=128, message='邮箱长度为8~128位'), DataRequired(message='邮箱不能为空')])
    roleid = SelectField('内容', validators=[DataRequired()])
    status = IntegerField('状态', validators=[DataRequired()])
    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.roleid.choices = [(role.id, role.name)
                               for role in Role.query.order_by(Role.name).all()]
