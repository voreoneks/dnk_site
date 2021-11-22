from django.urls import path
from .views import *

urlpatterns = [
    path('', MainInfoView.as_view(), name='release'),
    path('delete_photo/', delete_photo, name='delete_r_photo'),
    path('delete_cover/', delete_cover, name='delete_r_cover'),
    path('delete_cover_psd/', delete_cover_psd, name='delete_r_cover_psd'),
    path('delete_preview/', delete_preview, name='delete_preview'),
    path('audio/single', AudioSingleView.as_view(), name='r_audio_single'),
    path('audio/album', AudioAlbumView.as_view(), name='r_audio_album'),
    path('clear_table/', clear_table, name='clear_table'),
    path('success/', success_page, name='r_success'),
    path('video/', VideoView.as_view(), name='r_video')
]