# -*- coding: utf-8 -*-
# File: post_forms.py
# Author: Zhangzhijun
# Date: 2021/2/12 22:06
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length

from app.models.post import Category
from app.models.user import User


class PostForm(FlaskForm):
    title = StringField('标题', validators=[Length(min=1, max=64, message='标题长度为1~64位'), DataRequired(message='用户名不能为空')])
    slug = StringField('别名', validators=[Length(min=1, max=64, message='别名长度为6~12位'), DataRequired(message='用户名不能为空')])
    authorid = SelectField('作者', validators=[DataRequired()])
    excerpt = TextAreaField('摘要', validators=[DataRequired()])
    content = TextAreaField('内容', validators=[DataRequired()])
    categoryid = SelectField('分类', coerce=int, default=1)
    status = SelectField('状态', coerce=int, default=1)
    tag = StringField('标签', validators=[DataRequired()])
    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.categoryid.choices = [(category.id, category.name)
                                   for category in Category.query.order_by(Category.name).all()]
        self.authorid.choices = [(author.id, author.name)
                                 for author in User.query.order_by(User.login).all()]