from django.conf.urls import include, patterns

# Add additional url patterns for additional apps
# here and they will be included in the main urls.py
extrapatterns = patterns('',
     (r'^explorer/', include('explorer.urls')),
     (r'^explorer/', include('tendenci.apps.explorer_extensions.urls')),
     #(r'^helpdesk/', include('helpdesk.urls')),
     ('^', include('tendenci.apps.committees.urls')),
     ('^', include('tendenci.apps.case_studies.urls')),
     ('^', include('tendenci.apps.donations.urls')),
     ('^', include('tendenci.apps.speakers.urls')),
     ('^', include('tendenci.apps.staff.urls')),
     ('^', include('tendenci.apps.studygroups.urls')),
     ('^', include('tendenci.apps.videos.urls')),
     ('^', include('tendenci.apps.testimonials.urls')),
     (r'^', include('tendenci.apps.social_services.urls')),
)
