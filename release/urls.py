from django.urls import path
from .views import *

urlpatterns = [
    path('', MainInfoView.as_view(), name='release'),
    path('audio/', AudioView.as_view(), name='audio'),
    path('success/', success_page, name='success')
]