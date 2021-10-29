from django.urls import path
from .views import *

urlpatterns = [
    path('', MainInfoDocsView.as_view(), name='documents'),
    path('orginfo/', OrgInfoView.as_view(), name='orginfo'),
    path('audio/', AudioDocsView.as_view(), name='d_audio'),
    path('video/', VideoDocsView.as_view(), name='d_video'), 
    path('licence/', LicenceView.as_view(), name='licence'),
    path('music_author/<int:num_author>/', MusicAuthorView.as_view(), name='music_author'),
    path('words_author/<int:num_author>/', WordsAuthorView.as_view(), name='words_author'),
    path('others/<int:num_others>/', OthersView.as_view(), name='others'),
    path('phon_maker/<int:num_phon_maker>/', PhonMakerView.as_view(), name='phon_maker'),
    path('delete_music_author/', delete_music_author, name='delete_music_author'),
    path('delete_words_author/', delete_words_author, name='delete_words_author'),
    path('delete_others/', delete_others, name='delete_others'),
    path('delete_phon_maker/', delete_phon_maker, name='delete_phon_maker'),
    path('success/', success_page, name='d_success')
]