import os
from celery import shared_task, current_task
from pydub import AudioSegment
from pytube import YouTube

from accounts.models import User
from .models import YtMusicFiles
from clean_text.clean_text_filter import remove_special_characters

@shared_task(bind=True)
def DownloadYtMusicMp3Task(self, user_id, link):
    try:
        current_task.update_state(state='PROGRESS', meta={'progress': 0})
        get_link = link
        yt = YouTube(get_link)
        video = yt.streams.filter(only_audio=True).first()
        path_dir = "media/youtube_files"
        title_ = remove_special_characters(yt.title).split()
        title = "-".join(title_)
        downloaded_file = video.download(output_path=path_dir, filename=title)
        base, _ = os.path.splitext(downloaded_file)

        audio = AudioSegment.from_file(downloaded_file)
        new_file = base + '.mp3'
        audio.export(new_file, format='mp3')

        user = User.objects.get(id=user_id)

        YtMusicFiles.objects.create(created_by=user, downloaded_url_video_link=get_link, downloaded_music_title=title, downloaded_music_files=new_file)

        os.remove(downloaded_file)

        current_task.update_state(state='PROGRESS', meta={'progress': 100})

        return 'success'
    except Exception as e:
        print(f"Something is Wrong: {e}")
