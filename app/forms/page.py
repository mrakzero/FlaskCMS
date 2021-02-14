# -*- coding: utf-8 -*-
# File: page.py
# Author: Zhangzhijun
# Date: 2021/2/12 22:56
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length

from app.models.user import User


class PostForm(FlaskForm):
    title = StringField('标题', validators=[Length(min=1, max=64, message='标题长度为1~64位'), DataRequired(message='标题不能为空')])
    slug = StringField('别名', validators=[Length(min=1, max=64, message='别名长度为6~12位'), DataRequired(message='别名不能为空')])
    authorid = SelectField('作者', validators=[DataRequired()])
    content = TextAreaField('内容', validators=[DataRequired(message='内容不能为空')])
    status = IntegerField('状态', validators=[DataRequired()])
    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.authorid.choices = [(author.id, author.name)
                                 for author in User.query.order_by(User.username).all()]
