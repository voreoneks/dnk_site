from django.db.models import fields
from django.forms import ModelForm, RadioSelect
from django.forms import widgets
from django.forms.widgets import HiddenInput, Textarea

from .models import *


class MainInfoMarketingForm(ModelForm):
    class Meta:
        model = MainInfoMarketing
        fields = ('songers', 'release_title', 'release_type', 'genre', 'vk', 'inst', 'facebook', 'youtube', 'tiktok', 'other', 'user',)
        widgets = {
            'user': HiddenInput,
            'release_type': RadioSelect,
        }
        help_texts = {
            'vk': 'Ссылка на личную страницу и на официальное сообщество',

        }


class MarketingForm(ModelForm):
    class Meta:
        model = Marketing
        fields = ('positioning', 'where_from', 'affiliation', 'awards', 'photo', 'photo_link', 'inspiration', 'concept', 'guest_artists', 'user',)
        widgets = {
            'user': HiddenInput,
        }
        help_texts = {
            'positioning': 'Пример: независимый артист // андеграундный исполнитель // дуэт // группа // супергруппа // совместный проект и т.д.',
            'where_from': 'Пример: московский хип-хоп-артист // рок-группа из Уфы // Украинский поп-дуэт и т.д.',
            'affiliation': 'Пример: участник хип-хоп-формации,участник // бывший участник музыкальной группы',
            'photo_link': 'Вставьте ссылку на скачивание ваших фото. Инструкции по подбору фотографий по ссылке: https://disk.yandex.ru/d/qkZJhwS-Q9qc1w',
            'concept': 'Пример: история обреченных отношений // социально-политические гимны // рэп-манифест и т.д.',
        }

class PromoPlanForm(ModelForm):
    class Meta:
        model = PromoPlan
        fields = ('radio', 'pressa', 'social_crops', 'tv', 'info', 'other', 'project_plan', 'release_plan', 'user',)
        widgets = {
            'user': HiddenInput,
        }
        help_texts = {
            'radio':'Планируются ли премьеры на радиостанциях // гостевые эфиры // ротации // новинки //',
            'pressa':'Кто из СМИ, блоггеров поддерживаети в каких соцсетях, желательно с количеством фолловеров',
            'social_crops':'Какие паблики?',
            'tv':'Дата премьеры клипа на тв //гостевые эфиры // ротация нового клипа',
            'info':'Есть/планируется // дата релиза // режиссёр',
            'other':'Таргетированная реклама // перфоманс и инфлюенс-маркетинг',
            'project_plan':'Ближайшие концерты // презентации // туры',
            'release_plan':'Пример: ноябрь - Сингл, март - клип, май - Альбом, август - ВТБ Арена',
        }

class PressReleaseForm(ModelForm):
    class Meta:
        model = PressRelease
        fields = '__all__'
        widgets = {
            'user': HiddenInput,
            'press_release': Textarea(attrs={'rows': 5})
        }
        help_texts = {
            'press_release': 'Если у вас нет готового пресс-релиза, напишите основные детали о себе и своём релизе. Мы оформим это в текст.',
        }