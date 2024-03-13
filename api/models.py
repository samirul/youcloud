from django.db import models
from BaseId.models import BaseIdModel
from accounts.models import User

class YtMusicFiles(BaseIdModel):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    downloaded_url_video_link = models.CharField(max_length=255, null=True, blank=True)
    downloaded_music_title = models.CharField(max_length=255, null=True, blank=True)
    downloaded_music_files = models.FileField(upload_to='youtube_files', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.downloaded_url_video_link)
