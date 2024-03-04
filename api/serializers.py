import os
from rest_framework import serializers
from .models import YtMusicFiles

from django.conf import settings

class GetURLDownloadFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = YtMusicFiles
        fields = ['id','downloaded_url_video_link','created_at', 'updated_at']

        
class GetAudioFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = YtMusicFiles
        fields = ['id','downloaded_music_files','created_at', 'updated_at']