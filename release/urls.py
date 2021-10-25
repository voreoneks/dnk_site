from django.urls import path
from .views import *

urlpatterns = [
    path('', MainInfoView.as_view(), name='release'),
    path('audio/', AudioView.as_view(), name='r_audio'),
    path('success/', success_page, name='r_success'),
    path('video/', VideoView.as_view(), name='r_video')
]