# -*- coding: utf-8 -*-

from app import db


class Comment(db.Model):
    __tablename__ = 't_comment'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nickname = db.Column(db.String(64), nullable=False, comment='用户昵称')
    content = db.Column(db.Text, comment='评论内容')
    date = db.Column(db.DateTime, server_default=db.func.now(), comment='发表时间')
    postid = db.Column(db.Integer, db.ForeignKey('t_post.id'), comment='文章id')
    parentid = db.Column(db.Integer, db.ForeignKey("t_comment.id"), comment='父评论id')

    def __init__(self, **kwargs):
        super(Comment,self).__init__(**kwargs)

    def __repr__(self):
        return '<Model Comment `{}`>'.format(self.nickname)
