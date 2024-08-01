import os
import json
import pytest
from django.urls import reverse

# Result: Passed

@pytest.mark.django_db()
def test_google_login(client):
    code = code = os.getenv('GOOGLE_CODE')
    data = {"code": code}
    response = client.post(reverse('google'), content_type='application/json', data=json.dumps(data))
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'access' in data
    assert 'refresh' in data
    assert 'user' in data
    assert 'username' in data['user']
    assert response.status_code == 200


# pytest -v -s -vrx