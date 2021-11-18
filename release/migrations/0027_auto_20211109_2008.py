# Generated by Django 3.2.5 on 2021-11-09 17:08

from django.db import migrations, models
import release.models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0026_alter_maininfo_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to=release.models.update_filename, verbose_name='Аудио (WAV)'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='clean_link',
            field=models.FileField(blank=True, null=True, upload_to=release.models.update_filename, verbose_name='Clean version трека (WAV)'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='instrumental',
            field=models.FileField(blank=True, null=True, upload_to=release.models.update_filename, verbose_name='Instrumental (минус)'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='song_text',
            field=models.FileField(blank=True, null=True, upload_to=release.models.update_filename, verbose_name='Текст песни'),
        ),
        migrations.AlterField(
            model_name='maininfo',
            name='cover_psd',
            field=models.FileField(blank=True, null=True, upload_to=release.models.update_filename, verbose_name='Обложка в слоях (PSD)'),
        ),
        migrations.AlterField(
            model_name='maininfo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=release.models.update_filename, verbose_name='Прикрепить фото'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_preview',
            field=models.ImageField(blank=True, null=True, upload_to=release.models.update_filename, verbose_name='Превью клипа'),
        ),
    ]