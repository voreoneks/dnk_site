from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

class MainInfoMarketing(models.Model):
    release_type_choices = {
        ('SINGLE', 'Сингл'),
        ('ALBUM', 'Альбом / ЕР'),
        ('MAXI_SINGLE', 'Максисингл'),
        ('CLIP', 'Видеоклип'),
    }
    genre_choices = [
        ('NONE', 'Не выбрано'),
        ('BLUES','BLUES'), ('CHILDREN`S','CHILDREN`S'),
        ('CHRISTIAN','CHRISTIAN'), ('CLASSICAL','CLASSICAL'),
        ('COUNTRY','COUNTRY'), ('EDUCATIONAL','EDUCATIONAL'),
        ('ELECTRONIC','ELECTRONIC'), ('FOLK','FOLK'),
        ('HIP-HOP/RAP','HIP-HOP/RAP'), ('HOLIDAY','HOLIDAY'),
        ('JAZZ','JAZZ'), ('LATIN MUSIC','LATIN MUSIC'),
        ('METAL','METAL'), ('NEW AGE','NEW AGE'),
        ('POP','POP'), ('ALTERNATIVE','ALTERNATIVE'),
        ('R&B','R&B'), ('ROCK','ROCK'),
        ('PUNK','PUNK'), ('WORLD MUSIC','WORLD MUSIC'),
    ]

    songers = models.CharField(max_length=100, verbose_name='Исполнитель')
    release_title = models.CharField(max_length=100, verbose_name='Название релиза')
    release_type = models.CharField(max_length=20, choices=release_type_choices, default='SINGLE', verbose_name='Тип релиза')
    genre = models.CharField(max_length=20, choices=genre_choices, default='NONE', verbose_name='Жанр')
    vk = models.CharField(max_length=100, verbose_name='VK')
    inst = models.CharField(max_length=50, verbose_name='Instagram')
    facebook = models.CharField(max_length=100, verbose_name='Facebook', blank=True, null=True)
    youtube = models.CharField(max_length=100, verbose_name='Youtube', blank=True, null=True)
    tiktok = models.CharField(max_length=100, verbose_name='TikTok', blank=True, null=True)
    other = models.CharField(max_length=500, verbose_name='Другие социальные сети', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Marketing(models.Model):
    positioning = models.CharField(max_length=500, verbose_name='Позиционирование')
    where_from = models.CharField(max_length=500, verbose_name='Страна / город')
    affiliation = models.CharField(max_length=500, verbose_name='Принадлежность к музыкальному / творческому сообществу')
    awards = models.CharField(max_length=1024, verbose_name='Основные музыкальные награды и достижения')
    photo = models.ImageField(upload_to = 'uploads/%Y/%m/%d/', verbose_name='Качественные фотографии, которые будут отправлены редакторам площадок', blank=True, null=True)
    photo_link = models.URLField(verbose_name='Качественные фотографии, которые будут отправлены редакторам площадок', blank=True, null=True)
    inspiration = models.CharField(max_length=2048, verbose_name='Источник вдохновения (Артисты, альбомы, фильмы, страны и т.д.)')
    concept = models.CharField(max_length=2048, verbose_name='Концепция записи // Идея, главная задумка')
    guest_artists = models.CharField(max_length=1024, verbose_name='Приглашенные артисты и продюсеры с примерами песен, в записи которых они участвовали')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class PromoPlan(models.Model):
    radio = models.CharField(max_length=1024, verbose_name='Радио', blank=True, null=True)
    pressa = models.CharField(max_length=1024, verbose_name='Пресса', blank=True, null=True)
    social_crops = models.CharField(max_length=1024, verbose_name='Посевы в соцсетях', blank=True, null=True)
    tv = models.CharField(max_length=1024, verbose_name='TV', blank=True, null=True)
    info = models.CharField(max_length=1024, verbose_name='Информация по клипу', blank=True, null=True)
    other = models.CharField(max_length=1024, verbose_name='Другая информация по продвижению релиза', blank=True, null=True)
    project_plan = models.CharField(max_length=1024, verbose_name='Планы по развитию проекта', blank=True, null=True)
    release_plan = models.CharField(max_length=1024, verbose_name='План релизов на ближайшие полгода', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class PressRelease(models.Model):
    press_release = models.TextField(verbose_name='Пресс-релиз')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
