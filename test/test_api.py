import json
import pytest
from django.urls import reverse
from api.tasks import DownloadYtMusicMp3Task

# Result: Passed

@pytest.mark.django_db
def test_GetURLDownloadFileViewsID(get_user, client):
    _, user_id = get_user
    link = "https://youtu.be/_s7iMASihSQ?si=5JhdHQUulyEOOSdw"
    data = {"downloaded_url_video_link": link}
    response = client.post(reverse("download"), content_type='application/json', data=json.dumps(data))
    content = response.content.decode('utf-8')
    data = json.loads(content)
    download_id = data['download_id']
    response_2 = client.get(reverse("download-musics-id", args=[download_id]), content_type='application/json')
    content_2 = response_2.content.decode('utf-8')
    data_2 = json.loads(content_2)

    assert DownloadYtMusicMp3Task.delay(user_id, link).get(timeout=5) == 'success'
    assert data_2['status'] == 'Downloading Success.'
    assert data_2['progress'] == {'progress': 100}


@pytest.mark.django_db()
def test_Get_audio_files(download_music, client):
    response = client.get(reverse('show-musics'))
    content = response.content.decode('utf-8')
    data = json.loads(content)
    assert 'id' in data[0]
    assert 'downloaded_music_files' in data[0]
    assert 'downloaded_url_video_link' in data[0]
    assert data[0]['downloaded_music_title'] == 'OFFLINE'
    assert response.status_code == 200



@pytest.mark.django_db()
def test_delete_audio_file(get_music_id, client):
    data_ = get_music_id
    response = client.get(f'/audio/delete-audio/{data_.id}/')
    print(response) # temp
    assert response.status_code == 200

    