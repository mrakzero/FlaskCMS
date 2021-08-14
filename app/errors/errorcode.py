#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version: 1.0.0
# author:Zhang Zhijun
# time: 2021-03-13
# file: errorcode.py
# function:
# modify:


class ResponseCode(object):
    """
    成功类错误码：20000000 ~ 20099999
    错误类错误码：40000000 ~ 40099999
    服务器错误码：50000000 ~ 50099999
    
    通用成功类错误码：20000000
    登录注册类错误码：20001000
    用户错误码：20002000
    分类错误：20003000
    文章错误：20004000
    """
    SUCCESS = 20000000
    QUERY_DB_FAILED = 20000001

    REGISTER_SUCCESS = 20001000
    LOGIN_SUCCESS = 20001001
    LOGOUT_SUCCESS = 20001002

    CREATE_USER_SUCCESS = 20002000
    UPDATE_USER_SUCCESS = 20002001
    DELETE_USER_SUCCESS = 20002002
    GET_USER_SUCCESS = 20002003

    CREATE_CATEGORY_SUCCESS = 20003000
    UPDATE_CATEGORY_SUCCESS = 20003001
    DELETE_CATEGORY_SUCCESS = 20003002
    GET_CATEGORY_SUCCESS = 20003003

    CREATE_POST_SUCCESS = 20004000
    UPDATE_POST_SUCCESS = 20004001
    DELETE_POST_SUCCESS = 20004002
    GET_POST_SUCCESS = 20004003

    CREATE_PAGE_SUCCESS = 20005000
    UPDATE_PAGE_SUCCESS = 20005001
    DELETE_PAGE_SUCCESS = 20005002
    GET_PAGE_SUCCESS = 20005003

    CREATE_TAG_SUCCESS = 20006000
    UPDATE_TAG_SUCCESS = 20006001
    DELETE_TAG_SUCCESS = 20006002
    GET_TAG_SUCCESS = 20006003

    CREATE_COMMENT_SUCCESS = 20007000
    UPDATE_COMMENT_SUCCESS = 20007001
    DELETE_COMMENT_SUCCESS = 20007002
    GET_COMMENT_SUCCESS = 20007003

    CREATE_MEDIA_SUCCESS = 20008000
    UPDATE_MEDIA_SUCCESS = 20008001
    DELETE_MEDIA_SUCCESS = 20008002
    GET_MEDIA_SUCCESS = 20008003

    UPDATE_SITEINFO_SUCCESS = 20009001
    GET_SITEINFO_SUCCESS = 20009003

    BAD_REQUEST = 40000000

    USER_NOT_EXIST = 40002000
    USER_ALREADY_EXIST = 40002001

    CATEGORY_NOT_EXIST = 40003000
    CATEGORY_ALREADY_EXIST = 40003001

    POST_NOT_EXIST = 40004000
    POST_ALREADY_EXIST = 40004001

    PAGE_NOT_EXIST = 40005000
    PAGE_ALREADY_EXIST = 40005001

    TAG_NOT_EXIST = 40006000
    TAG_ALREADY_EXIST = 40006001

    COMMENT_NOT_EXIST = 40007000
    COMMENT_ALREADY_EXIST = 40007001

    MEDIA_NOT_EXIST = 40008000
    MEDIA_ALREADY_EXIST = 40008001


class ResponseMessage(object):
    SUCCESS = u"成功"
    QUERY_DB_FAILED = u"查询数据库失败"

    REGISTER_SUCCESS = u"注册成功"
    LOGIN_SUCCESS = u"登录成功"
    LOGOUT_SUCCESS = u"退出成功"

    CREATE_USER_SUCCESS = u"创建用户成功"
    UPDATE_USER_SUCCESS = u"更新用户信息成功"
    DELETE_USER_SUCCESS = u"删除用户成功"

    CREATE_CATEGORY_SUCCESS = u"创建分类成功"
    UPDATE_CATEGORY_SUCCESS = u"更新分类信息成功"
    DELETE_CATEGORY_SUCCESS = u"删除分类成功"

    CREATE_POST_SUCCESS = u"创建文章成功"
    UPDATE_POST_SUCCESS = u"更新文章信息成功"
    DELETE_POST_SUCCESS = u"删除文章成功"

    CREATE_PAGE_SUCCESS = u'创建页面成功'
    UPDATE_PAGE_SUCCESS = u'更新页面成功'
    DELETE_PAGE_SUCCESS = u'删除页面成功'

    CREATE_TAG_SUCCESS = u'创建文章标签成功'
    UPDATE_TAG_SUCCESS = u'更新文件标签成功'
    DELETE_TAG_SUCCESS = u'删除文件标签成功'

    CREATE_COMMENT_SUCCESS = u'创建文章评论成功'
    UPDATE_COMMENT_SUCCESS = u'更新文章评论成功'
    DELETE_COMMENT_SUCCESS = u'删除文章评论成功'

    CREATE_MEDIA_SUCCESS = u'创建媒体文件成功'
    UPDATE_MEDIA_SUCCESS = u'更新媒体文件成功'
    DELETE_MEDIA_SUCCESS = u'删除媒体文件成功'

    UPDATE_SITEINFO_SUCCESS = u'更新站点信息成功'

    BAD_REQUEST = u"HTTP 400 Bad Request"

    USER_NOT_EXIST = u"用户不存在"
    USER_ALREADY_EXIST = u"用户已存在"

    CATEGORY_NOT_EXIST = u"分类不存在"
    CATEGORY_ALREADY_EXIST = u"分类已存在"

    POST_NOT_EXIST = u"文章不存在"
    POST_ALREADY_EXIST = u"文章已存在"

    PAGE_NOT_EXIST = u'页面不存在'
    PAGE_ALREADY_EXIST = u'页面已存在'

    TAG_NOT_EXIST = u'文章标签不存在'
    TAG_ALREADY_EXIST = u'文章标签已存在'

    COMMENT_NOT_EXIST = u'文章评论不存在'
    COMMENT_ALREADY_EXIST = u'文章评论已存在'

    MEDIA_NOT_EXIST = u'媒体文件不存在'
    MEDIA_ALREADY_EXIST = u'媒体文件已存在'


class ResMsg(object):
    """
    封装响应文本
    example:
    def test():
        test_dict = dict(name="zhang",age=36)
        data=dict(code=ResponseCode.SUCCESS, msg=ResponseMessage.SUCCESS, data=test_dict)
        return jsonify(data)

    """

    def __init__(self, code=ResponseCode.SUCCESS,
                 msg=ResponseMessage.SUCCESS, data=None):

        self._code = code
        self._msg = msg
        self._data = data

    def update(self, code=None, data=None, msg=None):
        """
        更新默认响应文本
        :param code:响应状态码
        :param data: 响应数据
        :param msg: 响应消息
        :return:
        """
        if code is not None:
            self._code = code
        if data is not None:
            self._data = data
        if msg is not None:
            self._msg = msg

    def add_field(self, name=None, value=None):
        """
        在响应文本中加入新的字段，方便使用
        :param name: 变量名
        :param value: 变量值
        :return:
        """
        if name is not None and value is not None:
            self.__dict__[name] = value

    @property
    def data(self):
        """
        输出响应文本内容
        :return:
        """
        body = self.__dict__
        body["data"] = body.pop("_data")
        body["msg"] = body.pop("_msg")
        body["code"] = body.pop("_code")
        return body
