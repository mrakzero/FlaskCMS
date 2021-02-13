# -*- coding: utf-8 -*-
# File: page_management.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:22
from flask import Blueprint

bp_admin_page = Blueprint('admin_page', __name__, url_prefix='/admin', template_folder='../templates/admin',
                          static_folder='../static')
