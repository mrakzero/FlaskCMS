# -*- coding: utf-8 -*-
# File: site_resource.py
# Author: Zhangzhijun
# Date: 2021/2/12 23:01
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length

from app.models.user import User


class PostForm(FlaskForm):
    name = StringField('站点标题',
                       validators=[Length(min=1, max=64, message='站点标题长度为1~64位'), DataRequired(message='站点标题不能为空')])
    keywords = StringField('网站关键字',
                           validators=[Length(min=1, max=256, message='关键字长度为1~64位'), DataRequired(message='关键字不能为空')])
    description = StringField('网站描述',
                              validators=[Length(min=1, max=256, message='描述长度为1~64位'), DataRequired(message='描述不能为空')])

    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
