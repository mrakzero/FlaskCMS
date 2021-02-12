# -*- coding: utf-8 -*-

from flask import render_template
from . import main


@main.app_errorhandler(404)  # 路由装饰器由蓝本提供，这里要调用 app_errorhandler 而不是 errorhandler
def page_not_found(e):
    return render_template('admin/errors/404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('admin/errors/500.html'), 500
