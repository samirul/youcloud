import os
import re
from django.core.files import File
from django.core.files.storage import default_storage
from celery import shared_task, current_task
from pydub import AudioSegment
from pytube import YouTube
from pytube import cipher
from pytube.exceptions import RegexMatchError
from pytube. innertube import _default_clients
from accounts.models import User
from clean_text.clean_text_filter import remove_special_characters
from .models import YtMusicFiles


_default_clients[ "ANDROID"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients[ "ANDROID_EMBED"][ "context"][ "client"]["clientVersion"] = "19.08.35"
_default_clients[ "IOS_EMBED"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"][ "context"]["client"]["clientVersion"] = "6.41"
_default_clients[ "ANDROID_MUSIC"] = _default_clients[ "ANDROID_CREATOR" ]

def get_throttling_function_name(js: str) -> str:
    """Extract the name of the function that computes the throttling parameter.

    :param str js:
        The contents of the base.js asset file.
    :rtype: str
    :returns:
        The name of the function used to compute the throttling parameter.
    """
    function_patterns = [
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
    ]
    #logger.debug('Finding throttling function name')
    for pattern in function_patterns:
        regex = re.compile(pattern)
        function_match = regex.search(js)
        if function_match:
            #logger.debug("finished regex search, matched: %s", pattern)
            if len(function_match.groups()) == 1:
                return function_match.group(1)
            idx = function_match.group(2)
            if idx:
                idx = idx.strip("[]")
                array = re.search(
                    r'var {nfunc}\s*=\s*(\[.+?\]);'.format(
                        nfunc=re.escape(function_match.group(1))),
                    js
                )
                if array:
                    array = array.group(1).strip("[]").split(",")
                    array = [x.strip() for x in array]
                    return array[int(idx)]

    raise RegexMatchError(
        caller="get_throttling_function_name", pattern="multiple"
    )

cipher.get_throttling_function_name = get_throttling_function_name

@shared_task(bind=True)
def DownloadYtMusicMp3Task(self, user_id, link):
    try:
        current_task.update_state(state='PROGRESS', meta={'progress': 0})
        get_link = link
        yt = YouTube(get_link)
        video = yt.streams.filter(only_audio=True).first()
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
