import os
from celery.result import AsyncResult
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import YtMusicFiles
from api.tasks import DownloadYtMusicMp3Task
from .serializers import GetAudioFilesSerializer, GetURLDownloadFileSerializer


class GetURLDownloadFileViews(APIView):
    '''
        Will fetch 'downloaded_url_video_link' from reactjs and then download youtube music file in the
        backend using celery task 
    '''
    permission_classes = [IsAuthenticated]
    def post(self, request):
        '''
            Will send POST request from frontend reactjs
        '''
        user_id = request.user.id
        serializer = GetURLDownloadFileSerializer(data=request.data, context={'user':request.user})
        if serializer.is_valid():
            try:
                get_link = request.data.get('downloaded_url_video_link')
                downloadmp3 = DownloadYtMusicMp3Task.delay(user_id, get_link)
                return Response({'msg': 'File downloaded successfully', 'download_id': downloadmp3.id }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        print(serializer.errors)
        return Response({'error': 'something is wrong'}, status=status.HTTP_400_BAD_REQUEST)


    
    def get(self, request, downloadmp3_id):
        '''
            Will show these celery status in frontend depends on progress using get request
            will send GET request from frontend reactjs
        '''
        task_result = AsyncResult(downloadmp3_id)
        status_messages = {
            'PROGRESS': {'status': 'Downloading Progress..', 'progress': task_result.info},
            'SUCCESS': {'status': 'Downloading Success.', 'progress': task_result.info},
            'PENDING': {'status': 'Your downloading is pending..'},
            'FAILURE': {'status': 'Downloading Failed.', 'message': task_result.info},
        }
    
        if status in status_messages:
            return Response(status_messages[status])
    
        return Response(status_messages.get(task_result.status, {'status': 'Unknown status'}))

        
        
        
class GetAudioFiles(APIView):
    '''
        Will show all the musics files after downloaded successfully by user to frontend reactjs
    '''
    permission_classes = [IsAuthenticated]
    def get(self, request):
        '''
            will send GET request from frontend reactjs
        '''
        try:
            audio_files = YtMusicFiles.objects.select_related('created_by').filter(created_by=request.user)
            serializer = GetAudioFilesSerializer(instance=audio_files, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response({'errors': 'No downloaded content.'}, status=status.HTTP_204_NO_CONTENT)


class DeleteAudioFiles(APIView):
    '''
        will delete specific music files from database and storage based on music file id send by user from frontend 
    '''
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        '''
            will send GET request from frontend reactjs
        '''
        try:
            audio_files = YtMusicFiles.objects.select_related('created_by').filter(created_by=request.user, id=pk)
            try:
                for audio in audio_files:
                    if audio:
                        path = os.path.join(f"youtube_files\{audio.downloaded_music_title}.mp3")
                        os.remove(path)
            except OSError:
                pass
            audio_files.delete()

                    
            return Response(status=status.HTTP_200_OK)
        except Exception:
          return Response({'errors': 'No downloaded content.'}, status=status.HTTP_204_NO_CONTENT)  
        
        
# https://testdriven.io/blog/django-rest-auth/