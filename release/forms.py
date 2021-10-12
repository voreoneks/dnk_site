from django.forms import ModelForm, RadioSelect
from django.forms.widgets import HiddenInput
from .models import *

class MainInfoForm(ModelForm):
    class Meta:
        model = MainInfo
        fields = ['name', 'phone_number', 'email', 'is_update_photo', 'photo_link', 'photo', 'content_type', 'user']
        widgets = {
            'is_update_photo': RadioSelect,
            'content_type': RadioSelect,
            'user': HiddenInput,
        }
        help_texts = {
            'name':'Имя Артиста должно выглядеть так, как оно будет отражено на площадках',
            'email':'Для отчётов и дальнейшей коммуникации',
            'photo_link':'Вставьте ссылку на скачивание ваших фото. Инструкции по подбору фотографий по <a href = "https://disk.yandex.ru/d/qkZJhwS-Q9qc1w">ссылке.</a>',
            'photo':'Качественные фотографии для карточек артиста',
        }

class AudioForm(ModelForm):
    class Meta:
        model = Audio
        fields = ['songer', 'song_title', 'album_title', 'feat', 'genre', 'fio_songer', 'words_author', 'music_author', 'owner_citizenship', 'record_country', 'timing', 'song_preview', 'lexis', 'cover', 'cover_psd', 'audio', 'audio_link', 'clean_link', 'song_text', 'release_year', 'add_video', 'user']
        widgets = {
            'user': HiddenInput,
        }