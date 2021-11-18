from django.forms import ModelForm, RadioSelect
from django.forms.widgets import FileInput, HiddenInput, Textarea

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
            'inst': 'Укажите полную ссылку на страницу аккаунта. Например: https://www.instagram.com/myaccount.',
            'facebook': 'Укажите полную ссылку на страницу аккаунта. Например: https://www.facebook.com/myaccount.',
            'youtube': 'Укажите полную ссылку на страницу аккаунта. Например: https://www.youtube.com/user/myaccount.',
            'tiktok': 'Укажите полную ссылку на страницу аккаунта. Например: https://www.tiktok.com/@tiktok.',
            'other': 'Укажите полные ссылки на страницы аккаунтов. Например: https://t.me/myaccount.',
            'vk': 'Полная ссылка на личную страницу и на официальное сообщество. Например: https://vk.com/myaccount.',

        }


class MarketingForm(ModelForm):
    class Meta:
        model = Marketing
        fields = ('positioning', 'where_from', 'affiliation', 'awards', 'photo', 'photo_link', 'inspiration', 'concept', 'guest_artists', 'user',)
        widgets = {
            'photo': FileInput,
            'guest_artists': Textarea(attrs={'rows': 5}),
            'concept': Textarea(attrs={'rows': 5}),
            'inspiration': Textarea(attrs={'rows': 5}),
            'awards': Textarea(attrs={'rows': 5}),
            'user': HiddenInput,
        }
        help_texts = {
            'positioning': 'Пример: независимый артист // андеграундный исполнитель // дуэт // группа // супергруппа // совместный проект и т.д.',
            'where_from': 'Пример: московский хип-хоп-артист // рок-группа из Уфы // Украинский поп-дуэт и т.д.',
            'affiliation': 'Пример: участник хип-хоп-формации,участник // бывший участник музыкальной группы',
            'photo_link': 'Вставьте ссылку на скачивание ваших фото. Инструкции по подбору фотографий по ссылке: <a href="https://disk.yandex.ru/d/qkZJhwS-Q9qc1w" target="_blank" style="text-decoration: underline;">https://disk.yandex.ru/d/qkZJhwS-Q9qc1w</a>.',
            'concept': 'Пример: история обреченных отношений // социально-политические гимны // рэп-манифест и т.д.',
        }

class PromoPlanForm(ModelForm):
    class Meta:
        model = PromoPlan
        fields = ('radio', 'pressa', 'social_crops', 'tv', 'info', 'other', 'project_plan', 'release_plan', 'user',)
        widgets = {
            'radio': Textarea(attrs={'rows': 5}),
            'pressa': Textarea(attrs={'rows': 5}), 
            'social_crops': Textarea(attrs={'rows': 5}), 
            'tv': Textarea(attrs={'rows': 5}), 
            'info': Textarea(attrs={'rows': 5}), 
            'other': Textarea(attrs={'rows': 5}), 
            'project_plan': Textarea(attrs={'rows': 5}), 
            'release_plan': Textarea(attrs={'rows': 5}),
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