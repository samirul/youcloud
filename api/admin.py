from django.contrib import admin
from .models import YtMusicFiles


@admin.register(YtMusicFiles)
class YtMusicFilesAdmin(admin.ModelAdmin):
    list_display = [
      'id', 'created_by','downloaded_url_video_link', 'downloaded_music_title', 'downloaded_music_files', 'created_at', 'updated_at'
    ]
