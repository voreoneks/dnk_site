from typing import TypedDict
from django.db.models.enums import ChoicesMeta
from django.forms import ModelForm, RadioSelect
from django.forms.models import ModelMultipleChoiceField
from django.forms.widgets import ChoiceWidget, HiddenInput, MultipleHiddenInput, Select, TextInput
from .models import *

class MainInfoForm(ModelForm):
    class Meta:
        model = MainInfo
        fields = ['name', 'phone_number', 'email', 'is_update_photo', 'photo_link', 'photo', 'content_type', 'cover', 'cover_psd', 'num_songs', 'user']
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
        fields = ('songers', 'song_title', 'album_title', 'feat', 'genre', 'fio_songer', 'words_author', 'music_author', 'owner_citizenship', 'record_country', 'timing', 'song_preview', 'lexis', 'audio', 'audio_link', 'clean_link', 'song_text', 'release_year', 'add_video', 'user')
        help_texts = {
            'songers':'Написать имя исполнителя в том виде, в каком оно будет отражено на площадках. Если в песне несколько основных исполнителей, просьба заполнить всех основных исполнителей через запятую. Пример: "Джиган, Тимати, Егор Крид"',
            'feat': 'Если в песне присутствует артист на фите, просьба ответить в формате: "_________ (feat. _______)". Пример: МИШКА (feat. KATERINA).',
            'words_author': 'ФИО Автора слов',
            'music_author': 'ФИО Автора музыки',
            
        }
        
        widgets = {
            'user': HiddenInput,
            'id': MultipleHiddenInput,
        }