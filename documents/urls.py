from django.urls import path
from .views import *

urlpatterns = [
    path('', MainInfoDocsView.as_view(), name='documents'),
    path('orginfo/', OrgInfoView.as_view(), name='orginfo'),
    path('choice/<int:id>/', choice, name='choice'),
    path('audio/', AudioDocsView.as_view(), name='audio'),
    path('video/', VideoDocsView.as_view(), name='video'), 
    path('licence/', LicenceView.as_view(), name='licence'),
    path('music_author/<str:author>/', MusicAuthorView.as_view(), name='music_author'),
    path('words_author/<str:author>/', WordsAuthorView.as_view(), name='words_author'),
    path('others/', OthersView.as_view(), name='others'),
    path('phon_maker/<str:maker>', PhonMakerView.as_view(), name='phon_maker'),
    path('success/', success_page, name='success')
]