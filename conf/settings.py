import os
from tendenci.settings import *

# go one level up
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

ROOT_URLCONF = 'conf.urls'

INSTALLED_APPS += (
    'gunicorn',
)

SITE_ADDONS_PATH = os.path.join(PROJECT_ROOT, 'addons')

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# -------------------------------------- #
# DEBUG OPTIONS
# -------------------------------------- #
DEBUG_TOOLBAR = False
if DEBUG_TOOLBAR:
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

# -------------------------------------- #
# THEMES
# -------------------------------------- #
TEMPLATE_DIRS += (os.path.join(PROJECT_ROOT, "themes"),)
THEMES_DIR = os.path.join(PROJECT_ROOT, 'themes')


LOCALE_PATHS = (os.path.join(PROJECT_ROOT, 'themes'),)

# -------------------------------------- #
# STATIC MEDIA
# -------------------------------------- #
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

# Stock static media files and photos from the URL below
# are licensed by Ed Schipul as Creative Commons Attribution
# http://creativecommons.org/licenses/by/3.0/
#
# The full image set is available online at
# http://tendenci.com/photos/set/3/

STOCK_STATIC_URL = '//d15jim10qtjxjw.cloudfront.net/master-90/'

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.static',
    'tendenci.apps.base.context_processors.newrelic',)

# ----------------------------------------- #
# s3 storeage example
# set this up at https://console.aws.amazon.com/console/home
# deploy script will ignore and use local if not configured.
# It's all good.
# ----------------------------------------- #
AWS_LOCATION = ''    # this is usually your site name
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''

USE_S3_STORAGE = all([
    AWS_LOCATION,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_STORAGE_BUCKET_NAME
])


# -------------------------------------- #
# HAYSTACK SEARCH INDEX
# -------------------------------------- #
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_ROOT, 'index.whoosh'),
    }
}


# -------------------------------------- #
# CACHE
# -------------------------------------- #
LOCAL_CACHE_PATH = os.path.join(PROJECT_ROOT, "cache")


# CAMPAIGN MONITOR
CAMPAIGNMONITOR_URL = ''
CAMPAIGNMONITOR_API_KEY = ''
CAMPAIGNMONITOR_API_CLIENT_ID = ''

# ------------------------------------ #
# IMPERSONATION ADDON
# ------------------------------------ #

if os.path.exists(os.path.join(PROJECT_ROOT, 'addons/impersonation/')):
    MIDDLEWARE_CLASSES += (
        'addons.impersonation.middleware.ImpersonationMiddleware',
    )

# local settings for development
try:
    from local_settings import *
except ImportError:
    pass


# THIS MUST BE AT THE END!
# -------------------------------------- #
# ADDONS
# -------------------------------------- #

DEFAULT_INSTALLED_APPS = INSTALLED_APPS
from tendenci.apps.registry.utils import update_addons
INSTALLED_APPS = update_addons(INSTALLED_APPS, SITE_ADDONS_PATH)
