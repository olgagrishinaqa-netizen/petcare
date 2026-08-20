FROM python:3.13-slim

WORKDIR /app

# Устанавливаем cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY scripts ./scripts

# Копируем cron файл
COPY cronjob /etc/cron.d/generate_reminders
RUN chmod 0644 /etc/cron.d/generate_reminders

# Создаем лог файл
RUN touch /var/log/cron.log

# Запускаем cron и приложение
CMD cron && uvicorn app.main:app --host 0.0.0.0 --port 8000
