from tendenci.settings import *
import os

import environ

# Configure your site-specific settings here to override the defaults configured
# by Tendenci and Django. Secrets should be kept in an .env file and referenced 
# using django-environ to ensure they are not leaked when using source control 
# such as git. 
#
# See https://github.com/tendenci/tendenci/blob/master/tendenci/settings.py for
# Tendenci defaults.  See https://docs.djangoproject.com/en/1.11/ref/settings/
# for Django defaults.
#
# To override part of a data structure configured by Tendenci without replacing
# the entire data structure, you can use something like:
# Add a list item: INSTALLED_APPS += ['example_app']
# Remove a list item: INSTALLED_APPS.remove('some_app')
# Remove a hash key: LOGGING['handlers']['mail_admins'].pop('class', None)

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ['example.com', 'www.example.com']),
    TIME_ZONE=(str, 'America/Chicago'),
    SSL_ENABLED=(bool, False),
    SECURE_PROXY_SSL_HEADER=(bool, False),
    SESSION_COOKIE_SECURE=(bool, False),
    CSRF_COOKIE_SECURE=(bool, False),
    SESSION_EXPIRE_AT_BROWSER_CLOSE=(bool, False),
    SESSION_COOKIE_AGE=(int, 60 * 60 * 24 * 7 * 2),
    EMAIL_USE_TLS=(bool, False),
    EMAIL_PORT=(int, 25),
    CELERY_IS_ACTIVE=(bool, False),
    USE_DUMMY_CACHE=(bool, True),
)

environ.Env.read_env(os.path.join(PROJECT_ROOT, '.env'))


# ---------------------------------------------------------------------------- #
# Debug Setting
# ---------------------------------------------------------------------------- #

# Set DEBUG=True in .env for development/testing. Defaults to False for safer
# deploys (overrides Tendenci's DEBUG=True default).
DEBUG = env('DEBUG')

if DEBUG:
    disable_template_cache()


# ---------------------------------------------------------------------------- #
# Misc Site-Specific Settings
# ---------------------------------------------------------------------------- #

# Any site-specific settings that do not fit in the sections below can go here.


# ---------------------------------------------------------------------------- #
# Required Settings
# ---------------------------------------------------------------------------- #

# These must be set to two different random strings, at least 50 characters in
# length, that are unique to this site.  Django will refuse to start if these
# are not configured.
# The security of the site relies on these being appropriately random, so use a
# good random number generator.  Good random strings are conveniently available
# at https://www.grc.com/passwords.htm (Use the
# "63 random alpha-numeric characters" string, and refresh the page to get an
# additional string.)
SECRET_KEY = env('SECRET_KEY', default='')
SITE_SETTINGS_KEY = env('SITE_SETTINGS_KEY', default='')

# This must be set to a list of fully qualified domain names that are valid for
# this site.  Connections which request any other name will be rejected.
# To prevent HTTP Host header attacks, this list must be limited to names that
# are actually hosted on this server.
# If this server uses a wildcard DNS record then you can prefix the domain
# listed here with a '.' to match all subdomains ('.example.com').
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
if DEBUG:
    ALLOWED_HOSTS += ['localhost', '127.0.0.1', '[::1]']

# Prefer postgis:// so the GIS engine is preserved, e.g.:
# DATABASES_URL=postgis://tendenci:tendenci@localhost:5432/tendenci
# If unset, Tendenci's default DATABASES['default'] is left in place.
if env('DATABASES_URL', default=None):
    DATABASES['default'] = env.db('DATABASES_URL')

# This must be set to the time zone used by PostgreSQL, which defaults to the
# system time zone configured in /etc/timezone.
# To change the PostgreSQL time zone without changing the system time zone:
# sudo -u postgres psql -c "ALTER ROLE $DB_USER SET timezone TO 'US/Eastern';"
# A list of time zone names can be found at
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = env('TIME_ZONE')


# ---------------------------------------------------------------------------- #
# HTTPS and Session Settings
# ---------------------------------------------------------------------------- #

# Set SSL_ENABLED=True if this site supports HTTPS.
# This will cause the login page and other sensitive pages to require HTTPS.
SSL_ENABLED = env('SSL_ENABLED')

# Set SECURE_PROXY_SSL_HEADER=True if using NGINX.
# This will allow Tendenci to properly detect HTTP vs HTTPS client connections
# when using NGINX.  DO NOT use this if Tendenci is not behind NGINX, as that
# will open a security hole.
if env('SECURE_PROXY_SSL_HEADER'):
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Set these True if NGINX is configured to redirect all HTTP connections to
# HTTPS.  This is strongly recommended for live sites.
SESSION_COOKIE_SECURE = env('SESSION_COOKIE_SECURE')
CSRF_COOKIE_SECURE = env('CSRF_COOKIE_SECURE')

# Depending on configuration, logged in users may either be logged out when the
# user closes their browser, or may remain logged in after the user closes and
# reopens their browser.
# For logins through /admin/login/, SESSION_EXPIRE_AT_BROWSER_CLOSE controls
# this behavior.  (Default is False)
# For logins through /accounts/login/, the "Hide Remember Me" and
# "Remember Me Checked" settings in the "Users" app in Tendenci control this
# behavior, overriding SESSION_EXPIRE_AT_BROWSER_CLOSE.
SESSION_EXPIRE_AT_BROWSER_CLOSE = env('SESSION_EXPIRE_AT_BROWSER_CLOSE')
# Independently of the above behavior, users will also be logged out by both the
# server and their own browser if they do not visit the site for more than
# SESSION_COOKIE_AGE seconds.  However, each page load will reset this counter,
# allowing the user to remain logged in indefinitely as long as they continue to
# visit the site regularly.  (Default is 2 weeks)
SESSION_COOKIE_AGE = env('SESSION_COOKIE_AGE')


# ---------------------------------------------------------------------------- #
# EMail Settings
# ---------------------------------------------------------------------------- #

# Tendenci EMail is disabled by default (dummy backend).

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default=DEFAULT_FROM_EMAIL)
SERVER_EMAIL = env('SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

# If EMail is enabled, optionally uncomment and configure this to send an alert
# email to the specified addresses any time Python, Django, or Tendenci
# encounter an error.  This also enables some other non-error Tendenci email
# notifications.
#ADMINS = [('John', 'john@example.com'), ('Mary', 'mary@example.com')]
# To disable error emails and send only non-error Tendenci email notifications:
#disable_admin_emails()

EMAIL_BACKEND = env(
    'EMAIL_BACKEND',
    default='django.core.mail.backends.smtp.EmailBackend',
)
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_HOST = env('EMAIL_HOST', default='localhost')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')

# To send EMail via Amazon SES, set EMAIL_BACKEND=django_ses.SESBackend and
# configure AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY below in Amazon settings.

# To send newsletters via an SMTP server (example: mailgun):
#NEWSLETTER_EMAIL_HOST = 'smtp.mailgun.org'
#NEWSLETTER_EMAIL_PORT = 587
#NEWSLETTER_EMAIL_HOST_USER = ''
#NEWSLETTER_EMAIL_HOST_PASSWORD = ''

# To send newsletters via Amazon SES:
#NEWSLETTER_EMAIL_BACKEND = "django_ses.SESBackend"

# For development/testing:
# Try https://github.com/Nilhcem/FakeSMTP and use the SMTP configuration above,
# or try https://github.com/PaulSD/django_log_email and use the following
# configuration.
#EMAIL_BACKEND = 'django_log_email.backends.EmailBackend'
#EMAIL_LOG_FILE = '/var/log/tendenci/email.log'
# When using django_log_email, you can leave this setting commented to discard
# email after logging, or uncomment it to both log and send email.
#EMAIL_LOG_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# When using django_log_email, you can uncomment this setting to send error
# alert emails without logging.
#LOGGING['handlers']['mail_admins']['email_backend'] = 'django.core.mail.backends.smtp.EmailBackend'


# ---------------------------------------------------------------------------- #
# Payment Gateway Settings
# ---------------------------------------------------------------------------- #

#MERCHANT_LOGIN = env('MERCHANT_LOGIN', default='')
#MERCHANT_TXN_KEY = env('MERCHANT_TXN_KEY', default='')

# Authorize.Net
#AUTHNET_POST_URL = env(
#    'AUTHNET_POST_URL',
#    default='https://secure2.authorize.net/gateway/transact.dll',
#)
#AUTHNET_MD5_HASH_VALUE = env('AUTHNET_MD5_HASH_VALUE', default='')
#AUTHNET_CIM_API_TEST_URL = env(
#    'AUTHNET_CIM_API_TEST_URL',
#    default='https://apitest.authorize.net/xml/v1/request.api',
#)
#AUTHNET_CIM_API_URL = env(
#    'AUTHNET_CIM_API_URL',
#    default='https://api2.authorize.net/xml/v1/request.api',
#)

# FirstData
#FIRSTDATA_POST_URL = env(
#    'FIRSTDATA_POST_URL',
#    default='https://secure.linkpt.net/lpcentral/servlet/lppay',
#)

# FirstData E4
#FIRSTDATAE4_POST_URL = env(
#    'FIRSTDATAE4_POST_URL',
#    default='https://checkout.globalgatewaye4.firstdata.com/payment',
#)
#FIRSTDATA_RESPONSE_KEY = env('FIRSTDATA_RESPONSE_KEY', default='')
#FIRSTDATA_USE_RELAY_RESPONSE = env.bool('FIRSTDATA_USE_RELAY_RESPONSE', default=False)

# PayPal PayFlow Link
#PAYFLOWLINK_PARTNER = env('PAYFLOWLINK_PARTNER', default='')
#PAYPAL_MERCHANT_LOGIN = env('PAYPAL_MERCHANT_LOGIN', default='')
#PAYFLOWLINK_POST_URL = env(
#    'PAYFLOWLINK_POST_URL',
#    default='https://payflowlink.paypal.com',
#)

# PayPal
#PAYPAL_POST_URL = env(
#    'PAYPAL_POST_URL',
#    default='https://www.paypal.com/cgi-bin/webscr',
#)
# Or use the sandbox URL from Tendenci defaults:
#PAYPAL_POST_URL = PAYPAL_SANDBOX_POST_URL

# Stripe
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY', default='')
STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY', default='')


# ---------------------------------------------------------------------------- #
# Cache Settings
# ---------------------------------------------------------------------------- #

# If pylibmc is installed then Tendenci will attempt to connect to memcached on
# localhost.  If pylibmc and/or memcached is not installed then caching will be
# disabled.

# If multiple Tendenci sites share the same memcached, set SITE_CACHE_KEY to a
# value that is unique to this site.  This is used to prevent cache collisions
# between sites.
SITE_CACHE_KEY = env('SITE_CACHE_KEY', default=SITE_CACHE_KEY)
CACHE_PRE_KEY = SITE_CACHE_KEY

CACHES['default']['LOCATION'] = env(
    'CACHE_LOCATION',
    default=CACHES['default'].get('LOCATION', '127.0.0.1:11211'),
)

# To change the cache timeout:
# (Default is 30 days)
#CACHES['default']['TIMEOUT'] = 60*60*24*30
# USE_DUMMY_CACHE=True (default) forces DummyCache; set False to use Tendenci's
# memcached backend when available.
if env('USE_DUMMY_CACHE'):
    CACHES['default']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'

# ---------------------------------------------------------------------------- #
# Amazon S3 Storage Settings
# ---------------------------------------------------------------------------- #

AWS_LOCATION = env('AWS_LOCATION', default='')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default='')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', default='')
USE_S3_STORAGE = all([
    AWS_LOCATION,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_STORAGE_BUCKET_NAME,
])


# ---------------------------------------------------------------------------- #
# Celery Settings
# ---------------------------------------------------------------------------- #

CELERY_IS_ACTIVE = env('CELERY_IS_ACTIVE')


# ---------------------------------------------------------------------------- #
# Custom Application Settings
# ---------------------------------------------------------------------------- #

# To add an app to INSTALLED_APPS:
#INSTALLED_APPS += ['example_app']

# To remove a default app from INSTALLED_APPS:
#INSTALLED_APPS.remove('some_app')
# Or:
#remove_apps = ['app1', 'app2']
#for app in remove_apps:
#    INSTALLED_APPS.remove(app)

# To enable custom URL patterns to be configured in urls.py:
ROOT_URLCONF = 'conf.urls'

# To enable the Tendenci helpdesk app, uncomment this setting, uncomment
# ROOT_URLCONF above, and uncomment the helpdesk urlpattern in urls.py
#INSTALLED_APPS += ['markdown_deux', 'bootstrapform', 'tendenci.apps.helpdesk']


# ---------------------------------------------------------------------------- #
# Logging Settings
# ---------------------------------------------------------------------------- #

# By default, Tendenci logs all INFO and greater log messages to
# /var/log/tendenci/app.log
#
# When DEBUG is True, Tendenci logs DEBUG and greater log messages to
# /var/log/mysite/debug.log (in addition to logging INFO and greater log
# messages to /var/log/mysite/app.log)

# To change the log file names:
set_app_log_filename('/var/log/mysite/app.log')
set_debug_log_filename('/var/log/mysite/debug.log')

# To change the log level for the app.log file:
# (Valid levels are: 'DEBUG' 'INFO' 'WARNING' 'ERROR' 'CRITICAL')
#set_app_log_level('INFO')

# To disable logging:
disable_app_log()
disable_debug_log()

# To disable debug.log and write DEBUG messages to app.log when DEBUG is True:
#disable_debug_log()
#if DEBUG: set_app_log_level('DEBUG')

# To log to the console in addition to the log files (or instead of the log
# files if they are disabled above):
enable_console_log()
# To change the console log level:
#set_console_log_level('INFO')

# For more advanced configuration, you can modify the default LOGGING data
# structure, which is configured in
# https://github.com/tendenci/tendenci/blob/master/tendenci/settings.py
# For example:
#LOGGING['loggers']['django.db.backends']['level'] = 'DEBUG'
#LOGGING['loggers']['py.warnings'].pop('filters', None)

# To use Sentry (https://docs.sentry.io/), set SENTRY_DSN in .env:
SENTRY_DSN = env('SENTRY_DSN', default='')
if SENTRY_DSN:
    INSTALLED_APPS += ['raven.contrib.django.raven_compat']
    RAVEN_CONFIG = {'dsn': SENTRY_DSN}


# ---------------------------------------------------------------------------- #
# Additional Debugging Settings
# ---------------------------------------------------------------------------- #

# Uncomment and configure these settings to enable some additional debugging
# capabilities for clients connecting from one of the specified IPs.
# These debugging capabilities may expose internal/private data, so be careful
# to restrict this appropriately.
# Note that if you are running NGINX, all clients appear to be connecting from
# 127.0.0.1, so this example configuration will give all clients access to these
# debugging capabilities.
#if DEBUG:
#    INTERNAL_IPS = ['127.0.0.1', '::1']

# ---------------------------------------------------------------------------- #
# These lines must remain at the end of this file
# ---------------------------------------------------------------------------- #
from tendenci.apps.registry.utils import update_addons  # noqa: E402
INSTALLED_APPS = update_addons(INSTALLED_APPS, SITE_ADDONS_PATH)
