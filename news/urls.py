from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsPage.as_view(), name='news'),
    path('download/<slug:slug_>/', download, name='download'),
]