import os
from django.core.files import File
from django.core.files.storage import default_storage
from celery import shared_task, current_task
from pydub import AudioSegment
from pytubefix import YouTube
from pytubefix.cli import on_progress
from accounts.models import User
from clean_text.clean_text_filter import remove_special_characters
from .models import YtMusicFiles


@shared_task(bind=True)
def DownloadYtMusicMp3Task(self, user_id, link):
    try:
        current_task.update_state(state='PROGRESS', meta={'progress': 0})
        get_link = link
        yt = YouTube(get_link, use_oauth=True, allow_oauth_cache=True, on_progress_callback = on_progress)
        video = yt.streams.get_highest_resolution()
        path_dir = "youtube_files"
        title_ = remove_special_characters(yt.title).split()
        title = "-".join(title_)
        downloaded_file = video.download(output_path=path_dir, filename=title)
        base, _ = os.path.splitext(downloaded_file)

        audio = AudioSegment.from_file(downloaded_file)
        new_file = base + ".mp3"
        audio.export(new_file, format='mp3')

        user = User.objects.get(id=user_id)

        try:
            with open(new_file, 'rb') as f:
                file = File(f)
                file_path = default_storage.save(f"youtube_files/{os.path.basename(new_file)}", file)

                check_title_exist = YtMusicFiles.objects.select_related('created_by').filter(created_by=user, downloaded_music_title=title).defer('downloaded_music_files','created_at','updated_at')
                if not check_title_exist:
                    YtMusicFiles.objects.create(created_by=user, downloaded_url_video_link=get_link, downloaded_music_title=title, downloaded_music_files=file_path)
        except Exception as e:
            print(f"Something is Wrong: {e}")

        os.remove(downloaded_file)

        current_task.update_state(state='SUCCESS', meta={'progress': 100})

        return 'success'
    except Exception as e:
        current_task.update_state(state='FAILURE', meta={'progress': 0, 'error': str(e)})
        print(f"Something is Krong: {e}")
