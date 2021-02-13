# -*- coding: utf-8 -*-
# File: user_management.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:26
from flask import Blueprint

bp_admin_user = Blueprint('admin_user', __name__, url_prefix='/admin', template_folder='../templates/admin',
                          static_folder='../static')
