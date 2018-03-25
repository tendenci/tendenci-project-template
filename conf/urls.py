#
# This file is ignored unless "ROOT_URLCONF = 'conf.urls'" is configured in
# settings.py
#

from tendenci.urls import handler500  # noqa: F401
from tendenci.urls import pre_urlpatterns, post_urlpatterns
from django.conf.urls import url, include  # noqa: F401


urlpatterns = pre_urlpatterns + [
    #url(r'^', include('example_app.urls')),
    #url(r'^tickets/', include('tendenci.apps.helpdesk.urls')),
] + post_urlpatterns


# To remove a URL pattern from the default configuration:
#from tendenci.urls import remove_url_for_include  # noqa: E402
#remove_url_for_include(urlpatterns, 'some_app.urls')
# Or:
#remove_includes = ['app1.urls', 'app2.urls']
#for include in remove_includes:
#    remove_url_for_include(urlpatterns, include)
