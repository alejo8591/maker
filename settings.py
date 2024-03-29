# encoding: utf-8
# Copyright 2013 maker
# License
# coding=utf-8

"""
    Django settings for maker project.
"""

from os import path
PROJECT_ROOT = path.abspath(path.dirname(__file__)) # assuming settings are in the same dir as source

DEBUG = True
TEMPLATE_DEBUG = DEBUG

QUERY_DEBUG = False
QUERY_DEBUG_FULL = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

from core.db import DatabaseDict
DATABASES = DatabaseDict()

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Bogota'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-ES'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
FORMAT_MODULE_PATH = 'maker.formats'

MAKER_API_CONSUMER_DB = 'gis'
# OAUTH_DATA_STORE is needed for correct database setting up
OAUTH_DATA_STORE = 'maker.core.api.auth.store.store'


# Static files location for MAKER
STATIC_DOC_ROOT = path.join(PROJECT_ROOT, 'static')

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = path.join(STATIC_DOC_ROOT, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/media/'

# Captcha Settings
CAPTCHA_FONT_SIZE = 30
CAPTCHA_LENGTH = 6
CAPTCHA_DISABLE = True
CAPTCHA_FOREGROUND_COLOR = '#333333'
CAPTCHA_NOISE_FUNCTIONS = []

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static-admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'z_#oc^n&z0c2lix=s$4+z#lsb9qd32qtb!#78nk7=5$_k3lq16'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)


MIDDLEWARE_CLASSES = (
    'johnny.middleware.LocalStoreClearMiddleware',
    'johnny.middleware.QueryCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'maker.core.middleware.domain.DomainMiddleware',
    'maker.core.middleware.user.SSLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'maker.core.middleware.user.AuthMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'maker.core.middleware.chat.ChatAjaxMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
    "maker.core.middleware.modules.ModuleDetect",
    "minidetector.Middleware",
    "maker.core.middleware.user.CommonMiddleware",
    "maker.core.middleware.user.PopupMiddleware",
    "maker.core.middleware.user.LanguageMiddleware",
)

ROOT_URLCONF = 'maker.urls'

TEMPLATE_DIRS = (
    path.join(PROJECT_ROOT, 'templates'),
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'django_websocket',
    'django.contrib.messages',
    'maker.account',
    'maker.core',
    'maker.core.api',
    'maker.core.search',
    'maker.documents',
    'maker.events',
    'maker.finance',
    'maker.identities',
    'maker.infrastructure',
    'maker.knowledge',
    'maker.messaging',
    'maker.news',
    'maker.projects',
    'maker.reports',
    'maker.sales',
    'maker.services',
    'dajaxice',
    'dajax',
    'nuconnector',
    'coffin',
    'captcha',
    'south',
)

TEST_RUNNER = 'maker.core.test_runner.CustomTestRunner'

AUTH_PROFILE_MODULE = 'core.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'maker.core.auth.HashBackend',
    'maker.core.auth.EmailBackend',
)

# LDAP Configuration
#AUTH_LDAP_SERVER_URI = 'ldap://'
#AUTH_LDAP_BIND_DN = ""
#AUTH_LDAP_BIND_PASSWORD = ""
#AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=example,dc=com",
#        ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
#AUTH_LDAP_START_TLS = True

#
# MAKER configuration
#
MAKER_MODULE_IDENTIFIER = 'hmodule'

MAKER_DEFAULT_USER_ID = 1

MAKER_DEFAULT_PERMISSIONS = 'everyone'

MAKER_SEND_EMAIL_TO_CALLER = True

MAKER_ALLOW_EMAIL_NOTIFICATIONS = True
MAKER_ALLOW_GRITTER_NOTIFICATIONS = True

MAKER_PASSWORD_LENGTH_MIN = 4

MAKER_RESPONSE_FORMATS = {
                             'html': 'text/html',
                             'mobile': 'text/html',
                             'json': 'text/plain',
                             #'json': 'application/json',
                             'ajax': 'text/plain',
                             #'ajax': 'application/json',
                             'csv': 'text/csv',
                             'xls': 'text/xls',
                             'pdf': 'application/pdf',
                             'rss': 'application/rss+xml',
                             }

MAKER_IMAGE_MAX_SIZE = (300, 400)
MAKER_IMAGE_RESIZE_FILTER = 'ANTIALIAS'

MAKER_MINIFY_JSON = False

MAKER_PAGINATOR_LENGTH = 20
MAKER_PAGINATOR_PAGES = 15

#
# CRON Fine-tuning
#

# How often should we loop through jobs, add/remove from pool, recycle jobs:
MAKER_CRON_PERIOD = 10 # seconds, default 60

# Number of cycles to keep HIGH priority jobs before forcefully terminating
#MAKER_CRON_HIGH_PRIORITY = 10 # defualt 10 cycles

# Number of cycles to keep LOW priority jobs before forcefully terminating
#MAKER_CRON_LOW_PRIORITY = 3 # default 3 cycles

# Number of seconds since last access to domain to give the job HIGH priority
#MAKER_CRON_QUALIFY_HIGH = 10 # default 10 cycles

# Number of seconds since last access to domain to run cron jobs for the domain
#MAKER_CRON_QUALIFY_RUN = 86400 # seconds, default 86400, i.e. 1 day

# Number of jobs to keep in the pool at the same time
#MAKER_CRON_POOL_SIZE = 10 # default 10

# Priority value at which we should try to gracefully end a job
#MAKER_CRON_SOFT_KILL = 0 # defualt 0

# Priority value at which we must kill a job using any possible means (kill -9 job)
#MAKER_CRON_HARD_KILL = -1 # defualt -1

# Seconds to wait between SIGKILL signals to a dead job
#MAKER_CRON_GRACE_WAIT = 5 # default 5

# CHAT CRON!
MAKER_CRON_DISABLED = True # Run chat?

### CRON config ends here

MAKER_MULTIPLE_LOGINS_DISABLED = False

# (GMT+00:00) UTC
MAKER_SERVER_DEFAULT_TIMEZONE = 21
MAKER_SERVER_TIMEZONE =  (('0', u'(GMT-11:00) International Date Line West'),
                             ('1', u'(GMT-11:00) Midway Island'), ('2', u'(GMT-11:00) Samoa'),
                             ('3', u'(GMT-10:00) Hawaii'), ('4', u'(GMT-09:00) Alaska'),
                             ('5', u'(GMT-08:00) Tijuana'), ('6', u'(GMT-08:00) Pacific Time (US & Canada)'),
                             ('7', u'(GMT-07:00) Arizona'), ('8', u'(GMT-07:00) Arizona'),
                             ('9', u'(GMT-08:00) Pacific Time (US & Canada)'), ('10', u'(GMT-07:00) Arizona'),
                             ('11', u'(GMT-07:00) Mountain Time (US & Canada)'), ('12', u'(GMT-07:00) Chihuahua'),
                             ('13', u'(GMT-07:00) Mazatlan'), ('14', u'(GMT-06:00) Central Time (US & Canada)'),
                             ('15', u'(GMT-06:00) Guadalajara'), ('16', u'(GMT-06:00) Mexico City'),
                             ('17', u'(GMT-06:00) Monterrey'), ('18', u'(GMT-06:00) Saskatchewan'),
                             ('19', u'(GMT-05:00) Eastern Time (US & Canada)'), ('20', u'(GMT-05:00) Indiana (East)'),
                             ('21', u'(GMT-05:00) Bogota'), ('22', u'(GMT-05:00) Lima'),
                             ('23', u'(GMT-05:00) Quito'), ('24', u'(GMT-04:30) Caracas'),
                             ('25', u'(GMT-04:00) Atlantic Time (Canada)'), ('26', u'(GMT-04:00) La Paz'),
                             ('27', u'(GMT-04:00) Santiago'), ('28', u'(GMT-03:30) Newfoundland'),
                             ('29', u'(GMT-08:00) Pacific Time (US & Canada)'), ('30', u'(GMT-03:00) Brasilia'),
                             ('31', u'(GMT-03:00) Buenos Aires'), ('32', u'(GMT-03:00) Georgetown'),
                             ('33', u'(GMT-03:00) Greenland'), ('34', u'(GMT-02:00) Mid-Atlantic'),
                             ('35', u'(GMT-01:00) Azores'), ('36', u'(GMT-01:00) Cape Verde Is.'),
                             ('37', u'(GMT+00:00) Casablanca'), ('38', u'(GMT+00:00) Dublin'),
                             ('39', u'(GMT+00:00) Edinburgh'), ('40', u'(GMT+00:00) Lisbon'),
                             ('41', u'(GMT+00:00) London'), ('42', u'(GMT+00:00) Monrovia'),
                             ('43', u'(GMT+00:00) UTC'), ('44', u'(GMT+01:00) Amsterdam'),
                             ('45', u'(GMT+01:00) Belgrade'), ('46', u'(GMT+01:00) Berlin'),
                             ('47', u'(GMT+01:00) Bern'), ('48', u'(GMT+01:00) Bratislava'),
                             ('49', u'(GMT+01:00) Brussels'), ('50', u'(GMT+01:00) Budapest'),
                             ('51', u'(GMT+01:00) Copenhagen'), ('52', u'(GMT+01:00) Ljubljana'),
                             ('53', u'(GMT+01:00) Madrid'), ('54', u'(GMT+01:00) Paris'),
                             ('55', u'(GMT+01:00) Prague'), ('56', u'(GMT+01:00) Rome'),
                             ('57', u'(GMT+01:00) Sarajevo'), ('58', u'(GMT+01:00) Skopje'),
                             ('59', u'(GMT+01:00) Stockholm'), ('60', u'(GMT+01:00) Vienna'),
                             ('61', u'(GMT+01:00) Warsaw'), ('62', u'(GMT+01:00) West Central Africa'),
                             ('63', u'(GMT+01:00) Zagreb'), ('64', u'(GMT+02:00) Athens'),
                             ('65', u'(GMT+02:00) Bucharest'), ('66', u'(GMT+02:00) Cairo'),
                             ('67', u'(GMT+02:00) Harare'), ('68', u'(GMT+02:00) Helsinki'),
                             ('69', u'(GMT+02:00) Istanbul'), ('70', u'(GMT+02:00) Jerusalem'),
                             ('71', u'(GMT+02:00) Kyev'), ('72', u'(GMT+02:00) Minsk'),
                             ('73', u'(GMT+02:00) Pretoria'), ('74', u'(GMT+02:00) Riga'),
                             ('75', u'(GMT+02:00) Sofia'), ('76', u'(GMT+02:00) Tallinn'),
                             ('77', u'(GMT+02:00) Vilnius'), ('78', u'(GMT+03:00) Baghdad'),
                             ('79', u'(GMT+03:00) Kuwait'), ('80', u'(GMT+03:00) Moscow'),
                             ('81', u'(GMT+03:00) Nairobi'), ('82', u'(GMT+03:00) Riyadh'),
                             ('83', u'(GMT+03:00) St. Petersburg'), ('84', u'(GMT+03:00) Volgograd'),
                             ('85', u'(GMT+03:30) Tehran'), ('86', u'(GMT+04:00) Abu Dhabi'),
                             ('87', u'(GMT+04:00) Baku'), ('88', u'(GMT+04:00) Muscat'),
                             ('89', u'(GMT+04:00) Tbilisi'), ('90', u'(GMT+04:00) Yerevan'),
                             ('91', u'(GMT+04:30) Kabul'), ('92', u'(GMT+05:00) Ekaterinburg'),
                             ('93', u'(GMT+05:00) Islamabad'), ('94', u'(GMT+05:00) Karachi'),
                             ('95', u'(GMT+05:00) Tashkent'), ('96', u'(GMT+05:30) Chennai'),
                             ('97', u'(GMT+05:30) Kolkata'), ('98', u'(GMT+05:30) Mumbai'),
                             ('99', u'(GMT+05:30) New Delhi'), ('100', u'(GMT+05:30) Sri Jayawardenepura'),
                             ('101', u'(GMT+05:45) Kathmandu'), ('102', u'(GMT+06:00) Almaty'),
                             ('103', u'(GMT+06:00) Astana'), ('104', u'(GMT+06:00) Dhaka'),
                             ('105', u'(GMT+06:00) Novosibirsk'), ('106', u'(GMT+06:30) Rangoon'),
                             ('107', u'(GMT+07:00) Bangkok'), ('108', u'(GMT+07:00) Hanoi'),
                             ('109', u'(GMT+07:00) Jakarta'), ('110', u'(GMT+07:00) Krasnoyarsk'),
                             ('111', u'(GMT+08:00) Beijing'), ('112', u'(GMT+08:00) Chongqing'),
                             ('113', u'(GMT+08:00) Hong Kong'), ('114', u'(GMT+08:00) Irkutsk'),
                             ('115', u'(GMT+08:00) Kuala Lumpur'), ('116', u'(GMT+08:00) Perth'),
                             ('117', u'(GMT+08:00) Singapore'), ('118', u'(GMT+08:00) Taipei'),
                             ('119', u'(GMT+08:00) Ulaan Bataar'), ('120', u'(GMT+08:00) Urumqi'),
                             ('121', u'(GMT+09:00) Osaka'), ('122', u'(GMT+09:00) Sapporo'),
                             ('123', u'(GMT+09:00) Seoul'), ('124', u'(GMT+09:00) Tokyo'),
                             ('125', u'(GMT+09:00) Yakutsk'), ('126', u'(GMT+09:30) Adelaide'),
                             ('127', u'(GMT+09:30) Darwin'), ('128', u'(GMT+10:00) Brisbane'),
                             ('129', u'(GMT+10:00) Canberra'), ('130', u'(GMT+10:00) Guam'),
                             ('131', u'(GMT+10:00) Hobart'), ('132', u'(GMT+10:00) Melbourne'),
                             ('133', u'(GMT+10:00) Port Moresby'), ('134', u'(GMT+10:00) Sydney'),
                             ('135', u'(GMT+10:00) Vladivostok'), ('136', u'(GMT+11:00) Magadan'),
                             ('137', u'(GMT+11:00) New Caledonia'), ('138', u'(GMT+11:00) Solomon Is.'),
                             ('139', u'(GMT+12:00) Auckland'), ('140', u'(GMT+12:00) Fiji'),
                             ('141', u'(GMT+12:00) Kamchatka'), ('142', u'(GMT+12:00) Marshall Is.'),
                             ('143', u'(GMT+12:00) Wellington'), ('144', u'(GMT+13:00) Nukualofa'),
                             )

#
# Messaging
#
MAKER_MESSAGING_POP3_LIMIT = 100 # number of emails
MAKER_MESSAGING_IMAP_LIMIT = 200 # number of emails

MAKER_MESSAGING_UNSAFE_BLOCKS = ('head', 'object', 'embed', 'applet', 'noframes',
                                    'noscript', 'noembed', 'iframe', 'frame', 'frameset')

MAKER_MESSAGING_IMAP_DEFAULT_FOLDER_NAME = 'UNSEEN'

MAKER_SIGNALS_AUTOCREATE_USER = False

MAKER_HELP_LINK_PREFIX = '/help/'
MAKER_HELP_SOURCE = 'http://www.maker.com/help'

MAKER_LANGUAGES = (('en', u'English'), ('ru', u'Русский'), ('es', u'Español'), ('de', u'Deutsche'), ('zh_CN', u'简体中文'), ('fr', u'Français'), ('el', u'ελληνικά'), ('pt_BR', u'português'))
MAKER_LANGUAGES_DEFAULT = 'es'

MAKER_AJAX_RELOAD_ON_REDIRECT = ('home',
                                    'user_login',
                                    'account_settings_view',
                                    'core_admin_index_perspectives',
                                    'core_admin_perspective_view',
                                    'core_settings_view')

MAKER_FORCE_AJAX_RENDERING = True

#
# htsafe settings
#

# Replace unsafe tags
MAKER_SAFE_TAGS = ('div', 'ul', 'li', 'label', 'span', 'strong', 'em', 'p', 'input',
                      'select', 'textarea', 'br')
MAKER_UNSAFE_TAGS = ('script', 'object', 'embed',
                        'applet', 'noframes', 'noscript', 'noembed', 'iframe',
                        'frame', 'frameset')


#
# MAKER Subcription settings
#

EVERGREEN_FREE_USERS = 3

USER_PRICE = 15

MAKER_SUBSCRIPTION_CUSTOMIZATION = True

MAKER_SUBSCRIPTION_USER_LIMIT = 0

MAKER_SUBSCRIPTION_BLOCKED = False

MAKER_SUBSCRIPTION_SSL_ENABLED = False
MAKER_SUBSCRIPTION_SSL_ENFORCE = False

MAKER_DEMO_MODE = False


#
# Nuvius settings (for integration)
#
NUVIUS_URL = "http://nuvius.com"
NUVIUS_KEY = '28563.ff6ed93307fc398a52d312966c122660'
NUVIUS_SOURCE_ID = "28563"
NUVIUS_NEXT = "iframe"
NUVIUS_CHECK_USER_KEYS = True

NUVIUS_DATA_CACHE_LIFE = 600
CACHE_KEY_PREFIX = 'maker_'

#
# Email settings
#

"""
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'alejo8591@gmail.com'
EMAIL_HOST_PASSWORD = '2BeM5EIc'
"""
EMAIL_SERVER = 'smtp.gmail.com'
IMAP_SERVER = 'imap.gmail.com'
EMAIL_USERNAME = 'alejo8591@gmail.com'
EMAIL_PASSWORD = '2BeM5EIc'
EMAIL_FROM = 'alejo8591'
DEFAULT_SIGNATURE = """
Thanks!
The Tree.io Team
http://www.tree.io
            """


#
# Search index (Whoosh)
#
SEARCH_DISABLED = False
SEARCH_ENGINE = 'db'

from whoosh import fields
WHOOSH_SCHEMA = fields.Schema(id=fields.ID(stored=True, unique=True),
                              name=fields.TEXT(stored=True),
                              type=fields.TEXT(stored=True),
                              content=fields.TEXT,
                              url=fields.ID(stored=True))

WHOOSH_INDEX = path.join(PROJECT_ROOT, 'storage/search')

#
# CACHING
#
#CACHE_BACKEND = 'dummy://'
CACHE_BACKEND = 'locmem://?timeout=30'
#CACHE_BACKEND = 'memcached://127.0.0.1:11211/?timeout=30'

#CACHE_BACKEND="johnny.backends.locmem://"

JOHNNY_MIDDLEWARE_KEY_PREFIX = 'jc_maker'

DISABLE_QUERYSET_CACHE = False

MAKER_OBJECT_BLACKLIST = ['id', 'creator', 'object_name', 'object_type',
                             'trash', 'full_access', 'read_access', 'nuvius_resource',
                             'object_ptr', 'comments', 'likes', 'dislikes', 'tags',
                             'links', 'subscribers','read_by']

MAKER_UPDATE_BLACKLIST = ['likes', 'dislikes', 'tags', 'reference', 'total',
                             'links', 'subscribers', 'read_by', 'date_created', 'last_updated']

MAKER_TIMEZONE_BLACKLIST = ['date_created', 'last_updated', 'time_from', 'time_to']

WKPATH = path.join(PROJECT_ROOT, 'bin/wkhtmltopdf')
WKCWD = PROJECT_ROOT

CHAT_LONG_POLLING = False
CHAT_TIMEOUT = 25 # response time if not new data
CHAT_TIME_SLEEP_THREAD = 25 # interval for "Delete inactive users"
CHAT_TIME_SLEEP_NEWDATA = 1 # time sleep in expectation of new data

MESSAGE_STORAGE = 'maker.core.contrib.messages.storage.cache.CacheStorage'

# Dajaxice settings
DAJAXICE_MEDIA_PREFIX="dajaxice"
