FROM python:3.12
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements-freeze.txt /app/requirements-freeze.txt
RUN pip install --no-cache-dir -r requirements-freeze.txt

COPY . .

ENTRYPOINT python manage.py collectstatic --noinput && python manage.py migrate && exec gunicorn --bind 0.0.0.0:8079 -w 4 --threads 4 --worker-class="gthread" --keep-alive 30 --preload config.wsgi
