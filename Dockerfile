FROM python:3.12
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements-freeze.txt /app/requirements-freeze.txt
RUN pip install --no-cache-dir -r requirements-freeze.txt

COPY start.sh /start.sh
RUN chmod +x /start.sh

COPY . .
