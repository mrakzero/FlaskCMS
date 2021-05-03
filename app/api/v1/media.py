# -*- coding: utf-8 -*-
# File: media.py
# Author: Zhangzhijun
# Date: 2021/2/15 11:34
import os

from flask import Blueprint, send_from_directory, request, url_for
from flask_ckeditor import upload_fail, upload_success

bp_admin_media = Blueprint('admin_media', __name__, url_prefix='/admin', template_folder='../templates/admin',
                           static_folder='../static')


@bp_admin_media.route('/files/<path:filename>')
def uploaded_files(filename):
    path = '/the/uploaded/directory'
    return send_from_directory(path, filename)


@bp_admin_media.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    # Add more validations here
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join('/the/uploaded/directory', f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url=url)  # return upload_success call
