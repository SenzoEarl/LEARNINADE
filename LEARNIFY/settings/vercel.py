import os
import dj_database_url
from .base import *

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['.vercel.app', 'localhost', '127.0.0.1']
if os.environ.get('VERCEL_URL'):
    ALLOWED_HOSTS.append(os.environ.get('VERCEL_URL'))

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Static files (CSS, JavaScript, Images)
# Whitenoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
# Vercel doesn't support persistent file storage, so media files will not persist between deployments.
# For a production app, use AWS S3 or similar.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# CSRF
if os.environ.get('VERCEL_URL'):
    CSRF_TRUSTED_ORIGINS = [f"https://{os.environ.get('VERCEL_URL')}"]
else:
    CSRF_TRUSTED_ORIGINS = ["https://*.vercel.app"]

# Security
SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

# Use dummy cache if redis is not available in Vercel
if not os.environ.get('REDIS_URL'):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
    # Disable channels if redis is missing (Channels requires a real backend for layers)
    CHANNEL_LAYERS = {}
else:
    REDIS_URL = os.environ.get('REDIS_URL')
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': REDIS_URL,
        }
    }
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                'hosts': [REDIS_URL],
            }
        }
    }
