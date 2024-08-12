import os
import json
import pytest
from django.test import Client
from django.urls import reverse
from api.models import YtMusicFiles
from accounts.models import User

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def register_user(client):
    response = client.post('/api/registration/', {
        "username": "cat",
        "email": "cat@example.com",
        "password1": "cat@123A",
        "password2": "cat@123A"
    })
    content = response.content.decode('utf-8')
    data = json.loads(content)
    return data

@pytest.fixture
def login_user(client, register_user):
    response = client.post('/api/auth/login/', {
        "email": "cat@example.com",
        "password": "cat@123A",
    })
    content = response.content.decode('utf-8')
    data = json.loads(content)
    return data, data['access']




@pytest.fixture
def get_user(login_user, client):
    _, access = login_user
    url = reverse('get_user')
    headers = {
        'HTTP_AUTHORIZATION': f'Bearer {access}',
    }
    response = client.get(url, **headers)
    content = response.content.decode('utf-8')
    data = json.loads(content)
    user = data['user']
    user_id = data['user']['id']
    return user, user_id


@pytest.fixture
def download_music(get_user, client):
    link = "https://youtu.be/_s7iMASihSQ?si=5JhdHQUulyEOOSdw"
    data = {"downloaded_url_video_link": link}
    response = client.post(reverse("download"), content_type='application/json', data=json.dumps(data))
    content = response.content.decode('utf-8')
    data = json.loads(content)
    return data

@pytest.fixture
def get_music_id(get_user, download_music, client):
    _, user_id = get_user
    response = client.get(reverse('show-musics'))
    content = response.content.decode('utf-8')
    data = json.loads(content)
    user = User.objects.get(id=user_id)
    saved_data = YtMusicFiles.objects.create(created_by=user, downloaded_url_video_link=data[0]['downloaded_url_video_link'],
                                downloaded_music_title=data[0]['downloaded_music_title'],
                                downloaded_music_files=data[0]['downloaded_music_files'])
    return saved_data
