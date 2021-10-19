from django.urls import path
from .views import *

urlpatterns = [
    path('', MainInfoDocsView.as_view(), name='documents'),
]