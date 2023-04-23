# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.urls import path, include

from wagtail.admin import urls as admin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as documents_urls
from longclaw import urls as longclaw_urls
from longclaw.contrib.productrequests import urls as request_urls

urlpatterns = [
    path(r'^admin/', include(admin_urls)),
    path(r'^documents/', include(documents_urls)),

    path(r'', include(longclaw_urls)),
    path(r'', include(request_urls)),
    path(r'', include(wagtail_urls)),


]
