from django.urls import path
from .views import *

urlpatterns = [
    path('', LkView.as_view(), name='lk'),
    path('success/', success_page, name='lk_success'),
]