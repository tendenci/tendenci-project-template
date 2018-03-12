from django.conf.urls import url, include

# Add additional url patterns for additional apps
# here and they will be included in the main urls.py
extrapatterns = [
    url(r'^explorer/', include('explorer.urls')),
    url(r'^explorer/', include('tendenci.apps.explorer_extensions.urls')),
    #url(r'^tickets/', include('tendenci.apps.helpdesk.urls')),
    url(r'^', include('tendenci.apps.committees.urls')),
    url(r'^', include('tendenci.apps.case_studies.urls')),
    url(r'^', include('tendenci.apps.donations.urls')),
    url(r'^', include('tendenci.apps.speakers.urls')),
    url(r'^', include('tendenci.apps.staff.urls')),
    url(r'^', include('tendenci.apps.studygroups.urls')),
    url(r'^', include('tendenci.apps.videos.urls')),
    url(r'^', include('tendenci.apps.testimonials.urls')),
    url(r'^', include('tendenci.apps.social_services.urls')),
]
