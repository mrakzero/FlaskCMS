# -*- coding: utf-8 -*-
from flask import Flask
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf import CSRFProtect

from config import config

# 由于尚未初始化所需的程序实例，所以没有初始化扩展，创建扩展类时没有向构造函数传入参数。

mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
ckeditor = CKEditor()
csrf = CSRFProtect()  # CKEditor CSRF


def create_app(config_name):
    '''工厂函数'''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)  # 通过config.py统一接口
    mail.init_app(app)  # 同上
    db.init_app(app)  # 同上

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
    ckeditor.init_app(app)
    # 配置分页
    app.config['POST_PER_PAGE'] = 10

    # 附加路由和自定义错误页面，将蓝本注册到工厂函数
    from app.views.admin import dashboard, post_management, page_management, comment_management, media_management, \
        user_management, setting
    from app.views.cms import index, category, page, post

    app.register_blueprint(index.bp_cms_index)
    app.register_blueprint(category.bp_cms_category)
    app.register_blueprint(post.bp_cms_post)
    app.register_blueprint(page.bp_cms_page)

    app.register_blueprint(dashboard.bp_admin_index, url_prefix='/admin')
    app.register_blueprint(post_management.bp_admin_post)
    app.register_blueprint(page_management.bp_admin_page)
    app.register_blueprint(media_management.bp_admin_media)
    app.register_blueprint(user_management.bp_admin_user)
    app.register_blueprint(setting.bp_admin_setting)

    return app
