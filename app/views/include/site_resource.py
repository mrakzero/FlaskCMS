# -*- coding: utf-8 -*-
# File: site_resource.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:26
from flask import jsonify, current_app, flash
from flask_restful import Resource, fields, reqparse, marshal_with

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.models.site import Site
from app.utils import query_to_dict


class SiteResource():
    def get_site_info(self):
        try:
            site_info = Site.query.all()
        except:
            return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
        if site_info is None:
            return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)

        data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(site_info))
        current_app.logger.debug("data: %s", data)
        return jsonify(data)

    def update_site_info(self, site):

        db.session.add(site)
        db.session.commit()
        flash('Post created.', 'success')
        data = dict(code=ResponseCode.UPDATE_SITEINFO_SUCCESS, message=ResponseMessage.UPDATE_SITEINFO_SUCCESS)
        return jsonify(data)
