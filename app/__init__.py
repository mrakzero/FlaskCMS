# -*- coding: utf-8 -*-
import logging

from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf import CSRFProtect


from config import config

# 由于尚未初始化所需的程序实例，所以没有初始化扩展，创建扩展类时没有向构造函数传入参数。

mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()  # CKEditor CSRF
api = Api()  # restful api


def create_app(config_name):
    """
    工厂函数
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)  # 通过config.py统一接口
    mail.init_app(app)  # 同上
    db.init_app(app)  # 同上

    from app.api.v1.resourceList import loadResources
    loadResources()
    api.init_app(app)

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

    # 附加路由和自定义错误页面，将蓝本注册到工厂函数
    # import app.views.admin.index as admin_index
    # import app.views.admin.post as admin_post
    # import app.views.admin.category as admin_category
    # import app.views.admin.page as admin_page
    # import app.views.admin.media as admin_media
    # import app.views.admin.setting as admin_setting
    # import app.views.admin.user as admin_user
    #
    # import app.views.cms.index as cms_index
    # import app.views.cms.post as cms_post
    # import app.views.cms.category as cms_category
    # import app.views.cms.page as cms_page
    #
    # app.register_blueprint(cms_index.bp_cms_index)
    # app.register_blueprint(cms_category.bp_cms_category)
    # app.register_blueprint(cms_post.bp_cms_post)
    # app.register_blueprint(cms_page.bp_cms_page)
    #
    # app.register_blueprint(admin_index.bp_admin_index)
    # app.register_blueprint(admin_post.bp_admin_post)
    # app.register_blueprint(admin_page.bp_admin_page)
    # app.register_blueprint(admin_media.bp_admin_media)
    # app.register_blueprint(admin_user.bp_admin_user)
    # app.register_blueprint(admin_setting.bp_admin_setting)

    return app
