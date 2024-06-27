from django.urls import path
from api.views import GetAudioFiles, GetURLDownloadFileViews, DeleteAudioFiles

urlpatterns = [
    path("download/", GetURLDownloadFileViews.as_view(), name='download'),
    path("show-musics/", GetAudioFiles.as_view(), name='show-musics'),
    path("download/<downloadmp3_id>/", GetURLDownloadFileViews.as_view(), name='download-musics-id'),
    path("delete-audio/<str:pk>/", DeleteAudioFiles.as_view(), name='delete-audio'),
]
