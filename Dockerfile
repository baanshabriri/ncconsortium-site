# ---------- Builder ----------
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings
ENV SECRET_KEY=dummy-secret-key

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 manage.py collectstatic --noinput

# ---------- Runtime ----------
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

RUN addgroup --system nonroot && adduser --system --ingroup nonroot nonroot

COPY --from=builder /app /app
RUN chown -R nonroot:nonroot /app
USER nonroot

EXPOSE 8000

CMD ["python3", "-m", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
