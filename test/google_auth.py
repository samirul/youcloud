import os
import json
import pytest
from django.urls import reverse


@pytest.mark.django_db()
def test_google_login(client):
    code = code = os.getenv('GOOGLE_CODE')
    data = {"code": code}
    response = client.post(reverse('google'), content_type='application/json', data=json.dumps(data))
    assert response.status_code == 200
    assert b'access' in response.content
    assert b'refresh' in response.content
    assert b'username' in response.content


# pytest -v -s -vrx