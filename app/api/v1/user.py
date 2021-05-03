# -*- coding: utf-8 -*-
# File: user.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:26
from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash

from app import db, login_manager
from app.forms.user import UserForm, LoginForm, RegisterForm
from app.models.user import User

bp_admin_user = Blueprint('admin_user', __name__, url_prefix='/admin', template_folder='../templates/admin',
                          static_folder='../static')


@bp_admin_user.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user = get_user_info(register_form)
        if db.session.query(User).filter(User.username == user.username).count() > 0:
            flash('Username has exist.', 'failed')
            return render_template('admin/register.html', register_form=register_form)
        elif db.session.query(User).filter(User.email == user.email).count() > 0:
            flash('Email has exist.', 'failed')
            return render_template('admin/register.html', register_form=register_form)
        else:
            db.session.add(user)
            db.session.commit()
            flash('注册成功！', 'success')
            return redirect(url_for('index'))
    return render_template('admin/register.html', register_form=register_form)


@bp_admin_user.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user = User.query.first()
        # 验证用户名和密码是否一致
        if username == user.username and user.validate_password(password):
            login_user(user)  # 登入用户
            flash('Login success.')
            return redirect(url_for('admin_index'))
    return render_template('admin/login.html', login_form=login_form)


@bp_admin_user.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()  # 登出用户
    flash('Goodbye.')
    return redirect(url_for('index'))  # 重定向回首页


# 从表单中获取post信息
def get_user_info(form):
    username = form.username.data
    nickname = form.nickname.data
    password = form.password.data
    email = form.email.data
    print(generate_password_hash(password))
    user = User(
        username=username,
        nickname=nickname,
        password_hash=generate_password_hash(password),
        email=email,
    )

    return user


@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    return user  # 返回用户对象
