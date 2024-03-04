from django.db import models
from BaseId.models import BaseIdModel

class YtMusicFiles(BaseIdModel):
    downloaded_url_video_link = models.CharField(max_length=255)
    downloaded_music_files = models.FileField(upload_to='youtube_files')
    objects = models.Manager()

    def __str__(self):
        return str(self.downloaded_url_video_link)
