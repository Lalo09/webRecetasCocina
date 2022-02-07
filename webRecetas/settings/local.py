from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'recetas',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        'POST':3306
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

#Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")