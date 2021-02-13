# -*- coding: utf-8 -*-
# File: page.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:29
from flask import Blueprint, render_template

bp_cms_page = Blueprint('cms_page', __name__, template_folder='../templates/cms', static_folder='../static')
