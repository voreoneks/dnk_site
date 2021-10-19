# Generated by Django 3.2.5 on 2021-10-19 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('release', '0013_auto_20211019_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songers', models.CharField(max_length=100, verbose_name='Исполнитель')),
                ('video_title', models.CharField(max_length=100, verbose_name='Название видео')),
                ('feat', models.CharField(blank=True, max_length=100, null=True, verbose_name='feat.')),
                ('words_author', models.CharField(max_length=100, verbose_name='Автор слов')),
                ('music_author', models.CharField(max_length=100, verbose_name='Автор музыки')),
                ('lexis', models.CharField(choices=[('NO', 'Отсутствует'), ('YES', 'Присутствует')], max_length=15, verbose_name='Ненормативная лексика в песне')),
                ('director', models.CharField(max_length=100, verbose_name='Режиссер')),
                ('timing', models.CharField(max_length=5, verbose_name='Хронометраж')),
                ('release_year', models.CharField(max_length=4, verbose_name='Год выпуска')),
                ('video_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('video_preview', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Превью клипа')),
                ('production_country', models.CharField(max_length=100, verbose_name='Страна производства')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
