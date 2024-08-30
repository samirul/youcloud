from rest_framework import serializers
from .models import YtMusicFiles


class GetURLDownloadFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = YtMusicFiles
        fields = ['id','created_by','downloaded_url_video_link', 'downloaded_music_title', 'downloaded_music_files','created_at', 'updated_at']

        
class GetAudioFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = YtMusicFiles
        fields = ['id', 'downloaded_url_video_link', 'downloaded_music_title', 'downloaded_music_files','created_at', 'updated_at']