FROM python:3.12.3
ENV PYTHONDONTWRITTEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
EXPOSE 5432
EXPOSE 6379
WORKDIR /youcloud-app
COPY requirements.txt /youcloud-app/
COPY . /youcloud-app/
COPY test.py /youcloud-app/
COPY scripts.sh .
RUN python -m venv /py && \
    source ~/py/bin/activate && \
    /py/bin/pip install --upgrade pip && \
    apt-get update && apt-get install vim -y && \
    apt-get install -y postgresql-client && \
    /py/bin/pip install --no-cache-dir -r /requirements.txt && \
    apt install -y ffmpeg && \
    adduser --disabled-password --no-create-home youcloud-app-user && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R youcloud-app-user:youcloud-app-user /vol && \
    chmod -R 755 /vol && \
    chmod +x scripts.sh

USER youcloud-app-user

CMD ["./scripts.sh"]