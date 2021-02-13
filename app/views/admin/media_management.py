# -*- coding: utf-8 -*-
# File: media_management.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:24
from flask import Blueprint

bp_admin_media = Blueprint('admin_media', __name__, url_prefix='/admin', template_folder='../templates/admin',
                           static_folder='../static')
