# Generated by Django 3.2.5 on 2021-11-09 21:32

from django.db import migrations, models
import release.models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0027_auto_20211109_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio',
            field=models.FileField(null=True, upload_to=release.models.update_filename, verbose_name='Аудио (WAV)'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='clean_link',
            field=models.FileField(null=True, upload_to=release.models.update_filename, verbose_name='Clean version трека (WAV)'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='instrumental',
            field=models.FileField(null=True, upload_to=release.models.update_filename, verbose_name='Instrumental (минус)'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='song_text',
            field=models.FileField(null=True, upload_to=release.models.update_filename, verbose_name='Текст песни'),
        ),
    ]
