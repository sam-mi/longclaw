from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from search import views as search_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from longclaw import urls as longclaw_urls

urlpatterns = [
    path(r'^django-admin/', admin.site.urls),

    path(r'^admin/', include(wagtailadmin_urls)),
    path(r'^documents/', include(wagtaildocs_urls)),

    path(r'^search/$', search_views.search, name='search'),

    path(r'', include(longclaw_urls)),
    path(r'', include(wagtail_urls))
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
