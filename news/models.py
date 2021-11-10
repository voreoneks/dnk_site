from django.contrib.auth.models import User
from django.db import models
from pathlib import Path
import os
from transliterate import translit

def update_filename(instance, filename):
    path = 'news/' 
    filename_ = translit(filename, language_code='ru', reversed=True)
    return os.path.join(path, filename_)

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название статьи')
    content = models.TextField(verbose_name='Контент статьи')
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    image = models.ImageField(verbose_name='Изображение', upload_to = 'news/%Y/%m/%d', blank=True)
    file = models.FileField(upload_to = update_filename, blank=True, verbose_name='Файл к новости')
    slug = models.SlugField(verbose_name='Slug', null=True)
    user_visible = models.ManyToManyField(User, verbose_name='Статья для пользователя', blank=True)

    def filename(self):
        return Path(self.file.url).name

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cтатья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']