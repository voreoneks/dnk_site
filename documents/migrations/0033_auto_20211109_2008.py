# Generated by Django 3.2.5 on 2021-11-09 17:08

from django.db import migrations, models
import documents.models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0032_auto_20211106_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfodocs',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=documents.models.update_filename, verbose_name='Обложка (jpg 3000x3000)'),
        ),
        migrations.AlterField(
            model_name='maininfodocs',
            name='release_type',
            field=models.CharField(choices=[('ALBUM', 'Альбом / ЕР'), ('SINGLE', 'Сингл'), ('CLIP', 'Видеоклип')], default='SINGLE', max_length=15, null=True, verbose_name='Тип релиза'),
        ),
        migrations.AlterField(
            model_name='orginfosam',
            name='skan_passport',
            field=models.ImageField(blank=True, null=True, upload_to=documents.models.update_filename, verbose_name='Скан паспорта'),
        ),
    ]
