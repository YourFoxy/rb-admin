#!/bin/sh

export CPU_COUNT=`grep -c ^processor /proc/cpuinfo `
export WORKER_COUNT=${WORKER_COUNT:-$(( $CPU_COUNT ))}
export MAX_REQUESTS=${MAX_REQUESTS:-10000}

echo "creating additional project files"
python manage.py collectstatic --noinput

echo "run migrations"
python manage.py migrate

exec gunicorn --bind 0.0.0.0:8079 -w "$WORKER_COUNT" --threads 4 --worker-class="gthread" --keep-alive 30 --preload config.wsgi
