FROM python:3.11.4
ENV PYTHONDONTWRITTEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
EXPOSE 5432
EXPOSE 6379
WORKDIR /youcloud-app
COPY requirements.txt /youcloud-app/
COPY . /youcloud-app/
COPY scripts.sh .
RUN apt update && \
    apt-get install -y postgresql-client && \
    pip install --no-cache-dir -r requirements.txt && \
    apt install -y ffmpeg && \
    adduser --disabled-password --no-create-home youcloud-app-user && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R youcloud-app-user:youcloud-app-user /vol && \
    chmod -R 755 /vol && \
    chmod +x scripts.sh
    
COPY cipher.py /usr/local/lib/python3.11/site-packages/pytube/
COPY innertube.py /usr/local/lib/python3.11/site-packages/pytube/
USER youcloud-app-user

CMD ["./scripts.sh"]