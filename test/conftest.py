import os
import json
import pytest
from django.test import Client
from django.urls import reverse




@pytest.fixture
def client():
    return Client()


@pytest.fixture
def google_login(client):
    code = os.getenv('GOOGLE_CODE')
    data = {"code": code}
    client.post(reverse('google'), content_type='application/json', data=json.dumps(data))



pytest_plugins = ('celery.contrib.pytest', )

@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': os.environ.get('CELERY_BROKER_URL_LINK'),
        'result_backend': os.environ.get('CELERY_BROKER_URL_LINK')
    }



