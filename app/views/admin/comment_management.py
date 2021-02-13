# -*- coding: utf-8 -*-
# File: comment_management.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:25
from flask import Blueprint

bp_admin_comment = Blueprint('admin_comment', __name__, url_prefix='/admin', template_folder='../templates/admin',
                             static_folder='../static')
