#!/bin/sh

set -e

whoami

source /py/bin/activate
export PYTUBEFIX_CACHE_DIR=/youcloud-app/.pytubefix_cache

python manage.py collectstatic --noinput
python manage.py migrate

# DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

gunicorn youcloud.wsgi:application --bind 0.0.0.0:8000