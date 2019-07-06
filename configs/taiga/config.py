from .common import *

PUBLIC_REGISTER_ENABLED = True
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = '$TAIGA_SECRET'

MEDIA_URL = "$TAIGA_SCHEME://$TAIGA_HOST/media/"
STATIC_URL = "$TAIGA_SCHEME://$TAIGA_HOST/static/"
ADMIN_MEDIA_PREFIX = "$TAIGA_SCHEME://$TAIGA_HOST/static/admin/"
SITES["api"]["scheme"] = "$TAIGA_SCHEME"
SITES["api"]["domain"] = "$TAIGA_HOST"
SITES["front"]["scheme"] = "$TAIGA_SCHEME"
SITES["front"]["domain"] = "$TAIGA_HOST"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "$POSTGRES_DB",
        "HOST": "$POSTGRES_HOST",
        "USER": "$POSTGRES_USER",
        "PASSWORD": "$POSTGRES_PASSWORD"
    }
}

DEFAULT_FROM_EMAIL = "donotreply@" + "$TAIGA_HOST"
CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 #seconds
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False # You cannot use both (TLS and SSL) at the same time!
EMAIL_HOST = 'mail-relay'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://$RABBIT_USER:$RABBIT_PASSWORD@$RABBIT_HOST:$RABBIT_PORT/$RABBIT_VHOST"}