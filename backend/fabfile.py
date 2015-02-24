import os

from fabric.api import local

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def manage(command, args=''):
    local('{}/manage.py {} {}'.format(BASE_DIR, command, args))


def test(*args, **kwargs):
    manage('test')


def setup(*args, **kwargs):
    sudo = '' if 'no-sudo' in args else 'sudo -u postgres'
    local('%s psql -c "DROP DATABASE IF EXISTS job_match"' % sudo)
    local('%s psql -c "CREATE DATABASE job_match"' % sudo)
    local('{}/manage.py migrate'.format(BASE_DIR))
