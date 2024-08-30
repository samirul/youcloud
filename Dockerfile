FROM python:3.12.3
ENV PYTHONDONTWRITTEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTUBEFIX_CACHE_DIR=/youcloud-app/.pytubefix_cache
ENV PATH="/py/bin:$PATH"
EXPOSE 8000
EXPOSE 5432
EXPOSE 6379
WORKDIR /youcloud-app
COPY requirements.txt /youcloud-app/
COPY . /youcloud-app/
COPY test.py /youcloud-app/
COPY scripts.sh .
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update && apt-get install vim -y && \
    apt-get install -y postgresql-client && \
    /py/bin/pip install --no-cache-dir -r requirements.txt && \
    apt install -y ffmpeg && \
    adduser --disabled-password --no-create-home youcloud-app-user && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    mkdir -p /youcloud-app/.pytubefix_cache && \
    chown -R youcloud-app-user:youcloud-app-user /vol && \
    chown -R youcloud-app-user:youcloud-app-user /youcloud-app/.pytubefix_cache && \
    chmod -R 755 /vol && \
    chmod +x scripts.sh

COPY innertube.py /py/lib/python3.12/site-packages/pytubefix/

USER youcloud-app-user

CMD ["./scripts.sh"]