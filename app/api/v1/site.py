# -*- coding: utf-8 -*-
# File: site.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:26
from flask import jsonify, current_app, flash
from flask_restful import Resource, fields, reqparse, marshal_with

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.models.site import Site

PARSER_ARGS_STATUS = True

resource_fields = {
    'id': fields.String,
    'site_name': fields.String,
    'domain': fields.String,
    'keywords': fields.String,
    'description': fields.String

}

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, required=False, trim=True, location=[u'json', u'form', u'args', u'values'])
parser.add_argument('site_name', type=str, required=False, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入站点名称')
parser.add_argument('domain', type=str, required=False, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入站点域名')
parser.add_argument('keywords', type=int, trim=False, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入站点关键词')
parser.add_argument('description', type=str, required=False, trim=True, location=[u'json', u'form', u'args', u'values'],
                    help=u'请输入站点描述')


class SiteResource(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self):
        try:
            site_info = Site.query.all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if site_info is None:
            return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)

        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=serialize(site_info))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    def put(self):
        args = parser.parse_args(strict=PARSER_ARGS_STATUS)

        site = Site(
            site_name=args.site_name,
            domain=args.domain,
            keywords=args.keywords,
            description=args.description
        )
        db.session.add(site)
        db.session.commit()
        flash('Post created.', 'success')
        data = dict(code=ResponseCode.UPDATE_SITEINFO_SUCCESS, message=ResponseMessage.UPDATE_SITEINFO_SUCCESS)
        return jsonify(data)
