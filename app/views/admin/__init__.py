# -*- coding: utf-8 -*-
# File: __init__.py.py
# Author: Zhangzhijun
# Date: 2021/2/12 18:32

from flask import Blueprint

bp_admin = Blueprint('bp_admin', __name__, url_prefix='/admin', template_folder='../templates/admin/',
                     static_folder='../static')

from .category import *
from .comment import *
from .index import *
from .media import *
from .page import *
from .post import *
from .site import *
from .user import *
