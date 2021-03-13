#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version: 1.0.0
# author:Zhang Zhijun
# time: 2021-03-13
# file: category.py
# function:
# modify:
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length

from app.models.category import Category


class CategoryForm(FlaskForm):
    title = StringField('标题', validators=[Length(min=1, max=64, message='标题长度为1~64位'), DataRequired(message='标题不能为空')])
    slug = StringField('别名', validators=[Length(min=1, max=64, message='别名长度为6~12位'), DataRequired(message='别名不能为空')])
    parentid = SelectField('父分类', validators=[DataRequired()])
    description = StringField('描述', validators=[Length(min=1, max=64, message='描述长度为1-64位')])

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.parentid.choices = [(category.id, category.name)
                                 for category in Category.query.order_by(Category.name).all()]
