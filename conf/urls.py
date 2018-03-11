from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views import static
from tendenci.urls import urlpatterns as tendenci_urls

handler500 = 'tendenci.apps.base.views.custom_error'

urlpatterns = staticfiles_urlpatterns()

if not settings.USE_S3_STORAGE:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static.serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', static.serve, {
            'document_root': settings.STATIC_ROOT,
        }),
        url(r'^themes/(?P<path>.*)$', static.serve, {
            'document_root': settings.THEMES_DIR,
        }),
    ]

# Local url patterns for development
try:
    from local_urls import extrapatterns
    urlpatterns += extrapatterns
except ImportError:
    pass

urlpatterns += tendenci_urls
