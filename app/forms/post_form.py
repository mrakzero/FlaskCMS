# -*- coding: utf-8 -*-
# File: post_resource.py
# Author: Zhangzhijun
# Date: 2021/2/12 22:06
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length

from app.models.post import Category


class PostForm(FlaskForm):
    title = StringField('标题', validators=[Length(min=1, max=65, message='标题长度为1~64位'), DataRequired(message='标题不能为空')])
    slug = StringField('别名', validators=[Length(min=1, max=65, message='别名长度为6~12位'), DataRequired(message='别名不能为空')])
    excerpt = TextAreaField('摘要', validators=[DataRequired()])
    content = CKEditorField('内容', validators=[DataRequired(message='内容不能为空')])
    categoryid = SelectField('分类', validators=[DataRequired()])
    status = RadioField('状态', validators=[DataRequired()])
    tag = StringField('标签', validators=[DataRequired()])
    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.categoryid.choices = [(category.id, category.name)
                                   for category in Category.query.order_by(Category.name).all()]

        self.status.choices = [(True, u'立即发布'), (False, u'保存草稿')]
