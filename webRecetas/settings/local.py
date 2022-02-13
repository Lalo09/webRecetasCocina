from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database config
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

#Ruta static
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

#Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")