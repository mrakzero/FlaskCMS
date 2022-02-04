# -*- coding: utf-8 -*-
# File: sitting.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:26
from flask import url_for, render_template
from werkzeug.utils import redirect

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.forms.site_form import SiteForm
from app.models.site import Site
from app.views.admin import bp_admin


@bp_admin.route('/site/setting', methods=['GET', 'POST'])
def setting():
    site_form = SiteForm()
    if site_form.validate_on_submit():
        site = get_site_info(site_form)

        db.session.add(site)
        db.session.commit()
        return redirect(url_for('bp_admin.get_categories'))

    # site_form.title.data = site.site_name
    # site_form.slug.data = site.domain
    # site_form.excerpt.data = site.keywords
    # site_form.content.data = site.description
    # site_form.categoryid.data = site.categoryid
    # site_form.status.data = site.status

    return render_template('admin/site/setting.html', site_form=site_form)
    # return dict(code=ResponseCode.CREATE_CATEGORY_SUCCESS, message=ResponseMessage.CREATE_CATEGORY_SUCCESS)


def get_site_info(form):
    site = Site()
    site.name = form.name.data
    site.slug = form.slug.data
    site.parentid = form.parentid.data
    site.description = form.description.data

    return site
