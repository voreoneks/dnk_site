from django.contrib.auth.models import User
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название статьи')
    content = models.TextField(verbose_name='Контент статьи')
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    image = models.ImageField(verbose_name='Изображение', upload_to = 'images/%Y/%m/%d', blank=True)
    user_visible = models.ManyToManyField(User, verbose_name='Статья для пользователя', blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cтатья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']