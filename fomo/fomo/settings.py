"""
Django settings for fomo project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1htt1lx*!0e=9o2&h4*bk!&@f2gceai4!n-4ul5#w1$zmcg=d8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'account.FomoUser'

LOGIN_URL = '/account/login'

# Stripe API Keys
STRIPE_PUBLIC_KEY = 'pk_test_jbrwqk6C9nSritKUogsOTHRj'
STRIPE_PRIVATE_KEY = 'sk_test_d3PRcjrGAxq5k2Fs8jXSpH5b'

# Google Server Keys
GOOGLE_SERVER_KEY = 'AIzaSyCR5es2f7QwaoMKOJH0L8FXN3BeYs_QG-4'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus',
    'polymorphic',
    'homepage',
    'catalog',
    'account',
    'manager',
    'formlib',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_mako_plus.RequestInitMiddleware',
    # 'fomo.middleware.LastFiveMiddleware',
]

ROOT_URLCONF = 'fomo.urls'

TEMPLATES = [
   {
       'NAME': 'django_mako_plus',
       'BACKEND': 'django_mako_plus.MakoTemplates',
       'OPTIONS': {
           # functions to automatically add variables to the params/context before templates are rendered
           'CONTEXT_PROCESSORS': [
               'django.template.context_processors.static',            # adds "STATIC_URL" from settings.py
               'django.template.context_processors.request',           # adds "request" object
               'django.contrib.auth.context_processors.auth',          # adds "user" and "perms" objects
               'django_mako_plus.context_processors.settings',         # adds "settings" dictionary
           ],

           # identifies where the Mako template cache will be stored, relative to each template directory
           'TEMPLATES_CACHE_DIR': '.cached_templates',

           # the default app and page to render in Mako when the url is too short
           'DEFAULT_PAGE': 'index',
           'DEFAULT_APP': 'homepage',

           # the default encoding of template files
           'DEFAULT_TEMPLATE_ENCODING': 'utf-8',

           # these are included in every template by default - if you put your most-used libraries here, you won't have to import them exlicitly in templates
           'DEFAULT_TEMPLATE_IMPORTS': [
             'import django_mako_plus',
             'import os, os.path, re, json',
           ],

           # see the DMP online tutorial for information about this setting
           'URL_START_INDEX': 0,

           # whether to send the custom DMP signals -- set to False for a slight speed-up in router processing
           # determines whether DMP will send its custom signals during the process
           'SIGNALS': True,

           # whether to minify using rjsmin, rcssmin during 1) collection of static files, and 2) on the fly as .jsm and .cssm files are rendered
           # rjsmin and rcssmin are fast enough that doing it on the fly can be done without slowing requests down
           'MINIFY_JS_CSS': True,

           # the name of the SASS binary to run if a .scss file is newer than the resulting .css file
           # happens when the corresponding template.html is accessed the first time after server startup
           # if DEBUG=False, this only happens once per file after server startup, not for every request
           # specify the binary in a list below -- even if just one item (see subprocess.Popen)
           #'SCSS_BINARY': [ '/usr/bin/env', 'scss', '--unix-newlines' ],
           'SCSS_BINARY': None,

           # see the DMP online tutorial for information about this setting
           # it can normally be empty
           'TEMPLATES_DIRS': [
               # '/var/somewhere/templates/',
           ],
       },
   },

   # you'll likely already have the DjangoTemplates settings here
    {
        'NAME': 'django',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors':[
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
 ]

WSGI_APPLICATION = 'fomo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fomo',
        'USER': 'postgres',
        'PASSWORD': 'IsabellJ7260',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'   # you probably already have this
STATICFILES_DIRS = (
 # SECURITY WARNING: this next line must be commented out at deployment
 BASE_DIR,
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEBUG_PROPAGATE_EXCEPTIONS = DEBUG  # never set this True on a live site
LOGGING = {
     'version': 1,
     'disable_existing_loggers': True,
     'formatters': {
         'simple': {
             'format': '%(levelname)s %(message)s'
         },
     },
     'handlers': {
         'console':{
             'level':'DEBUG',
             'class':'logging.StreamHandler',
             'formatter': 'simple'
         },
     },
     'loggers': {
         'django_mako_plus': {
             'handlers': ['console'],
             'level': 'DEBUG',
             'propagate': False,
         },
     },
 }

# Active Directory Backend Integration
AD_ADMIN_DN = 'CN=Administrator,CN=Users,DC=familymusic,DC=local'
AD_ADMIN_PASS = 'PythonDanger12'
AD_SERVER = 'localhost'

AUTHENTICATION_BACKENDS = (
    #'fomo.backends.ActiveDirectoryBackend',
    'django.contrib.auth.backends.ModelBackend',
    )
