from django.urls import path
from .views import *

urlpatterns = [
    path('', MainInfoDocsView.as_view(), name='documents'),
    path('orginfo/', OrgInfoView.as_view(), name='orginfo'),
    path('choose/<int:id>/', choice, name='choice'),
    path('audio/', AudioDocsView.as_view(), name='audio'),
    path('video/', VideoDocsView.as_view(), name='video'), 
    path('licence/', LicenceView.as_view(), name='licence'),
    path('music_author/citizen/', )
]