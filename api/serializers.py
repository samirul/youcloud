from rest_framework import serializers
from .models import YtMusicFiles


class GetURLDownloadFileSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        if self.context['user']:
            ytmusic_user = self.context['user']
            validated_data['user'] = ytmusic_user
        ytmusic = YtMusicFiles.objects.create(**validated_data)
        return ytmusic

    class Meta:
        model = YtMusicFiles
        fields = ['id','created_by','downloaded_url_video_link', 'downloaded_music_title', 'downloaded_music_files','created_at', 'updated_at']

        
class GetAudioFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = YtMusicFiles
        fields = ['id', 'downloaded_url_video_link', 'downloaded_music_title', 'downloaded_music_files','created_at', 'updated_at']