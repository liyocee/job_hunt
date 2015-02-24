from .base import *  # NOQA
DEBUG = True
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'memory'
    }
}
SOUTH_TESTS_MIGRATE = False
