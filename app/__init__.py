# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from config import config

# 由于尚未初始化所需的程序实例，所以没有初始化扩展，创建扩展类时没有向构造函数传入参数。

mail = Mail()
db = SQLAlchemy()


def create_app(config_name):
    '''工厂函数'''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)  # 通过config.py统一接口
    mail.init_app(app)  # 同上
    db.init_app(app)  # 同上

    # 附加路由和自定义错误页面，将蓝本注册到工厂函数
    from app.views.admin import dashboard, post_management, page_management, comment_management, media_management, \
        user_management, setting
    from app.views.cms import index, category, page, post

    app.register_blueprint(index.bp_cms_index)
    app.register_blueprint(category.bp_cms_category)
    app.register_blueprint(post.bp_cms_post)
    app.register_blueprint(page.bp_cms_page)

    app.register_blueprint(dashboard.bp_admin_index)
    app.register_blueprint(post_management.bp_admin_post)
    app.register_blueprint(page_management.bp_admin_page)
    app.register_blueprint(media_management.bp_admin_media)
    app.register_blueprint(user_management.bp_admin_user)
    app.register_blueprint(setting.bp_admin_setting)

    return app
