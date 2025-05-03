"""
Django settings for config project.

Created for producion environment.
"""

from .base_settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": config('DATABASE_NAME'),
#         "USER": config('DATABASE_USER'),
#         "PASSWORD": config('DATABASE_PASSWORD'),
#         "HOST": config('DATABASE_HOST'),
#         "PORT": config('DATABASE_PORT'),
#     }
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR / "static")

# Security settings
# https://docs.djangoproject.com/en/4.2/topics/security/

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF=True,
SECURE_REFERRER_POLICY='strict-origin-when-cross-origin',
SECURE_CROSS_ORIGIN_OPENER_POLICY=True 
SECURE_SSL_REDIRECT=True

