#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version: 1.0.0
# author:Zhang Zhijun
# time: 2021-03-13
# file: errorcode.py
# function:
# modify:

from enum import Enum, unique


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

    CREATE_MEDIA_SUCCESS = 20007000
    UPDATE_MEDIA_SUCCESS = 20007001
    DELETE_MEDIA_SUCCESS = 20007002
    GET_MEDIA_SUCCESS = 20007003

    UPDATE_SITEINFO_SUCCESS = 20008001
    GET_SITEINFO_SUCCESS = 20008003

    BAD_REQUEST = 40000000

    USER_NOT_EXIST = 40002000
    USER_ALREADY_EXIST = 40002001

    CATEGORY_NOT_EXIST = 40003000
    CATEGORY_ALREADY_EXIST = 40003001

    POST_NOT_EXIST = 40004000
    POST_ALREADY_EXIST = 40004001


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


# @unique
# class ErrorCode(Enum):
#     SUCCESS = 200
#     LOGIN_IS_FAIL = 1001
#     PASS_WORD_INFO_NOT_FILL = 1002
#     TWO_PASS_WORD_DIFFERENT = 1003
#     OLD_PASS_WORD_IS_NOT_FAIL = 1004
#     LOGIN_FAIL = 1005
#     PASS_WORD_RESET_FAIL = 1006
#     USER_NOT_EXIST = 1007
#     IMPORT_CSV_FAIL = 1008
#     IMPORT_CSV_SUCCESS = 1009
#     RECORD_EXIST = 1010
#     ADD_DATA_FAIL = 1011
#     UPDATE_DATA_FAIL = 1012
#     DELETE_DATA_FAIL = 1013
#     GET_DATA_FAIL = 1014
#     REQUEST_VERSION_ISEXISTENCE = 1015
#     ALREADY_HANDLED = 1016
#     DATA_IS_NOT_EXIST = 1017
#     REQUEST_PARAM_MISSED = 1018
#     EQUEST_PARAM_FORMAT_ERROR = 1019
#     OPENTSDB_ERROR = 1020
#     DATA_BASE_ERROR = 1021
#     NOT_FOUND = 404
#     BAD_REQUEST = 400
#     FORBIDDEND = 403
#     WRONGVALUE = 1022
#     CHECK_EXIST_ERROR = 1023
#     EXCEPTION_DB = 1024


# class ResponseCode(object):
#
#     @staticmethod
#     def SUCCESS():
#         return {'code': 200, 'msg': '请求成功'}
#
#     @property
#     def LOGIN_IS_FAIL(self):
#         return {'code': 1001, 'msg': '用户名或者密码错误'}
#
#     @property
#     def PASS_WORD_INFO_NOT_FILL(self):
#         return {'code': 1002, 'msg': '密码信息填写完整'}
#
#     @property
#     def TWO_PASS_WORD_DIFFERENT(self):
#         return {'code': 1003, 'msg': '两次密码不一致'}
#
#     @property
#     def OLD_PASS_WORD_IS_NOT_FAIL(self):
#         return {'code': 1004, 'msg': '旧密码不正确'}
#
#     @property
#     def LOGIN_FAIL(self):
#         return {'code': 1005, 'msg': '登录失败请联系管理员'}
#
#     @property
#     def PASS_WORD_RESET_FAIL(self):
#         return {'code': 1006, 'msg': '密码重置失败'}
#
#     @property
#     def USER_NOT_EXIST(self):
#         return {'code': 1007, 'msg': '用户不存在'}
#
#     @property
#     def IMPORT_CSV_FAIL(self):
#         return {'code': 1008, 'msg': '导入数据失败'}
#
#     @property
#     def IMPORT_CSV_SUCCESS(self):
#         return {'code': 1009, 'msg': '导入数据成功'}
#
#     @property
#     def RECORD_EXIST(self):
#         return {'code': 1010, 'msg': '记录已存在'}
#
#     @property
#     def ADD_DATA_FAIL(self):
#         return {'code': 1011, 'msg': '添加数据失败'}
#
#     @property
#     def UPDATE_DATA_FAIL(self):
#         return {'code': 1012, 'msg': '修改数据失败'}
#
#     @property
#     def DELETE_DATA_FAIL(self):
#         return {'code': 1013, 'msg': '删除数据失败'}
#
#     @property
#     def GET_DATA_FAIL(self):
#         return {'code': 1014, 'msg': '获取数据失败'}
#
#     @property
#     def REQUEST_VERSION_ISEXISTENCE(self):
#         return {'code': 1015, 'msg': '请求的版本不存在'}
#
#     @property
#     def ALREADY_HANDLED(self):
#         return {'code': 1016, 'msg': '参数类型错误'}
#
#     @property
#     def DATA_IS_NOT_EXIST(self):
#         return {'code': 1017, 'msg': '数据不存在'}
#
#     @property
#     def REQUEST_PARAM_MISSED(self):
#         return {'code': 1018, 'msg': '请求参数缺失'}
#
#     @property
#     def REQUEST_PARAM_FORMAT_ERROR(self):
#         return {'code': 1019, 'msg': '请求参数格式错误'}
#
#     @property
#     def OPENTSDB_ERROR(self):
#         return {'code': 1020, 'msg': 'opentsdb服务器错误'}
#
#     @property
#     def DATA_BASE_ERROR(self):
#         return {'code': 1021, 'msg': "数据库连接失败"}
#
#     @property
#     def NOT_FOUND(self):
#         return {'code': 404, 'msg': 'HTTP 404 Not Found'}
#
#     @property
#     def BAD_REQUEST(self):
#         return {'code': 400, 'msg': 'HTTP 400 Bad Request'}
#
#     @property
#     def FORBIDDEND(self):
#         return {'code': 403, 'msg': 'HTTP 403 Forbidden'}
#
#     @property
#     def WRONGVALUE(self):
#         return {'code': 1022, 'msg': '参数值超出规定范围'}
#
#     @property
#     def CHECK_EXIST_ERROR(self):
#         return {'code': 1023, 'msg': '验证数据错误'}
#
#     @property
#     def EXCEPTION_DB(self):
#         return {'code': 1024, 'msg': '数据库操作异常'}
#
#     def get_struct_by_error_code(self, error_code):
#         if error_code == ErrorCode.SUCCESS:
#             return self.SUCCESS
#         if error_code == ErrorCode.LOGIN_IS_FAIL:
#             return self.LOGIN_IS_FAIL
#         if error_code == ErrorCode.PASS_WORD_INFO_NOT_FILL:
#             return self.PASS_WORD_INFO_NOT_FILL
#         if error_code == ErrorCode.TWO_PASS_WORD_DIFFERENT:
#             return self.TWO_PASS_WORD_DIFFERENT
#         if error_code == ErrorCode.OLD_PASS_WORD_IS_NOT_FAIL:
#             return self.OLD_PASS_WORD_IS_NOT_FAIL
#         if error_code == ErrorCode.LOGIN_FAIL:
#             return self.LOGIN_FAIL
#         if error_code == ErrorCode.PASS_WORD_RESET_FAIL:
#             return self.PASS_WORD_RESET_FAIL
#         if error_code == ErrorCode.USER_NOT_EXIST:
#             return self.PASS_WORD_RESET_FAIL
#         if error_code == ErrorCode.IMPORT_CSV_FAIL:
#             return self.IMPORT_CSV_FAIL
#         if error_code == ErrorCode.IMPORT_CSV_SUCCESS:
#             return self.IMPORT_CSV_SUCCESS
#         if error_code == ErrorCode.RECORD_EXIST:
#             return self.RECORD_EXIST
#         if error_code == ErrorCode.ADD_DATA_FAIL:
#             return self.ADD_DATA_FAIL
#         if error_code == ErrorCode.UPDATE_DATA_FAIL:
#             return self.UPDATE_DATA_FAIL
#         if error_code == ErrorCode.DELETE_DATA_FAIL:
#             return self.DELETE_DATA_FAIL
#         if error_code == ErrorCode.GET_DATA_FAIL:
#             return self.DELETE_DATA_FAIL
#         if error_code == ErrorCode.REQUEST_VERSION_ISEXISTENCE:
#             return self.REQUEST_VERSION_ISEXISTENCE
#         if error_code == ErrorCode.ALREADY_HANDLED:
#             return self.ALREADY_HANDLED
#         if error_code == ErrorCode.DATA_IS_NOT_EXIST:
#             return self.DATA_IS_NOT_EXIST
#         if error_code == ErrorCode.REQUEST_PARAM_MISSED:
#             return self.REQUEST_PARAM_MISSED
#         if error_code == ErrorCode.REQUEST_PARAM_FORMAT_ERROR:
#             return self.REQUEST_PARAM_FORMAT_ERROR
#         if error_code == ErrorCode.OPENTSDB_ERROR:
#             return self.OPENTSDB_ERROR
#         if error_code == ErrorCode.DATA_BASE_ERROR:
#             return self.DATA_BASE_ERROR
#         if error_code == ErrorCode.NOT_FOUND:
#             return self.NOT_FOUND
#         if error_code == ErrorCode.BAD_REQUEST:
#             return self.BAD_REQUEST
#         if error_code == ErrorCode.FORBIDDEND:
#             return self.FORBIDDEND
#         if error_code == ErrorCode.WRONGVALUE:
#             return self.WRONGVALUE
#         if error_code == ErrorCode.CHECK_EXIST_ERROR:
#             return self.CHECK_EXIST_ERROR
#         if error_code == ErrorCode.EXCEPTION_DB:
#             return self.EXCEPTION_DB
#
#
# response_code = ResponseCode()


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
