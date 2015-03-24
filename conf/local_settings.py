# Method that pulls settings from the standard settings.py
# file so that you can append or override items.
def get_setting(setting):
    import settings
    return getattr(settings, setting)

SECRET_KEY='your_unique_secret_key_Qoh222VG9pq8P9hOapH'
SITE_SETTINGS_KEY='tendenci_site_key_bdc635k2-283d-4a2c-a477-339ea866'

INSTALLED_APPS = get_setting('INSTALLED_APPS')

TEMPLATE_CONTEXT_PROCESSORS = get_setting('TEMPLATE_CONTEXT_PROCESSORS')

INSTALLED_APPS += (
    'django.contrib.gis',
    'committees',
    'case_studies',
    'donations',
    'speakers',
    'staff',
    'studygroups',
    'videos',
    'explorer',
    #'social_services',
    #'legacy_t4',

    # -- start of helpdesk --
    #'bootstrap_admin',
    #'taggit',
    #'bootstrapform',
    #'helpdesk',
    # -- end of helpdesk --
)

USE_I18N = True
ALLOWED_HOSTS = ["*"]

SITE_MODE = 'prod'

ADMINS = ()
MANAGERS = ADMINS

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '<DB_NAME>',
        'HOST': 'localhost',
        'USER': '<DB_USER>',
        'PASSWORD': '<DB_PASS>',
        'PORT': 5432,
        'OPTIONS': {'autocommit': True},
        }
}


SSL_ENABLED = False
CELERY_IS_ACTIVE = False

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'US/Central'

# -------------------------------------- #
# DEBUG OPTIONS
# -------------------------------------- #
SENTRY_DSN = ""
if SENTRY_DSN:
    INSTALLED_APPS += ('raven.contrib.django',)

# ---------------------------------------#
# PAYMENT GATEWAY
# ---------------------------------------#
# authorizenet, firstdata (the first two)
MERCHANT_LOGIN = ''
MERCHANT_TXN_KEY = ''
AUTHNET_MD5_HASH_VALUE = False

# paypalpayflowlink (currently US only unfortunately per PayPal)
PAYPAL_MERCHANT_LOGIN = ''
PAYFLOWLINK_PARTNER = 'PayPal'

# stripe
STRIPE_SECRET_KEY = ''
STRIPE_PUBLISHABLE_KEY = ''

# -------------------------------------- #
# EMAIL
# -------------------------------------- #
# remove or comment out this line once you have your email backend set up.
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = False
# EMAIL_HOST = None
# EMAIL_PORT = 25
# EMAIL_HOST_USER = None
# EMAIL_HOST_PASSWORD = None

#EMAIL_BACKEND = "django_ses.SESBackend"
# AWS_ACCESS_KEY_ID = ''
# AWS_SECRET_ACCESS_KEY = ''

DEFAULT_FROM_EMAIL = "no-reply@example.com"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# -------------------------------------- #
# CACHE
# -------------------------------------- #

SITE_CACHE_KEY = SECRET_KEY

CACHE_PRE_KEY = SITE_CACHE_KEY
JOHNNY_MIDDLEWARE_KEY_PREFIX = SITE_CACHE_KEY
JOHNNY_TABLE_BLACKLIST = ('base_updatetracker')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Local memcached requires memcached to be running locally.
MEMCACHED_ENABLED = True
if MEMCACHED_ENABLED:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': "127.0.0.1:11211",
        }
    }
CACHES['default']['TIMEOUT'] = 60 * 60 * 24 * 30  # 30 days
CACHES['default']['JOHNNY_CACHE'] = True

# ------------------------------------------------------------------- #
# sql_explorer
#
# To enable sql_explorer:
# 1) Uncomment SOUTH_MIGRATION_MODULES.
# 2) If using a different db instead of default, uncomment and specify
#    the EXPLORER_CONNECTION_NAME setting, and add a custom db connection
#    in DATABASES setting.
# 3) Uncomment explorer in the INSTALLED_APPS setting
# 4) Uncomment explorer in url patterns in the local_urls
# ------------------------------------------------------------------- #
#EXPLORER_CONNECTION_NAME = 't4db'
SOUTH_MIGRATION_MODULES = { 'explorer': 'explorer.south_migrations', }

# ------------------------------------------------------------------- #
# helpdesk
#
# To enable helpdesk:
# 1) Uncomment the helpdesk block in the INSTALLED_APPS settings
# 2) Uncomment helpdesk in url patterns in the local_urls
# 3) If adding helpdesk from an already existing project, please make sure to run:
#    python manage.y create_usersettings
# 4) If you want users to be able to communicate with the helpdesk through emails,
#    - edit helpdesk/poll_helpdesk_email_queues.sh with the proper directory values
#    - add "*/1 * * * * username /home/username/django/project/poll_helpdesk_email_queues.sh >> /tmp/foo.log 2>&1" to crontab
#    - setup the individual email info per Queue object you create
# ------------------------------------------------------------------- #
#HELPDESK_EMAIL_SUBJECT_TEMPLATE = "[Tendenci] {{ ticket.ticket }} {{ ticket.title|safe }} %(subject)s"

# sql explorer only allows superuser
EXPLORER_PERMISSION_VIEW =  lambda u: u.is_superuser
EXPLORER_PERMISSION_CHANGE =  lambda u: u.is_superuser

