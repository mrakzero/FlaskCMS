# -*- coding: utf-8 -*-
# File: user_management.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:26
from flask import Blueprint, flash, redirect, url_for, render_template

from app import db
from app.forms.user import UserForm, LoginForm, RegisterForm
from app.models.user import User

bp_admin_user = Blueprint('admin_user', __name__, url_prefix='/admin', template_folder='../templates/admin',
                          static_folder='../static')


@bp_admin_user.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user = get_user_info(register_form)
        if db.session.query(User).filter(User.username == user.username).all():
            return render_template('admin/register.html', register_form=register_form)
        else:
            db.session.add(user)
            db.session.commit()
            flash('Post created.', 'success')
            return redirect(url_for('cms.index'))
    return render_template('admin/register.html', register_form=register_form)


@bp_admin_user.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('admin_index'))
    return render_template('admin/login.html', login_form=login_form)


@bp_admin_user.route('/logout', methods=['GET', 'POST'])
def logout():
    pass


# 从表单中获取post信息
def get_user_info(form):
    username = form.username.data
    nickname = form.nickname.data
    password = form.password.data
    email = form.email.data

    user = User(
        username=username,
        nickname=nickname,
        password=password,
        email=email,
    )

    return user
