import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication


from rest_framework import status

from api.models import YtMusicFiles
from api.tasks import DownloadYtMusicMp3Task

from .serializers import GetAudioFilesSerializer, GetURLDownloadFileSerializer

class GetURLDownloadFileViews(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user_id = request.user.id
        serializer = GetURLDownloadFileSerializer(data=request.data, context={'user':request.user})
        if serializer.is_valid():
            try:
                get_link = request.data.get('downloaded_url_video_link')
                print(get_link)
                downloadmp3 = DownloadYtMusicMp3Task.delay(user_id, get_link)
                return Response({'msg': 'File downloaded successfully', 'download_id': downloadmp3.id }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        print(serializer.errors)
        return Response({'error': 'something is wrong'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, downloadmp3_id):
        task_result = AsyncResult(downloadmp3_id)
        if task_result.successful():
            return Response({'status': 'Downloding Success !'})
        if task_result.failed():
            return Response({'status': 'Downloading Failed !', 'message': task_result.result})
        if task_result.status == 'PENDING':
            return Response({'status': 'Your downloading is pending..'})
        if task_result.status == 'PROGRESS':
            return Response({'status': 'Downloading Progress..', 'progress': task_result.info})
        
class GetAudioFiles(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            audio_files = YtMusicFiles.objects.select_related('created_by').filter(created_by=request.user)
            serializer = GetAudioFilesSerializer(instance=audio_files, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response({'errors': 'No downloaded content.'}, status=status.HTTP_204_NO_CONTENT)


class DeleteAudioFiles(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            audio_files = YtMusicFiles.objects.select_related('created_by').filter(created_by=request.user, id=pk)
            try:
                for audio in audio_files:
                    if audio:
                        path = os.path.join(f"media\youtube_files\{audio.downloaded_music_title}.mp3")
                        os.remove(path)
            except OSError:
                pass
            audio_files.delete()

                    
            return Response(status=status.HTTP_200_OK)
        except Exception:
          return Response({'errors': 'No downloaded content.'}, status=status.HTTP_204_NO_CONTENT)  
# https://testdriven.io/blog/django-rest-auth/