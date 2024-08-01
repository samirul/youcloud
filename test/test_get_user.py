import json
import pytest
from django.urls import reverse

# Result: Passed

@pytest.mark.django_db()
def test_user(login_user, client):
    response = client.get(reverse('get_user'))
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'user' in data
    assert 'id' in data['user']
    assert 'username' in data['user']
    assert 'email' in data['user']
    assert data['user']['username'] == 'cat'
    assert data['user']['email'] == 'cat@example.com'
    assert response.status_code == 200
    