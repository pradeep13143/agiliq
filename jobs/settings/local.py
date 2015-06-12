from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'join_agiliq.db',        # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = 'YMIYxrcdMe1tbDKy3zRAQDEM5AW7W2iiMvZxqP74tePZxjBlKE'

EMAIL_HOST_USER = 'pradeepkumarg13@gmail.com'
EMAIL_HOST_PASSWORD = '9620305657'
EMAIL_HOST = 'smtp.gmail.com'

# Email settings
EMAIL_USE_TLS = True
EMAIL_PORT = 587
