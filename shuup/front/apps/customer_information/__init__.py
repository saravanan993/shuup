# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2016, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = __name__
    verbose_name = _('Shuup Frontend - Customer Information Editing')
    label = 'shuup_front.customer_information'

    provides = {
        "front_urls": [__name__ + '.urls:urlpatterns'],
        "customer_dashboard_items": [
            __name__ + '.dashboard_items:CustomerDashboardItem',
            __name__ + '.dashboard_items:CompanyDashboardItem',
            __name__ + '.dashboard_items:AddressBookDashboardItem'
        ],
    }


default_app_config = __name__ + '.AppConfig'
