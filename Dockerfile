FROM python:3.7
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .

# ENV MODE=dev
EXPOSE 8000
# django
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# sanic
# CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--worker-class", "sanic.worker.GunicornWorker"]
# gunicorn mysite.wsgi:application -w 3 -b 0.0.0.0:8000 --reload
CMD ["gunicorn", "opsweb.wsgi:application", "-w", "3", "-b", "0.0.0.0:8000", "--reload"]