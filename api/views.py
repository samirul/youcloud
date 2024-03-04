from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult

from api.models import YtMusicFiles
from api.tasks import DownloadYtMusicMp3Task

from .serializers import GetAudioFilesSerializer, GetURLDownloadFileSerializer


class GetURLDownloadFileViews(APIView):
    def post(self, request):
        serializer = GetURLDownloadFileSerializer(data=request.data)
        if serializer.is_valid():
            try:
                get_link = request.data.get('downloaded_url_video_link')
                downloadmp3 = DownloadYtMusicMp3Task.delay(get_link)
                return Response({'msg': 'File downloaded successfully', 'download_id': downloadmp3.id }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'error': 'something is wrong'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, downloadmp3_id):
        task_result = AsyncResult(downloadmp3_id)
        if task_result.successful():
            return Response({'status': 'Downloding Success !'})
        if task_result.failed():
            return Response({'status': 'Downloading Failed !', 'message': task_result.result})
        if task_result.status == 'PENDING':
            return Response({'status': 'Paste Youtube Link..'})
        if task_result.status == 'PROGRESS':
            return Response({'status': 'Downloading Progress..', 'progress': task_result.info})
        
class GetAudioFiles(APIView):
    def get(self, request):
        try:
            audio_files = YtMusicFiles.objects.all()
            serializer = GetAudioFilesSerializer(instance=audio_files, many=True)
            return Response(serializer.data)
        except Exception:
            return Response({'errors':'No downloaded content.'}, status= status.HTTP_204_NO_CONTENT)
        

