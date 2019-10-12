import os


# Please don't change following settings unless you know what you are doing
STATIC_ROOT = '/data/static'

MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')

# SECURITY WARNING: keep the secret key used in production secret!
# Or just write your own secret-key here instead of using a env-variable
### MUST MATCH THE VALUE OF PINRY_SERCRET_KEY IN YOUR .env FILE
SECRET_KEY = "change me"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# SECURITY WARNING: use your actual domain name in production!
### MUST MATCH THE VALUE OF PINRY_DOMAIN IN YOUR .env FILE
ALLOWED_HOSTS = ['pinry.yourdomain.org']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#### CHANGE THE VALUES OF USER AND PASSWORD BELOW TO MATCH THE VALUES IN YOUR .env FILE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'pinry-db',
        'NAME': 'pinry',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
    }
}

# Allow users to register by themselves
ALLOW_NEW_REGISTRATIONS = True

# Delete image files once you remove your pin
IMAGE_AUTO_DELETE = True

# thumbnail size control
IMAGE_SIZES = {
    'thumbnail': {'size': [240, 0]},
    'standard': {'size': [600, 0]},
    'square': {'crop': True, 'size': [125, 125]},
}

# Whether people can view pins without login
PUBLIC = True


# Setup support for proxy headers
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
