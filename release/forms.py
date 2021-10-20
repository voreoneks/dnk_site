from django.forms import ModelForm, RadioSelect
from django.forms.widgets import HiddenInput

from .models import *


class MainInfoForm(ModelForm):
    class Meta:
        model = MainInfo
        fields = ['name', 'phone_number', 'email', 'is_update_photo', 'photo_link', 'photo', 'content_type', 'cover', 'cover_psd', 'num_songs', 'user',]
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
        fields = ('songers', 'song_title', 'album_title', 'feat', 'genre', 'fio_songer', 'words_author', 'music_author', 'owner_citizenship', 'record_country', 'timing', 'song_preview', 'lexis', 'audio', 'audio_link', 'clean_link', 'song_text', 'release_year', 'user',)
        help_texts = {
            'songers':'Написать имя исполнителя в том виде, в каком оно будет отражено на площадках. Если в песне несколько основных исполнителей, просьба заполнить всех основных исполнителей через запятую. Пример: "Джиган, Тимати, Егор Крид"',
            'feat': 'Если в песне присутствует артист на фите, просьба ответить в формате: "_________ (feat. _______)". Пример: МИШКА (feat. KATERINA).',
            'words_author': 'ФИО Автора слов',
            'music_author': 'ФИО Автора музыки',
            
        }
        
        widgets = {
            'user': HiddenInput,
        }

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ('songers', 'video_title', 'feat', 'words_author', 'music_author', 'lexis', 'director', 'timing', 'release_year', 'video_link', 'video_preview', 'production_country', 'user',)

        help_texts = {
            'songers': 'Написать имя исполнителя в том виде, в каком оно будет отражено на площадках. Если в песне несколько основных исполнителей, просьба заполнить всех основных исполнителей через запятую. Пример: "Джиган, Тимати, Егор Крид"',
            'feat': 'Если в видео присутствует артист на фите, просьба ответить в формате: "_________ (feat. _______)". Пример: МИШКА (feat. KATERINA).',
            'words_author': 'ФИО Автора слов',
            'music_author': 'ФИО Автора музыки',
            'director': 'ФИО Режиссёра',
            'video_link': 'Используйте Google Drive или Яндекс Диск. Использовать облачные хранилища, в которых материал удаляется через неделю - запрещено.',
            'video_preview': 'Загрузите картинку, которая станет обложкой вашего клипа. Это может быть кадр из клипа или фотография.',
        }

        widgets = {
            'user': HiddenInput,
        }
