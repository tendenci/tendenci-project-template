# Method that pulls settings from the standard settings.py
# file so that you can append or override items.
def get_setting(setting):
    import settings
    return getattr(settings, setting)

SECRET_KEY='your_unique_secret_key_Qoh222VG9pq8P9hOapH'
SITE_SETTINGS_KEY='tendenci_site_key_bdc635k2-283d-4a2c-a477-339ea866'

INSTALLED_APPS = get_setting('INSTALLED_APPS')

INSTALLED_APPS += (
    'django.contrib.gis',
    'tendenci.apps.committees',
    'tendenci.apps.case_studies',
    'tendenci.apps.donations',
    'tendenci.apps.speakers',
    'tendenci.apps.staff',
    'tendenci.apps.studygroups',
    'tendenci.apps.videos',
    'tendenci.apps.testimonials',
    'tendenci.apps.social_services',
    # -- explorer block --
    'tendenci.apps.explorer_extensions',
    'explorer',
    # -- end of explorer block --

    # --helpdesk --
    #'markdown_deux',
    #'bootstrapform',
    #'tendenci.apps.helpdesk',
    # -- end of helpdesk
)

USE_I18N = True
ALLOWED_HOSTS = ["*"]

SITE_MODE = 'prod'

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '<DB_NAME>',
        'HOST': 'localhost',
        'USER': '<DB_USER>',
        'PASSWORD': '<DB_PASS>',
        'PORT': 5432,
        'autocommit': True,
        }
}


SSL_ENABLED = False
CELERY_IS_ACTIVE = False

# Logged in users may either be logged out when the user closes their
# browser, or may remain logged in after the user closes and reopens
# their browser.
# For logins through /admin/login/, SESSION_EXPIRE_AT_BROWSER_CLOSE
# controls this behavior.
# For logins through /accounts/login/, the "Hide Remember Me" and
# "Remember Me Checked" settings in the "Users" app in Tendenci control
# this behavior, overriding SESSION_EXPIRE_AT_BROWSER_CLOSE.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# Independently of that behavior, users will also be logged out by both
# the server and their browser if they do not visit the site for more
# than SESSION_COOKIE_AGE seconds.  However, each page load will reset
# this counter, allowing the user to remain logged in indefinitely as
# long as they continue to visit the site regularly.
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2  # 2 weeks

#SESSION_COOKIE_SECURE = True  # Send Session Cookie over HTTPS only
#CSRF_COOKIE_SECURE = True  # Send CSRF Cookie over HTTPS only

# Uncomment to properly detect HTTP vs HTTPS when running behind nginx.
# DO NOT uncomment if not running behind nginx, as that will open a security
# hole.
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

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
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
    RAVEN_CONFIG = {
        'dsn': SENTRY_DSN,
}

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
# Uncomment when using the PayPal Sandbox
#PAYPAL_POST_URL = 'https://www.sandbox.paypal.com/cgi-bin/webscr'

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


# sql explorer only allows superuser
EXPLORER_PERMISSION_VIEW =  lambda u: u.is_superuser
EXPLORER_PERMISSION_CHANGE =  lambda u: u.is_superuser

# helpdesk
#HELPDESK_REDIRECT_TO_LOGIN_BY_DEFAULT = True

# debug mode
DEBUG = False

# Django Debug Toolbar for profiling (measuring CPU/SQL/cache/etc timing)
# Set DEBUG_TOOLBAR_INSTALLED to deploy the relevant static files (when
# `python manage.py deploy` is run) and add the necessary middleware.
# Set DEBUG_TOOLBAR_ENABLED to actually enable profiling and the toolbar.
# DEBUG_TOOLBAR_INSTALLED should not impact performance, but
# DEBUG_TOOLBAR_ENABLED will slow down Django.
DEBUG_TOOLBAR_INSTALLED = True
DEBUG_TOOLBAR_ENABLED = False
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda req: DEBUG_TOOLBAR_ENABLED,
    'SHOW_COLLAPSED': False,
}

TEMPLATES = get_setting('TEMPLATES')
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
# Turn off the template caching
# TEMPLATES[0]['OPTIONS']['loaders'] = [
#                 'app_namespace.Loader',
#                 'tendenci.apps.theme.template_loaders.Loader',
#                 'django.template.loaders.filesystem.Loader',
#                 'django.template.loaders.app_directories.Loader',
#             ]

# -------------------------------------- #
# LOGGING
# -------------------------------------- #
ENABLE_LOGGING = False
if ENABLE_LOGGING:
  if DEBUG:
    import sys
    if not sys.warnoptions:
      # Log Python Warnings to the py.warnings logger instead of the console
      import logging
      logging.captureWarnings(True)
      # Enable ImportWarning and DeprecationWarning messages
      import warnings
      warnings.simplefilter("default")
  LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        # Set the default logger level to DEBUG so that all messages are passed
        # to the handlers and the handlers can decide which messages to actually
        # log.
        'level': 'DEBUG',
        'handlers': ['file', 'debug_file', 'mail_admins'],
    },
    'loggers': {
        # The 'django' logger must be defined to override the defaults
        # configured by Django:
        # https://github.com/django/django/blob/master/django/utils/log.py
        'django': {
            'level': 'DEBUG',
            # Disable the default handlers
            'handlers': [],
            # And use the 'root' handlers above instead
            'propagate': True,
        },
        # In Django <=1.10, 'django.request', 'django.security', and
        # 'py.warnings' must also be defined to override the defaults configured
        # by Django.
        'django.request': {
            'level': 'DEBUG',
            'handlers': [],
            'propagate': True,
        },
        'django.security': {
            'level': 'DEBUG',
            'handlers': [],
            'propagate': True,
        },
        'py.warnings': {
            'level': 'DEBUG',
            'handlers': [],
            'propagate': True,
        },
        # django.db.backends logs all SQL statements at DEBUG level when
        # settings.DEBUG is True.  That produces lots of log messages, so set
        # the level at INFO to filter them.
        'django.db.backends': {
            'level': 'INFO',
        },
        # The Daphne web server logs connection details at DEBUG level.  That
        # produces lots of log messages, so set the level at INFO to filter
        # them when running under Daphne.
        # In addition, Daphne logs ERRORs when workers are stopped/started.  It
        # is probably unnecessary to send emails for those, so disable the
        # mail_admins handler for Daphne logs.
        'daphne': {
            'level': 'INFO',
            'handlers': ['file', 'debug_file'],
            'propagate': False,
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'info': {
            'format': 'TIME="%(asctime)s" LEVEL=%(levelname)s PID=%(process)d LOGGER="%(name)s" MSG="%(message)s"'
        },
        'debug': {
            'format': 'TIME="%(asctime)s" LEVEL=%(levelname)s PID=%(process)d LOGGER="%(name)s" FILE="%(pathname)s" LINE=%(lineno)s FUNC="%(funcName)s" MSG="%(message)s"'
        },
    },
    'handlers': {
        # FileHandler is thread safe but not multi-process safe, so log output could be interleaved
        # if multiple worker processes generate a log message at the same time.  Since Django and
        # Tendenci logging is minimal and mostly non-critical, this is not likely to be much of a
        # problem in most cases.  However, if you need multi-process safe logging, use SysLogHandler
        # or SocketHandler with a log server such as https://pypi.python.org/pypi/multilog .
        #
        # DO NOT use RotatingFileHandler or TimedRotatingFileHandler here, as their rotation
        # behavior is not multi-process safe and will cause data to be lost from rotated log files.
        # When using those Handlers, each process will redundantly rotate the files and will
        # overwrite any files previously rotated by another process.  If you need logs to be
        # automatically rotated, either use logrotate (and restart Tendenci after rotation), or use
        # SocketHandler with a log server such as multilog which can then safely use
        # RotatingFileHandler or TimedRotatingFileHandler.
        'file': {
            'level': 'INFO',
            'formatter': 'info',
            'class': 'logging.FileHandler',
            'filename': '/var/log/tendenci/app.log',
        },
        'debug_file': {
            'filters': ['require_debug_true'],
            'level': 'DEBUG',
            'formatter': 'debug',
            'class': 'logging.FileHandler',
            'filename': '/var/log/tendenci/debug.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'tendenci.apps.base.log.CustomAdminEmailHandler',
        },
        'discard': {
            'level': 'CRITICAL',
            'class': 'logging.NullHandler',
        },
    },
  }
