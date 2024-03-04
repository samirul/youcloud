import os
from celery import shared_task, current_task
from pydub import AudioSegment
from pytube import YouTube
from .models import YtMusicFiles

@shared_task(bind=True)
def DownloadYtMusicMp3Task(self, link):
    current_task.update_state(state='PROGRESS', meta={'progress': 0})
    get_link = link
    print(get_link)
    yt = YouTube(get_link)
    video = yt.streams.filter(only_audio=True).first()
    path_dir = "youtube_files"
    downloaded_file = video.download(output_path=path_dir)
    base, _ = os.path.splitext(downloaded_file)

    audio = AudioSegment.from_file(downloaded_file)
    new_file = base + '.mp3'
    audio.export(new_file, format='mp3')

    YtMusicFiles.objects.create(downloaded_url_video_link=get_link, downloaded_music_files=new_file)

    os.remove(downloaded_file)

    current_task.update_state(state='PROGRESS', meta={'progress': 100})

    return 'success'