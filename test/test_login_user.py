import json
import pytest

# Result: Passed

@pytest.mark.django_db()
def test_register_user(client):
    response = client.post('/api/registration/', {
        "username": "cat",
        "email": "cat@example.com",
        "password1": "cat@123A",
        "password2": "cat@123A"
    })
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'access' in data
    assert 'refresh' in data
    assert 'user' in data
    assert 'pk' in data['user']
    assert data['user']['username'] == 'cat'
    assert response.status_code == 201


@pytest.mark.django_db()
def test_login_user(client, register_user):
    response = client.post('/api/auth/login/',{
        "email": "cat@example.com",
        "password": "cat@123A"
    })
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'access' in data
    assert 'refresh' in data
    assert 'user' in data
    assert 'pk' in data['user']
    assert data['user']['username'] == 'cat'
    assert response.status_code == 200