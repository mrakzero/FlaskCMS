# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from app.views.admin import index, post

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
    # app.register_blueprint(cms.index.bp_cms_index)
    app.register_blueprint(index.bp_admin_index)
    app.register_blueprint(post.bp_admin_post)

    return app
