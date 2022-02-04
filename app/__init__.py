# -*- coding: utf-8 -*-
import logging
import logging.config

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf import CSRFProtect

from config import config, logger_conf

# 由于尚未初始化所需的程序实例，所以没有初始化扩展，创建扩展类时没有向构造函数传入参数。

mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app(config_name):
    """
    工厂函数
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)  # 通过config.py统一接口
    mail.init_app(app)  # 同上
    db.init_app(app)  # 同上

    # logging config
    logging.config.dictConfig(logger_conf)

    # 设置登录安全级别
    login_manager.session_protection = 'strong'
    login_manager.init_app(app)
    # 配置CKEditor
    app.config['CKEDITOR_SERVE_LOCAL'] = True  # 使用CKEditor本地资源
    app.config['CKEDITOR_PKG_TYPE'] = 'basic'  # 3种类型：basic, standard and full
    app.config['CKEDITOR_LANGUAGE'] = 'zh'  # CKEditro 语言
    app.config['CKEDITOR_ENABLE_CODESNIPPET '] = True  # 代码高亮
    app.config['CKEDITOR_FILE_UPLOADER'] = '/media'  #
    app.config['CKEDITOR_ENABLE_CSRF'] = False  # 禁用CSRF保护
    csrf.init_app(app)
    # 配置分页
    app.config['POST_PER_PAGE'] = 10

    # 配置restful api
    # from app.api.v1 import api, registerResources
    # registerResources()
    # api.init_app(app)

    # 若使用Jija2模板，请打开蓝图的注释
    # 附加路由和自定义错误页面，将蓝本注册到工厂函数
    from app.views.admin import bp_admin
    from app.views.cms import bp_cms

    app.register_blueprint(bp_admin)
    app.register_blueprint(bp_cms)

    return app
