from django.urls import path
from .views import *

urlpatterns = [
    path('', MainInfoView.as_view(), name='release'),
    path('single/', single, name='single'),
]