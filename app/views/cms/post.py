# -*- coding: utf-8 -*-
# File: post.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:30
from flask import Blueprint, render_template

bp_cms_post = Blueprint('cms_post', __name__, template_folder='../templates/cms', static_folder='../static')
