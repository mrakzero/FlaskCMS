# -*- coding: utf-8 -*-

from threading import Thread
from flask import render_template, current_app
from flask_mail import Message
from . import mail


def send_async_mail(app, msg):
    '''创建邮件发送函数'''
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    if app.config['FLASKY_ADMIN']:
        msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                      sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        thr = Thread(target=send_async_mail, args=(app, msg))
        thr.start()  # 通过创建子线程实现异步发送邮件
        return thr
