from django.db import models
from django.contrib.auth.models import User
from django.http import request

def user_directory_path(instance):
    return 'uploads/{0}/%Y/%m/%d/'.format(instance.user.user.username)

class MainInfo(models.Model):
    bool_choices = [
        ('NO', 'Нет'),
        ('YES', 'Да'),
    ]
    content_choices = [
        ('SINGLE', 'Сингл'),
        ('ALBUM', 'Альбом'),
        ('CLIP', 'Видеоклип'),
    ]

    name = models.CharField(max_length=150, verbose_name='Имя артиста')
    phone_number = models.CharField(max_length=10, verbose_name='Телефон')
    email = models.EmailField(verbose_name='E-mail')
    is_update_photo = models.CharField(max_length=3, choices=bool_choices, verbose_name='Обновить/добавить фото в карточках артиста на площадках?', default='NO')
    photo_link = models.URLField(verbose_name='Ссылка на скачивание фото', null=True, blank=True)
    photo = models.ImageField(upload_to = user_directory_path, verbose_name='Прикрепить фото', blank=True)
    content_type = models.CharField(max_length=9, choices=content_choices, verbose_name='Тип релиза', default='SINGLE')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    