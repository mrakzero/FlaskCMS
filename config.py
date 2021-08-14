# -*- coding: utf-8 -*-

import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):  # 所有配置类的父类，通用的配置写在这里
    DEBUG = True
    WTF_CSRF_ENABLED = False  # 激活跨站点请求伪造保护
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # PERMANENT_SESSION_LIFETIME = timedelta(days=31),  # session有效期时间的设置
    # SESSION_COOKIE_NAME = "session"  # cookies中存储的session字符串的键
    # SESSION_COOKIE_DOMAIN = None  # session作用域
    # SESSION_COOKIE_PATH = None  # session作用的请求路径
    # SESSION_COOKIE_HTTPONLY = True  # session是否只支持http请求方式
    # SESSION_COOKIE_SECURE = False  # session安全配置
    # SESSION_COOKIE_SAMESITE = None
    # SESSION_REFRESH_EACH_REQUEST = True
    JSONIFY_MIMETYPE = "application/json"  # 设置jsonify响应时返回的contentype类型
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[FlaskCMS]'
    FLASKY_MAIL_SENDER = 'FlaskCMS Admin'
    FLASKY_ADMIN = 'admin@flaskcms.com'

    # USE_X_SENDFILE = False
    # SERVER_NAME = None,  # 主机名设置
    # APPLICATION_ROOT = "/"  # 应用根目录配置

    @staticmethod
    def init_app(app):  # 静态方法作为配置的统一接口，暂时为空
        pass


class DevelopmentConfig(Config):  # 开发环境配置类
    DEBUG = True  # debug模式的设置,开发环境用，自动重启项目，日志级别低，报错在前端显示具体代码
    TESTING = False  # 测试模式的设置，无限接近线上环境，不会重启项目，日志级别较高，不会在前端显示错误代码
    MAIL_SERVER = 'smtp.flaskcms.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'user@flaskcms.com'
    MAIL_PASSWORD = 'xxxxxx'
    SQLALCHEMY_ECHO = True  # 如果设置成 True，SQLAlchemy 将会记录所有发到标准输出(stderr)的语句
    SQLALCHEMY_DATABASE_URI = 'postgresql://flaskcms:flaskcms@localhost/flaskcms'


class TestingConfig(Config):  # 测试环境配置类
    DEBUG = False  # debug模式的设置,开发环境用，自动重启项目，日志级别低，报错在前端显示具体代码
    TESTING = True  # 测试模式的设置，无限接近线上环境，不会重启项目，日志级别较高，不会在前端显示错误代码
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):  # 生产环境配置类
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


# config字典注册了不同的配置，默认配置为开发环境，本例使用开发环境
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# 配置日志
logger_conf = {
    'version': 1,
    # 设置输出格式
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    # 设置处理器
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default',
        'level': 'DEBUG'
    }},
    # 设置root日志对象配置
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    },
    # 设置其他日志对象配置
    'loggers': {
        'test':
            {'level': 'DEBUG',
             'handlers': ['wsgi'],
             'propagate': 0}
    }
}
